from abc import ABC, abstractmethod
from datetime import date, datetime

contas = []
clientes = []

class Transacao(ABC):

    @property
    @abstractmethod
    def valor(self):
        pass


    @abstractmethod
    def registrar(self, conta):
        pass


class Deposito(Transacao):
    def __init__(self, valor, conta):
        super().__init__()
        self._valor = valor
        self.conta = conta
        
    
    @property
    def valor(self):
        return self._valor
    
    
    def registrar(self, conta):
        conta.historico.adicionar_transacao(self)
    

class Saque(Transacao):
    def __init__(self, valor, conta):
        super().__init__()   
        self._valor = valor
        self.conta = conta
        
    
    @property
    def valor(self):
        if self._valor >= 0 and self._valor <= self.conta.limite:
            return self._valor
        else:
            return None
        
    
    def registrar(self, conta):
        conta.historico.adicionar_transacao(self)
        

class Historico:
    def __init__(self):
        self._transacoes = []
        
    
    @property
    def transacoes(self):
        return self._transacoes
    
    
    def adicionar_transacao(self, transacao:Transacao):
        self._transacoes.append(
            {
                "Tipo": transacao.__class__.__name__,
                "Titular": transacao.conta.cliente.nome,
                "CPF": transacao.conta.cliente.cpf,
                "Valor": f"R$ {transacao.valor}",
                "Data": date.today().strftime("%d/%m/%Y")
            }
        )
        
       
class Cliente:
    def __init__(self, endereco:str):
        self.endereco = endereco
        self._contas = []


    @property
    def contas(self):
        return self._contas
    
    
    def adicionar_contas(self):
        pass
                
      
class PessoaFisica(Cliente):
    def __init__(self, endereco:str, nome:str, cpf:int, data_nascimeto:date):
        super().__init__(endereco)
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimeto
        
        
    def adicionar_contas(self, numero:int, cpf:int):
        self._contas.append(
            {
                "Conta": numero,
                "Nome": self.nome,
                "CPF": cpf,
                "DATA": datetime.now().strftime("%d/%m/%Y | %H:%M")
            }
        )
        return "Conta vinculada ao cliente!"
        

class Conta:
    def __init__(self, numero:int, cliente:Cliente):
        self._saldo = 0
        self.numero = numero
        self.agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()
        
    
    @property
    def saldo(self):
        return self._saldo
    
    
    @saldo.setter
    def saldo(self, valor:float):
        self._saldo -= valor    
    
    
    @property
    def cliente(self):
        return self._cliente
    
    
    @property
    def historico(self):
        return self._historico
    
    
    @classmethod
    def nova_conta(cls, cliente:Cliente, numero:int):
        return cls(numero, cliente)
    
    
    def sacar(self):
        pass        
    
    
    def depositar(self):
        pass
    

class ContaCorrente(Conta):
    def __init__(self, numero, cliente):
        super().__init__(numero, cliente)
        self._limite = 500.0
        self._limite_saque = 3
        
    
    @property
    def limite(self):
        return self._limite

        
    @property
    def limite_saque(self):
        return self._limite_saque
    
    
    def sacar(self, valor:float):
        if self._limite_saque != 0:
            if valor > 0 and valor <= self._limite:
                if (self._saldo - valor) >= 0:
                    self._saldo -= valor
                    self._limite_saque -= 1
                    Saque(valor, self).registrar(self)
                    return "Saque bem sussedido!"
                else:
                    return "Saldo INSUFICIÊNTE!"
            else:
                return f"Saque deve ser maior que 0 e menor que {self._limite}."
        else:
            return f"Você atingiu o limite máximo de saques!"
        
    
    def depositar(self, valor:float):
        if valor > 0:
            self._saldo += valor
            Deposito(valor, self).registrar(self)
            return "Valor depositado!"
        else:
            return "Depósito inválido!"
            
            
        
                    
                
def cliente_existe(cpf:int, clientes:list):
    """
    Recebe cpf e clientes para verificar
    a existência na lista de clientes
    
    Retorna True se existir
    """
    for cliente in clientes:
        if cliente.cpf == cpf:
            return True
    else:
        return False
    
    
def retorna_cliente(cpf:int, clientes:list):
    """
    Recebe cpf e cliente
    
    Retorna intância de cliente:Cliente
    """
    for cliente in clientes:
        if cliente.cpf == cpf:
            return cliente
    else:
        return False
    
        
def conta_existe(numero:int, contas:list):
    """
    Recebe numero e contas para verificar
    a existência na lista de contas
    
    Retorna True se existir
    """
    for conta in contas:
        if conta.numero == numero:
            return True
    else:
        return False


def retorna_conta(numero:int, contas:list):
    for conta in contas:
        if conta.numero == numero:
            return conta
    else:
        return False        
    
def listar_clientes():
    """
    Percorre clientes e printa
    cada ocorrência
    """
    global clientes
    if clientes:
        for cliente in clientes:
            print(f"""
                  CPF: {cliente.cpf}
                  NOME: {cliente.nome}
                  NASCIMENTO: {cliente.data_nascimento}
            """)
    else:
        print("Nenhum cliente cadastrado!")
    return ""     
    

def listar_contas():
    """
    Percorre contas e printa
    cada ocorrência
    """
    global contas
    if contas:
        for conta in contas:
            print(f"""
                  CPF TITULAR: {conta.cliente.cpf}
                  ================================
                  Nome: {conta.cliente.nome}
                  Número: {conta.numero}
                  Agência: {conta.agencia}
            """)
    else:
        print("Nenhuma conta cadastrada!")
    
    
def criar_PessoaFisica(endereco:str, 
        nome:str, 
        cpf:int, 
        dia_nas:int, 
        mes_nas:int, 
        ano_nas:int
    ):
    """ Função para criar Cliente > PessoaFisica

    Args:
        endereco (str): endereco
        nome (str): nome completo
        cpf (int): cpf da pessoa
        dia_nas (_type_): dia (DD)
        mes_nas (_type_): mês (MM)
        ano_nas (_type_): ano (YYYY)

    Returns:
        str : status de criação
    """
    global clientes
    if cliente_existe(cpf, clientes):
        return f"ERRO! CPF: {cpf} já cadastrado!"
    else:
        data = date(ano_nas, mes_nas, dia_nas)
        clientes.append(PessoaFisica(endereco, nome, cpf, data))
        return "Cliente criado!"


def criar_Conta(numero:int, cpf:int):
    """ Função para criar Conta > ContaCorrente

    Args:
        numero (int): numero para conta
        cpf (int): cpf do titular

    Returns:
        str: status de criação
    """
    global contas, clientes
    
    if cliente_existe(cpf, clientes):
        if conta_existe(numero, contas):
            return "Conta já existe!"
        else:
            cliente = retorna_cliente(cpf, clientes)
            contas.append(ContaCorrente.nova_conta(cliente, numero))
            status = cliente.adicionar_contas(numero, cpf)
            return f"Conta criada | {status}"
    else:
        return "Cliente ainda não foi criado!"     


def fazer_saque(cpf:int, numero_conta:int, valor:float) -> str:
    global contas, clientes
    
    if cliente_existe(cpf, clientes) and conta_existe(numero_conta, contas):
        cliente = retorna_cliente(cpf, clientes)
        cliente_contas = cliente.contas
        for conta_cliente in cliente_contas:
            if conta_cliente["Conta"] == numero_conta:
                conta = retorna_conta(numero_conta, contas)
                status = conta.sacar(valor)
                return status
            else:
                return "Conta não é do Cliente"
        else:
            return "Cliente não possui conta"
    else:
        return "Cliente não existe ou conta não existe."


def fazer_deposito(cpf:int, numero_conta:int, valor:float) -> str:
    global contas, clientes
    
    if cliente_existe(cpf, clientes) and conta_existe(numero_conta, contas):
        cliente = retorna_cliente(cpf, clientes)
        cliente_contas = cliente.contas
        for conta_cliente in cliente_contas:
            if conta_cliente["Conta"] == numero_conta:
                conta = retorna_conta(numero_conta, contas)
                status = conta.depositar(valor)
                return status
            else:
                return "Conta não é do Cliente"
        else:
            return "Cliente não possui conta"
    else:
        return "Cliente não existe ou conta não existe."
    
    
def exibir_extrato(numero:int):
    global contas
    if conta_existe(numero, contas):
        conta = retorna_conta(
            numero=numero,
            contas=contas
        )
        
        extrato = conta.historico.transacoes
        if extrato:    
            for transacao in extrato:
                mov = [f"{chave}: {valor}" for chave, valor in transacao.items()]
                print("\n".join(mov), end="\n\n")
            print(f"Saldo atual: R$ {conta.saldo}")
        else:
            return "Nenhum movimento na conta, ainda."
        
    else:
        return "Conta não existe!"

    
                    
            
    
