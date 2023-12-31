from sqlalchemy import MetaData, Column, DateTime, func
from sqlalchemy.ext.declarative import declarative_base

naming_convention = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}


class InsertionDateTime:
    insertion_time = Column(DateTime, server_default=func.now(), nullable=False)


Base = declarative_base(metadata=MetaData(naming_convention=naming_convention))
metadata = Base.metadata

