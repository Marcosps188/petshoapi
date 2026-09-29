from typing import Literal
from datetime import datetime
from pydantic import BaseModel, ConfigDict, EmailStr, Field


# schemas de entrada de dados (post/put)
class CategoriaSchema(BaseModel):
    nome: str = Field(min_length=2, max_length=50)


class UsuarioSchema(BaseModel):
    nome: str = Field(min_length=2, max_length=100)
    email: EmailStr
    telefone: str = Field(min_length=8, max_length=20)
    tipo_usuario: Literal["cliente", "freelancer"] = "cliente"


class FreelancerSchema(BaseModel):
    valor_hora: int = Field(gt=0)
    bio: str = Field(min_length=5)
    habilidade: str = Field(min_length=2)
    id_usuario: int
    id_categoria: int


# schemas de saida de dados
class CategoriaResponseSchema(CategoriaSchema):
    id_categoria: int
    model_config = ConfigDict(from_attributes=True)


class UsuarioResponseSchema(UsuarioSchema):
    id_usuario: int
    data_cadastro: datetime
    model_config = ConfigDict(from_attributes=True)


class UsuarioResumoSchema(BaseModel):
    nome: str
    email: str
    telefone: str
    model_config = ConfigDict(from_attributes=True)


class CategoriaResumoSchema(BaseModel):
    nome: str
    model_config = ConfigDict(from_attributes=True)


class FreelancerResponseSchema(BaseModel):
    id_freelancer: int
    valor_hora: int
    bio: str
    habilidade: str
    usuario: UsuarioResumoSchema
    categoria: CategoriaResumoSchema
    model_config = ConfigDict(from_attributes=True)