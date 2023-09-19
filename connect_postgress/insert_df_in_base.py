import pandas as pd
import psycopg2
from sqlalchemy import create_engine

# Supondo que você já tem um DataFrame chamado 'df' com seus dados

# Configurações de conexão com o PostgreSQL
db_config = {
    'user': 'seu_usuario',
    'password': 'sua_senha',
    'host': 'localhost',
    'port': '5432',  # Porta padrão do PostgreSQL
    'database': 'sua_base_de_dados'
}

# Criar uma conexão com o PostgreSQL
conn = psycopg2.connect(**db_config)

# Crie um mecanismo SQLAlchemy para que você possa usar a função to_sql()
engine = create_engine(f'postgresql+psycopg2://{db_config["user"]}:{db_config["password"]}@{db_config["host"]}:{db_config["port"]}/{db_config["database"]}')

# Substitua 'sua_tabela' pelo nome da tabela em que você deseja inserir os dados
nome_da_tabela = 'sua_tabela'

# Use a função to_sql() para inserir dados no PostgreSQL
df.to_sql(nome_da_tabela, engine, if_exists='replace', index=False)

# Feche a conexão com o PostgreSQL
conn.close()
