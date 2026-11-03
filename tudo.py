# Crie um programa que solicite o nome e o cargo do novo funcionário
print ("Bem vindo! precisamos de alguns dados seus para fazermos o seu cadastro")
nome = input ("Informe o seu NOME: ")
cargo = input("informe seu cargo: ")

print ("carregando")
print ("...")
print ("...")
print ("...")
print ("...")
print ("...")

#Imprima uma mensagem formatada de boas-vindas ao sistema da ArkeTech.

print ("------------------")
print (f"Bem vindo, {nome}!")
print ("------------------")

#Solicite o valor da hora de trabalho do funcionário e a quantidade de horas extras trabalhadas

hora = float(input("Qual é o valor de sua hora de trabalho?: "))
dia = float(input("Quantas horas você trabalha por dia?: "))
horas_extras = float(input("Quantas horas extras você trabalhou?: "))

#Calcule e exiba o valor total a ser pago (sem acréscimos percentuais neste momento).

horas = dia * hora * 15 + horas_extras * hora
print(f" ---Você recebe um valor de R$ {horas}.---")

#peça ao usuário para inserir os três valores de despesas. Converta-os para números decimais

print("Gastos de viajem")

transporte = float(input("Quanto foi o valor do transporte: "))
hospedagem = float(input("Quanto foi o valor da hospedagem: "))
alimentação = float(input("Quanto foi o valor da alimentação: "))

valor = transporte + alimentação + hospedagem

print ("CARREGANDO")
print ("...")
print ("...")
print ("...")

print (f"O valor total a ser rembolsado é de {valor}")

#Receba o custo de fabricação de um produto. Calcule e exiba o preço de venda considerando uma margem de lucro fixa de 35%.

nomeprod = input("Qual o nome do novo produto: ")
preço = float(input("Qual o valor do produto: "))

valorluc = preço * 0.35

print(f"você tem que ter um ganho de {valorluc} para ter lucro")

#Solicite o ano de nascimento do candidato, calcule a idade com base no ano atual e exiba True se ele tiver 24 anos ou menos, e False caso contrário.

print("----------------------------------------")
print("         Controle de acesso...          ")
print("----------------------------------------")

idade = int(input("Informe a sua idade: "))

if idade > 24:
    print("Acesso negado.")
    False
else:
    True
    print("Acesso liberado")

    #solicite o status da credencial ("ativa" ou "bloqueada"). Se for ativa, exiba "Acesso Liberado". Caso contrário, exiba "Acesso Negado: Procure a portaria".
while True:
    status = input("Qual o status do seu credencial: ").strip().lower()

    if status == "ativa":
        print("Acesso permitido, Bem vindo!")
        break
    elif status == "bloqueada":
        print("Acesso negado")
        break
    else:
        print("Coloque CORRETAMENTE")

        preço_empresa = float(input("Qual é o preço do produto que a empresa está oferecendo?: "))
if preço_empresa >= 100000:
    print("Aprovamos limite de até 20.000")
elif preço_empresa > 50000 and preço_empresa < 100000:
    print("Aprovamos limite de até 10.000")
else:
    print("Crédito reprovado, o valor do produto é muito baixo para aprovação de crédito.")


faltas = int(input("Digite o número de faltas injustificadas: "))
vendas = float(input("Digite o valor total de vendas: R$ "))
 
 
if faltas == 0 and vendas > 50000:
    print("PLR Aprovada")
else:
    print("PLR Negada")

print("----------------------------------------")
print( "               Sua região              ")
print("----------------------------------------")
 
regiao = input("Informe a sua região(S,SE,CO,NE,E): ").strip().upper()
if regiao == "S" or regiao == "SE":
    print(" Sua taxa de frete é de 15R$")
elif regiao == "NE" or regiao == "N":
    print(" Sua taxa de frete é de 35R$")
elif regiao == "CO":
    print(" Sua taxa de frete é de 25R$")

print ("======================")
print ("ESTOQUE DE PRODUTOS   ")
print ("======================")
print("")
estoque = int(input("informe a quanidade de produtos no estoque: "))
if estoque <16:
    print("COMPRA URGENTE")
if estoque >16 and estoque < 50:
    print("ESTOQUE REGULAR")
if estoque > 50:
    print("ESTOQUE CHEIO")

while True:
    matricula = input("Digite a matrícula do funcionário para bater o ponto: ").strip()
   
   
    if matricula == "0000":
        print("Sistema encerrado para manutenção.")
        break
       
   
    print(f"Ponto batido com sucesso para a matrícula: {matricula}!")
    print("-" * 30)  

funcionarios = ["ana", "lucas", "beatriz", "carlos"]
 
 
for nome in funcionarios:
   
    email = f"{nome.strip().lower()}@arketech.com"
    print(f"Funcionário(a): {nome.title()} -> E-mail: {email}")


funcionarios = ["ana", "lucas", "beatriz", "carlos"]
 
 
for nome in funcionarios:
   
    email = f"{nome.strip().lower()}@arketech.com"
    print(f"Funcionário(a): {nome.title()} -> E-mail: {email}")


senha = "Admin123"
tentativas = 1
max_tentativas = 3

while tentativas <= max_tentativas:
    print(f"Tentativas {tentativas} de {max_tentativas}")
    senha_digitada = input("Digite a sua senha: ")
    if senha_digitada == senha:
     print("Acesso liberado")
     break
    else:
     print("Senha INCORRETA")
     print("Tente novamente")
     tentativas += 1
else:
    print("Acesso bloqueado")

tri_um = input("Digite a quantidade de vendas do 1º trimestre: ")
tri_dois = input("Digite a quantidade de vendas do 2º trimestre: ")
tri_tres = input("Digite a quantidade de vendas do 3º trimestre: ")
print(f" O total dos três trimestres é: {float(tri_um) + float(tri_dois) + float(tri_tres)}")