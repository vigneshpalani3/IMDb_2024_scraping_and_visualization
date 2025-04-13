from sqlalchemy import create_engine

def create_connection():
    username="root"
    host="localhost"
    password="%40Vicky143"
    database="imdb"

    return create_engine(f"mysql+pymysql://{username}:{password}@{host}/{database}")