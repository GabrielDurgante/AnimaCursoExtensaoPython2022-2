# comando input(), permitir que o usuario digite algo

nome = input("Digite seu nome: ")
idade = int (input("Digite sua idade: "))
dobro = idade * 2

print(f"\nSeu nome é {nome} e sua idade é {idade} anos")     
print(f"O dobro da sua idade é {dobro} \n")

#Estrutura condicional - if
#se a pessoa for maior de idade, mostre "Voce é maior de idade", se for menor de idade, mostre "Voce é menor de idade"

if idade >= 18:
  print(f"Voce tem {idade}, logo, é maior de idade e pode beber e dirigir")
  
else:
  print(f"Voce tem {idade}, logo, é menor de idade e vai ficar só assistindo")

