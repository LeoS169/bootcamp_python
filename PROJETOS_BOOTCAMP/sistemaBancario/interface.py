from os import system
from sistemaBacarioV3 import (criar_PessoaFisica, 
criar_Conta, fazer_saque, fazer_deposito,
exibir_extrato, listar_clientes, listar_contas
)

while True:
    
    print("="*40)
    print("BEM VINDO AO BANCO DO BURACO DE LAGOA".center(40, " "))
    print("="*40, end="\n\n")
    
    print("ESCOLHA UMA AÇÃO:".center(40, " "))
    print("""
        0 - SAIR (Pressione 0)
        1 - CADASTRAR CLIENTE (Pressione 1)  
        2 - CADASTRAR CONTA CORRENTE (Pressione 2)     
        3 - DEPOSITAR (Pressione 3)
        4 - SACAR (Pressione 4)
        5 - VISUALIZAR EXTRATO (Pressione 5)
        6 - LISTAR CONTAS (Pessione 6)
        7 - LISTAR CLIENTES (Pressione 7)        
        """)
    
    acao = input("> ")
    system("cls")
    print()
    
    if acao == "0":
        print("VOCÊ SAIU!".center(40, " "))
        break
    
    elif acao == "1":
        print("CADASTRO DE CLIENTE".center(40, " "), end="\n\n")
        nome = input("Nome: ")
        cpf = int(input("CPF: "))
        
        print("DATA DE NASCIMENTO: ".center(40, " "))
        dia = int(input("Dia: "))
        mes = int(input("Mês: "))
        ano = int(input("Ano: "))
        
        print("ENDERECO: ".center(40, " "))
        rua = input("Rua: ")
        bairro = input("Bairro: ")
        cidade = input("Cidade: ")
        uf = input("UF: ")
        endereco = f"{rua}, {bairro}. {cidade}/{uf}"        
        
        status = criar_PessoaFisica(endereco, nome, cpf, dia, mes, ano)
        print(status)
        
    elif acao == "2":
        print("CRIAÇÃO DE CONTA".center(40, " "), end="\n\n")
        numero_conta = int(input("Número da conta: "))
        cpf = int(input("CPF do titular: "))
        
        status = criar_Conta(numero_conta, cpf)
        print(status)
        
    elif acao == "3":
        print("DEPÓSITO".center(40, " "), end="\n\n")
        cpf = int(input("CPF do titular: "))
        numero_conta = int(input("Número da conta: "))
        valor = float(input("Valor do depósito: "))
        
        status = fazer_deposito(cpf, numero_conta, valor)
        print(status)
        
    
    elif acao == "4":
        print("SAQUE".center(40, " "), end="\n\n")
        cpf = int(input("CPF do titular: "))
        numero_conta = int(input("Número da conta: "))
        valor = float(input("Valor do saque: "))
        
        status = fazer_saque(cpf, numero_conta, valor)
        print(status)
    
    elif acao == "5":
        print("EXTRATO DA CONTA".center(40, " "))        
        numero_conta = int(input("Número da conta: "))
        
        status = exibir_extrato(numero_conta)
        print(status)
        
    
    elif acao == "6":
        print("LISTAGEM DE CONTAS".center(40, " "))
        listar_contas()

        
    elif acao == "7":
        print("LISTAGEM DE CLIENTES:".center(40, " "))
        listar_clientes()
        