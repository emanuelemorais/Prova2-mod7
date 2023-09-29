import psycopg2

# Constantes
DB_USER = "admin123"
DB_PASSWORD = "admin123"
DB_HOST = "flai.crwpblenphuv.us-east-1.rds.amazonaws.com"
DB_PORT = "5432"
DB_NAME = "flai"

# Conexão com o banco
con = psycopg2.connect(
    database= DB_NAME,
    user= DB_USER,
    password= DB_PASSWORD,
    host= DB_HOST,
    port= DB_PORT
)

# Criação do cursor
cur = con.cursor()

print("teste")
# Roda o comando SQL
cur.execute(
    """DROP TABLE IF EXISTS minhas_notas ;

    CREATE TABLE minhas_notas (
        id SERIAL PRIMARY KEY,
        titulo VARCHAR(255) NOT NULL,
        descricao TEXT NOT null,
        data_criacao TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
    );"""
)

print("ok")
# Fecha a conexão
con.close()
    
