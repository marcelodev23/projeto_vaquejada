from pydantic import BaseModel
from typing import List, Optional


class UserCreate(BaseModel):
    nome: str
    email:str
    telefone: str
    password: str
    pix: Optional[str]

class login(BaseModel):
    email: str
    password:str


class Pedidos(BaseModel):
    id_evento: int
    puxador: str
    esteira: str
    representacao: str
    telefone: str
    numeros: str

class Evento(BaseModel):
    id_user: int
    nome_parque: str
    valor_senha: float
    date_evento: str
    Quantidade_senhas : int

class Usertipo(BaseModel):
    id_user:int
    tipo:int    

class Pedido_type(BaseModel):
   id: int
   operação:str
    

class nodificacao(BaseModel):
    id: int
    id_user: int
    id_root: int
    solicitacao:str
