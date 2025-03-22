from datetime import datetime
from os import system

saldo = 0
extrato = []

LIMITE_SAQUE = 500
quantidade_saques = 3


def depositar(valor:float):
    global saldo, extrato
    if (valor <= 0):
        return "Digite um valor VÁLIDO"
    else:
        saldo += valor
        extrato.append(f"DEPOSITO: R${valor:.2f} | Data/Hora: {datetime.now()}")
        return "Depósito efetuado com SUCESSO!"

    
def saque(valor:float):
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
        ret_saque = saque(valor=valor)
        print(ret_saque.center(40, " "), end="\n\n")
    elif acao == "3":
        print("EXTRATO BANCÁRIO".center(40, " "), "\n\n")
        mostra_extrato()
        
          
    
    
