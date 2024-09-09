from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlmodel import SQLModel, Session, create_engine

database_file = 'planner.db'
database_url = 'sqlite:///' + database_file
connection_args = {"check_same_thread": False}
engine = create_engine(database_url, echo=True, connect_args={"check_same_thread": False})
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def conn():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session
    # db = SessionLocal()
    # try:
    #     yield db
    # finally:
    #     db.close()
