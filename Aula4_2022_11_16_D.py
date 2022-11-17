import Aula4_2022_11_16_C as bd

con, cur = bd.conectar()

nome = input("Informe o nome do Herói/Vilão: ")
nome_civil = input("Informe o nome civil do Herói/Vilão: ")
tipo_numerico = input("Tecle 1 para Herói ou 2 para Vilão: ")

#consulta a tabela grupos e exibe a tabela 


#Consulta para o valor maximo usado no banco
sql = "SELECT MAX(pessoa_id)+1 FROM pessoas"
cur.execute(sql)
pessoa_id = cur.fetchone()[0]

if tipo_numerico == "1":
  tipo = "Herói(na)"
else:
  tipo = "Vilã(o)"

  sql = f"INSERT INTO pessoas (pessoa_id, nome, nome_civil, tipo) VALUES ({pessoa_id}, '{nome}', '{nome_civil}', '{tipo}')"

  #insert pessoas_grupo
  #insert into pessoas_grupo(pessoa_id, grupo_id,) VALUES(x,x)

  cur.execute(sql)
  con.commit()
  con.close()











