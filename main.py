# Pedir a nota (0 a 10) e informar se o aluno passou ou não

nota1 = float(input("Informe a nota da sua avaliação a1 (0-10): "))
nota2 = float(input("Informe a nota da sua avaliação a2 (0-10): "))
nota3 = float(input("Informe a nota da sua avaliação a3 (0-10): "))

soma_total = round((nota1 + nota2 + nota3) / 3 , 2)

print(f"Sua nota total foi {soma_total}")

if soma_total >= 7 and soma_total <=10:
  print("parabens, voce passou!!")
  
elif soma_total < 7 and soma_total >= 0:
  print("Puts, voce reprovou!")

else:
  print("voce digitou alguma nota fora do padrão")
