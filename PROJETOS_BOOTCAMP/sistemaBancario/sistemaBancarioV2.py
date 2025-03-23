from datetime import datetime
from os import system

"""
Este script é um sistema bancário simples escrito em Python. 
Ele permite ao usuário realizar operações básicas como depositar dinheiro, 
sacar dinheiro e visualizar o extrato da conta.

Esse script foi feito com base no projeto do BootCamp da Suzano/DIO.
"""

saldo = 0
extrato = []
usuarios = {}
contas = {}
num_conta = 1

LIMITE_SAQUE = 500
quantidade_saques = 3


def depositar(valor:float):
    """Função para depositar

    Args:
        valor (float): valor para deposito

    Returns:
        string: status para exibição
        
    Atividade:
        faz o append de informações no extrato
    """
    global saldo, extrato
    if (valor <= 0):
        return "Digite um valor VÁLIDO"
    else:
        saldo += valor
        extrato.append(f"DEPOSITO: R${valor:.2f} | Data/Hora: {datetime.now()}")
        return "Depósito efetuado com SUCESSO!"

    
def sacar(valor:float):
    """ Função para sacar

    Args:
        valor (float): valor para saque

    Returns:
        string: status para exibição
        
    Atividade:
        faz o append de informações no extrato
    """
    global saldo, quantidade_saques, extrato
    if quantidade_saques != 0:
        if valor <= 0:
            return "Digite um valor VÁLIDO"
        elif valor > saldo:
            extrato.append(f"TENTATIVA DE SAQUE de R${valor:.2f}: Saldo de insuficiênte! | Data/Hora: {datetime.now()}.")
            return f"Saldo INSUFICIÊNTE! Saldo: R${saldo:.2f}"
        else:
            if valor > 500:
                return "OS SAQUES TÊM UM LIMITE DE R$500.00!"
            else:
                saldo -= valor
                quantidade_saques -= 1
                extrato.append(f"SAQUE: R${valor:.2f} | Data/Hora: {datetime.now()}")
                return "Saque efetuado com SUCESSO!"                
    else:
        return "VOCÊ TEM UM LIMITE DE 3 SAQUES DIÁRIOS!"            


def mostra_extrato():
    """ Função para mostrar extrato
    
    Atividade: 
        percorre lista de extrato exibindo-os
        mostra informações sobre conta
    """
    global extrato, saldo, quantidade_saques
    if extrato:
        for info in extrato:
            print(info, end="\n")        
        else:
            print(f"""
                INFOS DA CONTA -> 
                
                SALDO: R${saldo:.2f} 
                SAQUES DISPONÍVEIS: {quantidade_saques}
                DATA/HORA: {datetime.now()} 
                
                """)
    else:
        print("Nenhuma ação realizada na conta!")
    return ''


def cadastrar_user(
    nome:str,
    data_nascimento:datetime,
    cpf:int,
    endereco:str
):
    global usuarios
    cpf_cadastrados = usuarios.keys()
    if cpf_cadastrados:
        for cpf_cad in cpf_cadastrados:
            if int(cpf_cad) == cpf:
                return f"CPF {cpf} JÁ CADASTRADO!"
            else:
                usuarios[f"{cpf}"] = {
                    "nome": nome,
                    "data_nasc": data_nascimento,
                    "endereco": endereco
                }
                return "CADASTRADO"
    else:
        usuarios[f"{cpf}"] = {
            "nome": nome,
            "data_nasc": data_nascimento,
            "endereco": endereco
        }
        return "CADASTRADO"


def cad_conta_corrente(
    cpf_usuario:int
):
    global usuarios, contas, num_conta
    cpf_cadastrados = usuarios.keys()
    if cpf_cadastrados:
        for cpf_cad in cpf_cadastrados:
            if int(cpf_cad) == cpf_usuario:
                contas[f"{cpf_usuario}"] = {
                    "agencia": "0001",
                    "num_conta": num_conta
                }
                num_conta += 1    
                return (
                    "CONTA CADASTRADA!\n".center(40, " "),
                    f"""
                    INFORMAÇÕES DA CONTA
                    
                    CPF: {cpf_usuario},
                    NOME: {usuarios[f"{cpf_usuario}"]["nome"]}
                    ENDERECO: {usuarios[f"{cpf_usuario}"]["endereco"]}
                    AGÊNCIA: 0001
                    N° DA CONTA: {num_conta - 1}                  
                    """
                )            
            else:
                continue
        else:
            return f"USUÁRIO COM CPF {cpf_usuario} NÃO CADASTRADO", ""
    else:
        return "ERRO: NENHUM USUÁRIO CADASTRADO!", ""
    
def listar_contas():
    global contas, usuarios
    if contas:
        chaves_conta = contas.keys()
        for cpf in chaves_conta:
            print(f"CONTA DO CPF: {cpf}".center(40, " "))
            print(f"""
                  INFORMAÇÕES
                  
                  TITULAR: {usuarios[f"{cpf}"]["nome"]}
                  ENDEREÇO: {usuarios[f"{cpf}"]["endereco"]}
                  AGÊNCIA: 0001
                  N° DA CONTA: {contas[f"{cpf}"]["num_conta"]}
                  
                  """, end="\n\n")
    else:
        print("NÃO EXISTEM CONTAS CADASTRADAS!", end="\n\n")
    return ''
    
                        


while True:
    
    print("="*40)
    print("BEM VINDO AO BANCO DO BURACO DE LAGOA".center(40, " "))
    print("="*40, end="\n\n")
    
    print("ESCOLHA UMA AÇÃO:".center(40, " "))
    print("""
        0 - SAIR (Pressione 0)
        1 - DEPOSITAR (Pressione 1)
        2 - SACAR (Pressione 2)
        3 - VISUALIZAR EXTRATO (Pressione 3)
        4 - CADASTRAR USUÁRIO (Pressione 4)  
        5 - CADASTRAR CONTA CORRENTE (Pressione 5)     
        6 - LISTAR CONTAS (Pessione 6)          
        """)
    
    acao = input("> ")
    system("cls")
    print()
    
    if acao == "0":
        print("VOCÊ SAIU!".center(40, " "))
        break
    elif acao == "1":
        print("DEPÓSITO".center(40, " "), end="\n\n")
        valor = float(input("Digite um valor: "))
        ret_depositar = depositar(valor=valor)
        print(ret_depositar.center(40, " "), end="\n\n")
    elif acao == "2":
        print("SAQUE".center(40, " "), end="\n\n")
        valor = float(input("Digite um valor: "))
        ret_saque = sacar(valor=valor)
        print(ret_saque.center(40, " "), end="\n\n")
    elif acao == "3":
        print("EXTRATO BANCÁRIO".center(40, " "), "\n\n")
        mostra_extrato()
    elif acao == "4":
        print("CADASTRO DE USUÁRIO".center(40, " "), end="\n\n")
        nome = input("Nome do usuário: ")
        cpf = int(input("CPF: "))
        
        print("DATA DE NASCIMENTO:".center(40, " "))
        dia = int(input("Dia: "))
        mes = int(input("Mês: "))
        ano = int(input("Ano: "))
        
        print("ENDEREÇO:".center(40, " "))
        rua = input("Logradouro: ")
        bairro = input("Bairro: ")
        cidade = input("Cidade: ")
        estado = input("UF: ")
        endereco = f"{rua} - {bairro} - {cidade}/{estado}"
        
        status = cadastrar_user(
            nome=nome,
            cpf=cpf,
            data_nascimento=datetime(ano, mes, dia),
            endereco=endereco
        )
        print(status, end="\n\n")
    elif acao == "5":
        print("CADASTRO DA CONTA:".center(40," "), end="\n\n")
        cpf_usuario = int(input("CPF do usuário: "))
        status_a, status_b = cad_conta_corrente(cpf_usuario=cpf_usuario)
        print(status_a, status_b)
    elif acao == "6":
        listar_contas()
        

