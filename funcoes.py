import textwrap
from classes import *

def menu():
  print('''
################################
Bem-vindo ao The Bank System!

[1] - Depositar
[2] - Sacar
[3] - Extrato
[4] - Criar Usuário
[5] - Criar Conta
[6] - Listar Contas     
[0] - Sair
''')

def linha():
  print('#'*32)

def filtrar_cliente(cpf, clientes):
  for cliente in clientes:
    if cliente.cpf == cpf:
      return cliente
  return None

def filtrar_conta(cliente):
  if not cliente.contas:
    print('Nenhuma conta encontrada')
    return
  return cliente.contas[0]

def deposito(clientes):
  cpf = input('Informe o CPF do cliente→ ')
  cliente = filtrar_cliente(cpf, clientes)

  if not cliente:
    print('Cliente não encontrado')
    return
  
  valor = float(input('Informe o valor do depósito→ '))
  transacao = Deposito(valor)

  conta = filtrar_conta(cliente)
  if not conta:
    print('Conta não encontrada')
    return
  cliente.realizar_transacao(conta, transacao)

def saque(clientes):
  cpf = input('Informe o CPF do cliente→ ')
  cliente = filtrar_cliente(cpf, clientes)

  if not cliente:
    print('Cliente não encontrado')
    return
  
  valor = float(input('Informe o valor do saque→ '))
  transacao = Saque(valor)

  conta = filtrar_conta(cliente)
  if not conta:
    print('Conta não encontrada')
    return
  cliente.realizar_transacao(conta, transacao)

def imprimir_extrato(clientes):
  cpf = input('Digite o CPF do cliente: ')
  cliente = filtrar_cliente(cpf, clientes)

  if not cliente:
    print('Cliente não encontrado')
    return
  
  conta = filtrar_conta(cliente)
  if not conta:    
    return
  
  transacoes = conta.historico.transacoes
  extrato = ''

  if not transacoes:
    extrato = 'Nenhuma movimentação realizada'
  else:
    for transacao in transacoes:
      if transacao['tipo'] == 'Deposito':
        extrato += f'\n{transacao["data"]}: \033[32m[+] R$ {transacao["valor"]:.2f}\033[0m'
      elif transacao['tipo'] == 'Saque':
        extrato += f'\n{transacao["data"]}: \033[31m[-] R$ {transacao["valor"]:.2f}\033[0m'

  print(extrato)
  print(f'\nSaldo atual: R$ {conta.saldo:.2f}')

def criar_cliente(clientes):
  cpf = input('Informe o CPF do cliente→ ')
  cliente = filtrar_cliente(cpf, clientes)

  if cliente:
    print('Cliente já cadastrado')
    return
  
  nome = input('Informe o nome→ ').upper()
  data_nascimento = input('Informe a data de nascimento→ ')
  logradouro = input('Logradouro(Rua, Av, etc)→ ').upper()
  numero = input('Informe o número→ ')
  cidade = input('Informe a cidade→ ').upper()
  estado = input('Informe o estado→ ').upper()

  endereco = Endereco(logradouro, numero, cidade, estado)
  cliente = PessoaFisica(cpf, nome, data_nascimento, endereco)
  clientes.append(cliente)
  print('Cliente cadastrado com sucesso')

def criar_conta(numero_conta, clientes, contas):
  cpf = input('Digite o CPF do cliente: ')
  cliente = filtrar_cliente(cpf, clientes)

  if not cliente:
    print('Cliente não encontrado')
    return
  
  conta = ContaCorrente.nova_conta(cliente=cliente, numero=numero_conta)
  contas.append(conta)
  cliente.contas.append(conta)
  print('Conta criada com sucesso')

def listar_contas(contas):
  lin = 1
  for conta in contas:    
    print(textwrap.dedent(str(conta)))
    if len(contas) > lin:
     linha()
     lin += 1
