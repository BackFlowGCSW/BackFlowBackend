from neomodel import config
from config.settings import NEO4J_URI, NEO4J_USER, NEO4J_PASSWORD

config.DATABASE_URL = f"neo4j+s://{NEO4J_USER}:{NEO4J_PASSWORD}@{NEO4J_URI.split('://')[-1]}"