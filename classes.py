from abc import ABC, abstractmethod
from datetime import datetime

class Transacao(ABC):
  @property
  @abstractmethod
  def valor(self):
    pass

  @abstractmethod
  def registrar(self, conta):
    pass

class Deposito(Transacao):
  def __init__(self, valor):
    self._valor = valor

  @property
  def valor(self):
    return self._valor

  def registrar(self, conta):
    sucesso_transacao = conta.depositar(self._valor)

    if sucesso_transacao:
        conta.historico.adicionar_transacao(self)

class Saque(Transacao):
  def __init__(self, valor):
    self._valor = valor

  @property
  def valor(self):
    return self._valor

  def registrar(self, conta):
    sucesso_transacao = conta.sacar(self._valor)

    if sucesso_transacao:
        conta.historico.adicionar_transacao(self)

class Historico:
  def __init__(self):
    self._transacoes = []

  @property
  def transacoes(self):
    return self._transacoes
  
  def adicionar_transacao(self, transacao):
    self._transacoes.append(
      {
        "tipo": transacao.__class__.__name__,
        "valor": transacao.valor,
        "data": datetime.now().strftime('%d/%m/%Y %H:%M:%S')
      }
    )

class Conta:
  def __init__(self, numero, cliente):
    self._saldo = 0
    self._numero = numero
    self._agencia = "0001"
    self._cliente = cliente
    self._historico = Historico()

  @classmethod
  def nova_conta(cls, cliente, numero):
    return cls(numero, cliente)

  @property
  def saldo(self):
    return self._saldo
    
  @property
  def numero(self):
    return self._numero
  
  @property
  def agencia(self):
    return self._agencia
  
  @property
  def cliente(self):
    return self._cliente
  
  @property
  def historico(self):
    return self._historico
  
  def sacar(self, valor):
    if valor > self._saldo:
      print("Saldo insuficiente")

    elif self._saldo >= valor and valor > 0:
      self._saldo -= valor
      print(f"R$ {valor:.2f} sacado com sucesso")
      return True
    else:
      print("Valor inválido")
    return False
  
  def depositar(self, valor):
    if valor > 0:
      self._saldo += valor
      print(f"R$ {valor:.2f} depositado com sucesso")
    else:
      print("Valor inválido")
      return False
    return True

class ContaCorrente(Conta):
  def __init__(self, numero, cliente, limite=500, limite_saque=3):
    super().__init__(numero, cliente)
    self._limite = limite
    self._limite_saque = limite_saque 
  
  def sacar(self, valor):
    qtd_saque = len([transacao for transacao in self.historico.transacoes if transacao['tipo'] == Saque.__name__])
    total_limite = valor > self._limite
    total_saque = qtd_saque >= self._limite_saque

    if valor > self._saldo:
      print("Saldo insuficiente")
      return False    
  	
    if total_limite:
      print("Valor acima do limite")
      return False
    

    if total_saque:
      print("Limite de saques atingido")
      return False
   
    self._saldo -= valor
    print(f"R$ {valor:.2f} sacado com sucesso")
    return True
  
  def __str__(self):
    return f"""\
      Agência:\t{self.agencia}
      Conta Corrente:\t{self.numero}
      Titular:\t{self.cliente.nome}
    """

class Endereco:
  def __init__(self, logradouro, numero, cidade, estado):
    self.logradouro = logradouro
    self.numero = numero
    self.cidade = cidade
    self.estado = estado

class Cliente:
  def __init__(self, endereco):
    self.endereco = endereco
    self.contas = []

  def realizar_transacao(self, conta, transacao):
    return transacao.registrar(conta)
  
  def adicionar_conta(self, conta):
    self.contas.append(conta)
  
class PessoaFisica(Cliente):
  def __init__(self, cpf, nome, data_nascimento, endereco):
    super().__init__(endereco)
    self.cpf = cpf
    self.nome = nome
    self.data_nascimento = data_nascimento