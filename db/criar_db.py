import sqlite3

conn = sqlite3.connect(r'/Users/marceloalves/Documents/Developer/Projetos/projeto_vaquejada/dados.db')
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE Use(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    email VARCHAR(255) NOT NULL,
    senha VARCHAR(255) NOT NULL,
    telefone VARCHAR(20) NOT NULL,
    nome VACHAR(255),
    tipo_user INTEGER CHECK(tipo_user IN (0,1,2)) DEFAULT 0 ,
    chave_pix VARCHAR(255)
);
""")

cursor.execute("""
CREATE TABLE Evento (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        Nome_parque VARCHAR(255) NOT NULL,
        Quantidade_senahs INT NOT NULL,
        id_user INT NOT NULL,
        Valor_senha REAL NOT NULL,
        date_evento DATE NOT NULL,
        status INTEGER CHECK(status IN (0,1,2)) DEFAULT 0,
        FOREIGN KEY(id_user) REFERENCES User(id)
);
""")

cursor.execute("""
CREATE TABLE Pedidos (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        id_evento INT NOT NULL,
        numeros TEX NOT NULL,
        telefone VARCHAR(255) NOT NULL,
        puxador VARCHAR(255) NOT NULL,
        esteira VARCHAR(255) NOT NULL,
        representacao VARCHAR(255) NOT NULL,
        criado_em DATE NOT NULL ,
        status INTEGER CHECK(status IN (0,1,2)) DEFAULT 0,       
        FOREIGN KEY(id_evento) REFERENCES Evento(id)
);
""")

cursor.execute("""
CREATE TABLE numeros (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        id_pedido INT NOT NULL,
        numero INTEGER NOT NULL,
        FOREIGN KEY(id_pedido) REFERENCES Pedidos(id)
);
""")


print('Tabela criada com sucesso.')
# desconectando...
conn.close()