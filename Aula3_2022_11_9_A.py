# laços - while 

contador = 1

while (contador <= 10):
  print(f"{contador}")
  contador = contador + 1

#Lista 
frutas = ["morango", "laranja", "pêra"]
print(frutas)
print("\n")
print(frutas[0])
print(frutas[1])
print(frutas[2])
print("\n")


#adcionar nova fruta
frutas.append("manga")
print("\n")

#exibir quantas frutas tem na lista
print(len(frutas))
print("\n")

#contador de frutas 
contador = 0
while (contador <= 3):
  print(frutas[contador])
  contador = contador + 1 
