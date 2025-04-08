from neo4j import GraphDatabase
from config.settings import NEO4J_URI, NEO4J_USER, NEO4J_PASSWORD

driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))

def run_query(query: str, parameters: dict = {}):
    with driver.session() as session:
        return session.execute_write(lambda tx: tx.run(query, parameters))
