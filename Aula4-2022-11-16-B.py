# passo 1 - Importar a biblioteca SQLite3
import sqlite3

# passo 2 - estabelecer uma conexão com o banco de dados 
conexao = sqlite3.connect("dc_universe.db")

# passo 3 - criar um objeto do tipo cursor 
cursor = conexao.cursor()

# passo 4 - inserir um herói/vilão
sql = "INSERT INTO pessoas (pessoa_id, nome, nome_civil, tipo) VALUES (12, 'The Flash', 'Barry Allen', 'Herói()na')"

# passo 5 - Executar o comando SQL
cursor.execute(sql)
