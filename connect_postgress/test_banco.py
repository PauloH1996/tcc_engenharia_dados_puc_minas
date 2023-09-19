import psycopg2

# Informações de conexão com o banco de dados
conexao_info = {
    "dbname": "postgres",
    "user": "postgres",
    "password": "tcc123",
    "host": "localhost",
    "port": "5432",  # Porta padrão do PostgreSQL
}

# Comando SQL para criar a tabela
comando_sql = """
CREATE TABLE IF NOT EXISTS nome_da_tabela (
    id SERIAL PRIMARY KEY,
    nome TEXT NOT NULL,
    idade INTEGER NOT NULL
);
"""

try:
    # Conecta ao banco de dados
    conexao = psycopg2.connect(**conexao_info)

    # Cria um cursor para executar comandos SQL
    cursor = conexao.cursor()

    # Executa o comando SQL para criar a tabela
    cursor.execute(comando_sql)

    # Confirma a transação
    conexao.commit()

    print("Tabela criada com sucesso!")

except psycopg2.Error as e:
    print("Erro ao criar a tabela:", e)

finally:
    # Fecha o cursor e a conexão
    if cursor:
        cursor.close()
    if conexao:
        conexao.close()
