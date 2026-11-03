#Solicite o valor da hora de trabalho do funcionário e a quantidade de horas extras trabalhadas

hora = float(input("Qual é o valor de sua hora de trabalho?: "))
dia = float(input("Quantas horas você trabalha por dia?: "))
horas_extras = float(input("Quantas horas extras você trabalhou?: "))

#Calcule e exiba o valor total a ser pago (sem acréscimos percentuais neste momento).

horas = dia * hora * 15 + horas_extras * hora
print(f" ---Você recebe um valor de R$ {horas}.---")