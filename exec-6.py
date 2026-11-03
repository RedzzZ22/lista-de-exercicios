#solicite o status da credencial ("ativa" ou "bloqueada"). Se for ativa, exiba "Acesso Liberado". Caso contrário, exiba "Acesso Negado: Procure a portaria".
while True:
    status = input("Qual o status do seu credencial: ").strip().lower()

    if status == "ativa":
        print("Bem vindo")
        break
    elif status == "bloqueada":
        print("Acesso negado")
        break
    else:
        print("Coloque CORRETAMENTE")