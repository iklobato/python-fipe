from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel

Base = declarative_base()


class BaseUpdateModel(BaseModel):
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()

    def __init__(self, **data):
        super().__init__(**data)
        if 'id' in data:
            self.update_updated = datetime.now()

    class Config:
        orm_mode = True


class Marca(BaseUpdateModel):
    codigo: str
    nome: str

    def __repr__(self):
        return f"Marca(codigo={self.codigo}, nome={self.nome})"

    class Config:
        orm_mode = True


class Modelo(BaseUpdateModel):
    nome: str
    codigo: int

    def __repr__(self):
        return f"Modelo(codigo={self.codigo}, nome={self.nome})"

    class Config:
        orm_mode = True


class Ano(BaseUpdateModel):
    codigo: str
    nome: str

    def __repr__(self):
        return f"Ano(codigo={self.codigo}, nome={self.nome})"

    class Config:
        orm_mode = True


class Valor(BaseUpdateModel):
    tipo_veiculo: int
    valor: str
    marca: str
    modelo: str
    ano_modelo: int
    combustivel: str
    codigo_fipe: str
    mes_referencia: str
    sigla_combustivel: str

    class Config:
        orm_mode = True
