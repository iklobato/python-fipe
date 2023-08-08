from datetime import datetime
from sqlalchemy import Column, DateTime, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class BaseUpdatedModel(Base):
    __abstract__ = True

    created_at = Column(DateTime, nullable=False, default=datetime.now)
    updated_at = Column(DateTime, nullable=False, default=datetime.now, onupdate=datetime.now)


class Marca(BaseUpdatedModel):
    __tablename__ = "marcas"

    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    fipe_id = Column(Integer, nullable=False)
    key = Column(String, nullable=False)


class Modelos(BaseUpdatedModel):
    __tablename__ = "modelos"

    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    fipe_id = Column(Integer, nullable=False)
    marca_id = Column(Integer, ForeignKey('marcas.id'), nullable=False)
    key = Column(String, nullable=False)

    marca = relationship('Marca')


class Anos(BaseUpdatedModel):
    __tablename__ = "anos"

    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    fipe_id = Column(Integer, nullable=False)
    modelo_id = Column(Integer, ForeignKey('modelos.id'), nullable=False)
    key = Column(String, nullable=False)

    modelo = relationship('Modelos')
