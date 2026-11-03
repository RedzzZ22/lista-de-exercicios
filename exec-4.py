#Receba o custo de fabricação de um produto. Calcule e exiba o preço de venda considerando uma margem de lucro fixa de 35%.

nomeprod = input("Qual o nome do novo produto: ")
preço = float(input("Qual o valor do produto: "))

valorluc = preço * 0.35

print(f"você tem que ter um ganho de {valorluc} para ter lucro")