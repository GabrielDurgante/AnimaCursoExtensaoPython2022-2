# passo 1 - Importar a biblioteca SQLite3
import sqlite3

# passo 2 - estabelecer uma conexão com o banco de dados 
conexao = sqlite3.connect("dc_universe.db")

# passo 3 - criar um objeto do tipo cursor 
cursor = conexao.cursor()

# passo 4 - comando SQL do banco
sql = "SELECT pessoa_id, nome, nome_civil, tipo FROM pessoas"

# passo 5 - Executar o comando SQL no SQLite (cursor)
cursor.execute(sql)

# passo 6 - Exibir a consulta com todos os nomes de heróis e vilões do banco de dados
pessoas = cursor.fetchall()
for pessoa in pessoas:
  print(pessoa)
  print("\n")

for pessoa in pessoas:
  print(f"Personagem: {pessoa[1]} Identidade: ({pessoa[2]}) \n")

for pessoa in pessoas:
  print(f"Personagem: {pessoa[1]} Profissão: ({pessoa[3]}) \n")
  
