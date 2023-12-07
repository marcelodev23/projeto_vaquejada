import sqlite3
from time import sleep

conn = sqlite3.connect(r'/Users/marceloalves/Documents/Developer/Projetos/projeto_vaquejada/db/dados.db')
cursor = conn.cursor()

def getID_Pedidos_tamanho():
    cursor.execute(""" SELECT * FROM Pedidos;""")
    t = len(cursor.fetchall())
    conn.close()
    return t


def setNumeros(id,numeros):
    lista = numeros.split(',')
    for dado in lista:
        cursor.execute("""
INSERT INTO numeros(id_pedido,numero)
VALUES (?,?)
""", (id,dado))
        print('Dados inseridos com sucesso.')
        conn.commit()
        conn.close()

def getPedidos():
    sql = '''SELECT numero,puxador, esteira, representacao,status  
FROM Pedidos  
INNER JOIN numeros 
ON Pedidos.id = numeros.id_pedido;'''
    cursor.execute(sql) 
    result = cursor.fetchall() 
    result.sort()
    return result

def getEvento():
    sql = '''SELECT Nome_parque,Quantidade_senahs, Valor_senha, date_evento,nome  
FROM Evento  
INNER JOIN Use 
ON Evento.id = Use.id;'''
    cursor.execute(sql) 
    result = cursor.fetchall() 
    result.sort()
    return result

def setLogin(email:str,senha):
    import hashlib
    senha = hashlib.sha256(senha.encode('utf-8')).hexdigest()
    cursor.execute("""SELECT * FROM Use;""")
    valor=cursor.fetchall()
    resutado=''
    for i in range(0,len(valor)):
        if valor[i][1] == email:
            if valor[i][2] == senha:
                cursor.execute("""SELECT id FROM Use WHERE email=?;""",(email,))
                resutado = {"status":"success",
                        "msg":cursor.fetchall()[0][0]}
            else:
                resutado = {"status":"error",
                        "msg":'Senha'}
        else:
            resutado = {"status":"error",
                        "msg":'email'}
    return resutado
        
def getpedido(telefone):
    cursor.execute("""SELECT * FROM Pedidos WHERE telefone=?;""",(telefone,))
    resp=cursor.fetchall()
    lista=[]
    for valor in range(0,len(resp)):
        lista.append({'id':resp[valor][0],'numeros':resp[valor][2]})
    
    return {"status":"success","msg":lista} 

def setUserCreate(email,senha,nome,telefone,pix):
    import hashlib
    senha = hashlib.sha256(senha.encode('utf-8')).hexdigest()
    cursor.execute("""INSERT INTO Use(email,senha,telefone,nome,chave_pix) VALUES (?,?,?,?,?)""",(email,senha,telefone,nome,pix))
    conn.commit()
    return 'Dados inseridos com sucesso.'

def getId(id:int):
    cursor.execute("""SELECT * FROM Use WHERE id=?;""",(id,))
    resp=cursor.fetchall()
    if resp != []:
        return True
    else:
        return False  

def alterando_type_user(id:int,tipo:int):
        if getId(id):
            match tipo:
                case 0:
                    cursor.execute("""UPDATE Use SET tipo_user = ? WHERE id = ? """, (0, id,))
                    conn.commit()
                    
                    return 'UPDATE use 0'
                case 1:
                    cursor.execute("""UPDATE Use SET tipo_user = ? WHERE id = ? """, (1, id,))
                    conn.commit()
                    
                    return 'UPDATE use 1'
                case _:
                    return "Tipo user inválido"
        else:
            return 'Erro user inválido' 

def setEvento(user_id:int,nome_parque:str,valor_senha:float,data:str,quantidade_senha:int):
    cursor.execute("""SELECT tipo_user FROM Use WHERE id=?;""",(user_id,))
    resp=cursor.fetchall()
    if resp != []:
        if resp[0][0] == 1:
            cursor.execute("""INSERT INTO Evento (Nome_parque, Quantidade_senahs, id_user, Valor_senha, date_evento)VALUES (?,?,?,?,?)
            """, (nome_parque,quantidade_senha,user_id,valor_senha,data))
            conn.commit()
            
            return 'Dados inseridos com sucesso.'
        else:
            return 'Voce não tem permissão para isso :/'
    else:
        return 'ID de usuário não existe' 

def setPedidoDB(id_evento:int,telefone,puxador,esteira,representacao,numeros):
    from datetime import datetime
    date = f'{datetime.now().year}-{datetime.now().month}-{datetime.now().day}'
    numeros_r=[]
    total=0
    lista = numeros.split(',')
    try:
        for dado in lista:
            cursor.execute("""SELECT * FROM numeros WHERE numero=?;""",(dado,))
            resp=cursor.fetchall()
            if resp != []:
                numeros_r.append(resp[0][2])
            else:
                total+=1  
        if total == len(lista):
            #ADD dados
        #-------------------------------------------
            cursor.execute(""" INSERT INTO Pedidos(id_evento,telefone, puxador,esteira,representacao, criado_em,numeros)VALUES (?,?,?,?,?,?,?)
            """, (id_evento,telefone,puxador,esteira,representacao,date,numeros))
            conn.commit()
            #--------------------------------------------
            cursor.execute(""" SELECT * FROM Pedidos;""")
            t = len(cursor.fetchall())
            #--------------------------------------------
            for dado in lista:
                cursor.execute("""INSERT INTO numeros(id_pedido,numero)VALUES (?,?)""", (t,dado))
                conn.commit()
            
            return {"status":"success",
                    "msg":'add dados'}
        else:
            return {"status":"error",
                    "msg":numeros_r} 
            #('erro',numeros_r)
    except:
            
            return {"status":"error",
                    "msg":"add"} 
       

def pedidos_type(id:int,tipo:str):
            match tipo:
                case 'cancelar':
                    cursor.execute("""UPDATE Pedidos SET status = ? WHERE id = ? """, (2,id,))
                    conn.commit()
                    cursor.execute("""DELETE FROM numeros WHERE id_pedido = ? """, (id,))
                    conn.commit()
                    
                    return 'Pedidos cancelador'
                case 'pagar':
                    cursor.execute("""UPDATE Pedidos SET status = ? WHERE id = ? """, (1,id,))
                    conn.commit()
                  
                    return 'Pedidos pagor'
                case _:
                    return "Tipo operação inválido"
    
#pedidos_type(1,'cancelar')
