# passo 1 - Importar a biblioteca SQLite3
import sqlite3

#Passos 2 e 3 virarão função conectar()
def conectar():
  conexao = sqlite3.connect("dc_universe.db")
  cursor = conexao.cursor()

  return conexao, cursor


