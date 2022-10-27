# comando input(), permitir que o usuario digite algo

nome = input("Digite seu nome: ")
idade = int (input("Digite sua idade: "))
dobro = idade * 2
genero = input("Voce é do genero masculino ou feminino (M ou F): ")

print(f"\nSeu nome é {nome} e sua idade é {idade} anos")     
print(f"O dobro da sua idade é {dobro} \n")

#Estrutura condicional - if e else
#se a pessoa for maior de idade, mostre "Voce é maior de idade", se for menor de idade, mostre "Voce é menor de idade"

if idade >= 18 and genero == "M" or genero == "m":
  print(f"Voce tem {idade} anos, logo, é homem maior de idade e precisa/precisou participar do serviço militar.")
  
elif idade >= 18 and genero == "F" or genero == "f":
  print(f"Voce tem {idade} anos, logo, é mulher maior de idade e não precisa participar do serviço militar")

elif idade < 18 and genero == "M" or genero == "m":
  print(f"Voce tem {idade} anos, logo, é homem menor de idade e vai precisar fazer o alistamento no futuro")

elif idade < 18 and genero == "F" or genero == "f":
  print(f"Voce tem {idade} anos, logo, é mulher menor de idade e não vai precisar fazer o alistamento no futuro")

  

