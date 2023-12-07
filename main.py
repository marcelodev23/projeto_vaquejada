from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models.models_api import Pedidos,UserCreate,Usertipo,Evento,Pedido_type,login
from db.CRUD import setPedidoDB,setUserCreate,alterando_type_user,setEvento,pedidos_type,setLogin,getEvento,getPedidos,getpedido

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post('/user')
async def user(dados: UserCreate):
    return setUserCreate(email=dados.email,
                         senha=dados.password,
                         telefone=dados.telefone,
                         nome=dados.nome,pix=dados.pix)



@app.post('/login')
async def Login(dados:login):
    return setLogin(dados.email,dados.password)

@app.post('/user/type')
async def user(dados: Usertipo):
    return alterando_type_user(id=dados.id_user,tipo=dados.tipo,)
 
@app.post('/evento')
async def evento(dados: Evento):
    return setEvento(user_id=dados.id_user,
                     nome_parque=dados.nome_parque,
                     valor_senha=dados.valor_senha,
                     data=dados.date_evento,
                     quantidade_senha=dados.Quantidade_senhas,)

@app.post('/pedidos')
async def pedidos(dados: Pedidos):
    return setPedidoDB(id_evento=1,
                       puxador=dados.puxador,
                       esteira=dados.esteira,
                       numeros=dados.numeros,
                       telefone=dados.telefone,
                       representacao=dados.representacao,)
@app.get('/pedido/{telefone}')
async def getPedido(telefone:str):
    return getpedido(telefone)

@app.post('/pedidos/status')
async def pedidos_status(dados:Pedido_type):
    return pedidos_type(id=dados.id,tipo=dados.operação)

@app.get("/dados/{item}")
async def get_pedidos(item:str):
    if item =="pedidos":
        return getPedidos()
    elif item =='evento':
        return getEvento()