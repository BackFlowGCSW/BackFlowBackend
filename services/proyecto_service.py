from models.proyecto import Proyecto
from datetime import date
from fastapi import HTTPException
from factory.proyecto.proyecto_factory import ProyectoFactory
from typing import List
from models.organizacion import Organizacion
from models.rol import Rol
from models.usuario import Usuario
from neomodel import db

class ProyectoService:
    @staticmethod
    def crear_proyecto(data: dict) -> Proyecto:
        """
        Crea un nuevo proyecto validando datos, generando configuración base
        según la metodología (fases y roles) y asociando al creador y organización.
        """
        organizacion = ProyectoService._validar_organizacion(
            data["organizacion_id"])
        ProyectoService._validar_nombre_proyecto_unico(
            data["nombre"], organizacion)
        usuario = ProyectoService._validar_usuario(data["creado_por"])

        if "metodologia" not in data:
            raise HTTPException(
                status_code=400, detail="Métodología no especificada")
        creador = ProyectoFactory.get_creador(data["metodologia"])

        proyecto = creador.crear_proyecto(data)
        if proyecto.fecha_inicio and proyecto.fecha_fin:
            if proyecto.fecha_inicio > proyecto.fecha_fin:
                raise HTTPException(
                    status_code=400, detail="La fecha de inicio no puede ser posterior a la fecha de fin.")

        proyecto.fecha_creacion = date.today()
        proyecto.creado_por = data["creado_por"]
        proyecto.save()

        proyecto.miembros.connect(usuario)
        ProyectoService._asociar_organizacion(proyecto, organizacion)
        ProyectoService._asociar_fases(proyecto, creador)
        ProyectoService._asociar_roles(proyecto, creador)
        ProyectoService._asignar_rol_a_creador(proyecto, usuario)

        print(f"✅ Proyecto '{proyecto.nombre}' creado correctamente")
        return proyecto

    @staticmethod
    def listar_proyectos() -> List[dict]:
        """
        Lista todos los proyectos activos.
        """
        proyectos = Proyecto.nodes.filter(activo=True)
        return [{
            "uid": p.uid,
            "nombre": p.nombre,
            "descripcion": p.descripcion,
            "fecha_creacion": p.fecha_creacion.isoformat() if p.fecha_creacion else None,
            "fecha_inicio": p.fecha_inicio.isoformat() if p.fecha_inicio else None,
            "fecha_fin": p.fecha_fin.isoformat() if p.fecha_fin else None,
            "metodologia": p.metodologia,
            "repositorio": p.repositorio,
        } for p in proyectos]

    @staticmethod
    def editar_proyecto(uid: str, data: dict):
        """
        Edita los datos de un proyecto.
        """
        proyecto = Proyecto.nodes.get_or_none(uid=uid)
        if not proyecto:
            raise HTTPException(
                status_code=404, detail="Proyecto no encontrado")

        campos_permitidos = {
            "nombre", "descripcion", "fecha_inicio", "fecha_fin", "repositorio"
        }
        for campo, valor in data.items():
            if campo in campos_permitidos:
                setattr(proyecto, campo, valor)

        proyecto.save()
        return {"mensaje": "Proyecto actualizado correctamente"}

    @staticmethod
    def deshabilitar_proyecto(uid: str):
        """
        Desactiva un proyecto (soft delete).
        """
        proyecto = Proyecto.nodes.get_or_none(uid=uid)
        if not proyecto:
            raise HTTPException(
                status_code=404, detail="Proyecto no encontrado")

        proyecto.activo = False
        proyecto.save()
        return {"mensaje": "Proyecto deshabilitado"}

    # ----------- Metodos Privados --------------
    @staticmethod
    def _validar_organizacion(org_id: str) -> Organizacion:
        org = Organizacion.nodes.get_or_none(uid=org_id)
        if not org or not org.activa:
            raise HTTPException(
                status_code=404, detail="Organización no válida")
        return org

    @staticmethod
    def _validar_usuario(user_id: str) -> Usuario:
        user = Usuario.nodes.get_or_none(uid=user_id)
        if not user:
            raise HTTPException(
                status_code=404, detail="Usuario creador no encontrado")
        return user

    @staticmethod
    def _validar_nombre_proyecto_unico(nombre: str, org: Organizacion):
        proyectos = Proyecto.nodes.filter(nombre=nombre)
        for p in proyectos:
            if org in p.pertenece_a.all():
                raise HTTPException(
                    status_code=400, detail="Nombre de proyecto ya en uso en esa organización")

    @staticmethod
    def _asociar_organizacion(proyecto: Proyecto, org: Organizacion):
        proyecto.pertenece_a.connect(org)

    @staticmethod
    def _asociar_fases(proyecto: Proyecto, creador):
        fases = creador.crear_fases()
        for fase in fases:
            proyecto.fases.connect(fase)

    @staticmethod
    def _asociar_roles(proyecto: Proyecto, creador):
        roles = creador.crear_roles()
        for rol in roles:
            proyecto.tiene_rol.connect(rol)

    @staticmethod
    def _asignar_rol_a_creador(proyecto: Proyecto, usuario: Usuario):
        """
        Asigna automáticamente un rol al creador según la metodología del proyecto.
        """
        nombre_rol = {
            "SCRUM": "Scrum Master",
            "RUP": "Administrador de Configuración"
        }.get(proyecto.metodologia.upper(), "Líder")

        rol = next(
            (r for r in proyecto.tiene_rol.all() if r.nombre.lower() == nombre_rol.lower()),
            None
        )

        if rol:
            usuario.cumple_rol.connect(rol)
            print(f"✅ Rol '{nombre_rol}' asignado a {usuario.nombre}")
        else:
            print(f"⚠️ No se encontró el rol '{nombre_rol}' en el proyecto '{proyecto.nombre}'")

