# Bibliotecas
import os # Para limpar o terminal
from time import sleep # Para aguardar determinado tempo entre operaçoes visuais

# Matriz com os produtos e seus preços
produtos = [
    ["COCA - COLA", 3.75],
    ["PEPSI", 3.67],
    ["MONSTER", 9.96],
    ["CAFÉ", 1.25],
    ["REDBULL", 13.99]
]

# Lista com as quantidades de cada produto disponíveis
quantidades = [2, 5, 1, 100, 2]

# Credenciais do modo administrador
admin_username = "admin"
admin_password = "123"

# Estoques de notas e moedas
estoque_notas_moedas = {
    10000: 10,
    5000: 10,
    2000: 10,
    1000: 10,
    500: 10,
    200: 10,
    100: 10,
    50: 10,
    25: 10,
    10: 10,
    5: 10,
    1: 10
}

# Função para exibir o menu de produtos
def exibir_menu():
    print("MAQUINA DE REFRIGERANTES")
    for i in range(len(produtos)): # Percorre a lista de produtos
        print(f"({i+1}) {produtos[i][0]} ---------- R${produtos[i][1]:.2f} - Estoque: {quantidades[i]} unidade(s)")# Apresenta os produtos, quantidade e precos

# Função para calcular e dar o troco
def calcular_troco(valor_troco):

    troco = round(valor_troco * 100, 2)  # Converte o troco de reais para centavos
    notas_moedas_dadas = []  # Lista para armazenar as notas e moedas dadas

    for nota_moeda, estoque in estoque_notas_moedas.items(): # Percorre o estoque de notas e moedas

        troco = int(troco) # Converte o troco para inteiro
        quantidade_notas_moedas = min(estoque, troco // nota_moeda) # Calcula a quantidade de notas/moedas que pode ser dada

        if quantidade_notas_moedas > 0: # Verifica se a quantidade de notas/moedas pode ser dada

            estoque_notas_moedas[nota_moeda] -= quantidade_notas_moedas # Remove a quantidade de notas/moedas do estoque
            notas_moedas_dadas.append([nota_moeda, quantidade_notas_moedas]) # Adiciona a quantidade de notas/moedas dadas a lista
            troco -= quantidade_notas_moedas * nota_moeda # Subtrai a quantidade de notas/moedas dadas do troco

    if troco == 0: # Verifica se o troco foi dada com sucesso

        print("Troco dado com sucesso:")

        for nota_moeda, quantia in notas_moedas_dadas: # Percorre a lista de notas e moedas dadas
            print(f"{int(quantia)} notas/moedas de R${(nota_moeda / 100):.2f}") # Apresenta a quantidade de notas/moedas dadas em reais e centavos

    else: # Caso o troco não tenha sido dada
        print("Não é possível dar o troco devido à falta de notas/moedas disponíveis.")
        print("Transação cancelada.")
        return False # Retorna falso

    return True # Retorna verdadeiro caso o troco tenha sido dado com sucesso

# Função para realizar a venda do produto escolhido
def realizar_venda(escolha_produto):

    produto = produtos[escolha_produto-1] # Seleciona o produto escolhido
    quantidade = quantidades[escolha_produto-1] # Seleciona a quantidade do produto escolhido
    
    if quantidade < 1: # Verifica se a quantidade do produto escolhido esta disponível (caso não esteja)
        print("ESTOQUE INSUFICIENTE")
        print("Escolha outra Bebida")
        return # Retorna para o menu
    
    valor_pagamento = float(input(f"Pagamento para {produtos[escolha_produto-1][0]}: R$")) # Recebe o valor de pagamento do usuário

    if valor_pagamento < produto[1]: # Verifica se o valor de pagamento é menor que o preço do produto

        print("Valor insuficiente")
        return # Retorna para o menu caso o valor de pagamento seja insuficiente
    
    troco = valor_pagamento - produto[1] # Calcula o troco
    print(f"TROCO = R$ {troco:.2f}") # Apresenta o troco

    if calcular_troco(troco): # Chama a função para dar o troco em notas e moedas

        quantidades[escolha_produto-1] -= 1 # Remove uma unidadedo produto escolhido do estoque
        print("Restam", quantidades[escolha_produto-1], "Unidades de ", produtos[escolha_produto-1][0]) # Apresenta o estoque restante

# Função para o modo administrador
def modo_administrador():
    # Credenciais do administrador
    username = input("Digite o nome de usuário: ")
    password = input("Digite a senha: ")

    if username == admin_username and password == admin_password: # Verifica se as credenciais do administrador sao corretas

        while True: # Loop principal do modo administrador
            os.system("cls")
            print("Modo Administrador:")
            print("(1) Adicionar Produto")
            print("(2) Remover Produto")
            print("(3) Editar Produto")
            print("(4) Editar Estoque de Notas/Moedas")
            print("(5) Voltar ao Menu Principal")
            escolha_admin = int(input("Escolha a opção desejada: ")) # Recebe a opção do modo administrador

            if escolha_admin == 1: # Opção para adicionar um novo produto

                os.system("cls") # Limpa o terminal

                # Dados do novo produto
                nome_produto = input("Digite o nome do novo produto: ")
                preco_produto = float(input("Digite o preço do novo produto: "))
                estoque_produto = int(input("Digite a quantidade em estoque: "))

                produtos.append([nome_produto, preco_produto]) # Adiciona o novo produto na lista de produtos e preços
                quantidades.append(estoque_produto) # Adiciona a quantidade do novo produto na lista de quantidades
                print("Produto adicionado com sucesso!")

            elif escolha_admin == 2: # Opção para remover um produto

                os.system("cls") # Limpa o terminal

                exibir_menu() # Exibe a lista de produtos

                produto_remover = int(input("Digite o número do produto a ser removido: ")) # Recebe a opção do produto a ser removido

                if 1 <= produto_remover <= len(produtos): # Verifica se o produto escolhido existe

                    del produtos[produto_remover - 1] # Remove o produto da lista de produtos e preços
                    del quantidades[produto_remover - 1] # Remove a quantidade do produto da lista de quantidades
                    print("Produto removido com sucesso!")
                else: # Caso o produto escolhido não exista
                    print("Número de produto inválido!")

            elif escolha_admin == 3: # Opção para editar um produto

                os.system("cls") # Limpa o terminal

                exibir_menu() # Exibe a lista de produtos

                produto_editar = int(input("Digite o número do produto a ser editado: ")) # Recebe a opção do produto a ser editado

                if 1 <= produto_editar <= len(produtos): # Verifica se o produto escolhido existe

                    #  Novos dados do novo produto escolhido
                    novo_nome = input("Digite o novo nome do produto: ")
                    novo_preco = float(input("Digite o novo preço do produto: "))
                    novo_estoque = int(input("Digite a nova quantidade em estoque: "))

                    produtos[produto_editar - 1] = [novo_nome, novo_preco] # Edita o nome e o preço do produto
                    quantidades[produto_editar - 1] = novo_estoque # Edita a quantidade em estoque do produto
                    print("Produto editado com sucesso!")
                else: # Caso o produto escolhido não exista
                    print("Número de produto inválido!")

            elif escolha_admin == 4: # Opção para editar o estoque de notas e moedas

                os.system("cls") # Limpa o terminal

                print("Editar Estoque de Notas/Moedas:")
                for nota_moeda, estoque in estoque_notas_moedas.items(): # Percorre o estoque de notas e moedas
                    novo_estoque = int(input(f"Digite o novo estoque para R${nota_moeda/100:.2f}: ")) # Recebe o novo estoque
                    estoque_notas_moedas[nota_moeda] = novo_estoque # Edita o estoque de notas e moedas
                print("Estoque de Notas/Moedas editado com sucesso!")

            elif escolha_admin == 5: # Opção para voltar ao menu principal
                break

            input("Pressione Enter para continuar...")

    else: # Credenciais inválidas
        print("Credenciais inválidas. Acesso negado.")
        sleep(1)

# Maquina de Bebidas
while True: # Loop principal para a execução da máquina

    os.system("cls") # Limpa o terminal

    # Tela inicial
    print("Bem-vindo à Máquina de Bebidas!")
    print("(1) Modo Cliente")
    print("(2) Modo Administrador")
    print("(3) Sair")
    escolha_modo = int(input("Escolha o modo desejado: ")) # Recebe a opção do modo
    
    if escolha_modo == 1: # Opção para o modo cliente

        os.system("cls") # Limpa o terminal

        exibir_menu() # Exibe a lista de produtos
        escolha_produto = int(input("ESCOLHA O NÚMERO DO PRODUTO DESEJADO: ")) # Recebe a opção do produto desejado do usuario
    
        if escolha_produto < 1 or escolha_produto > len(produtos): # Verifica se o produto escolhido existe

            os.system("cls") # Limpa o terminal

            print(f"O produto {escolha_produto} é inválido") # Apresenta uma mensagem de erro caso o produto escolhido seja inválido
            continue # Retorna para o loop principal
    
        realizar_venda(escolha_produto) # Chama a função para realizar a venda do produto escolhido pelo usuario
    
        repetir = input("Calcular novamente? (s/n): ") # Recebe se o usuário deseja realizar uma nova compra

        # Verifica se o usuário deseja realizar uma nova compra
        if repetir != "s": # Caso o usuário não deseje realizar uma nova compra
            break # Encerra o programa

    elif escolha_modo == 2: # Opção para o modo administrador

        os.system("cls") # Limpa o terminal

        modo_administrador() # Chama a função para o modo administrador

    elif escolha_modo == 3: # Opção para sair
        break # Encerra o programa
