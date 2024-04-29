# Constantes
LIMITE_SAQUES = 3
LIMITE = 500
AGENCIA = '0001'

# Variáveis globais
saldo = 0
extrato = ''
num_saques = 0
usuarios = []
contas = []


def menu():
  print('''
################################
Bem-vindo ao The Bank System!

[1] - Depositar
[2] - Sacar
[3] - Extrato
[4] - Criar Usuário
[5] - Criar Conta
[0] - Sair

→ Selecione uma opção: ''', end='')


def depositar(valor):
  global saldo, extrato
  if valor <= 0:
    print('Valor inválido, por favor informe um valor maior que zero!')
  else:
    saldo += valor
    extrato += f' [+] R$ {valor:.2f}\n'
    print('Depósito efetuado com sucesso!')


def sacar(valor):
  global saldo, extrato, num_saques, LIMITE_SAQUES
  if valor <= 0:
    print('Valor inválido, por favor informe um valor maior que zero!')
  elif valor > LIMITE:
    print(f'O valor máximo por saque é de R$ {LIMITE:.2f}, saque não efetuado!')
  elif num_saques >= LIMITE_SAQUES:
    print('Você atingiu o limite de saques diários, saque não efetuado!')
  elif saldo < valor:
    print('Saldo insuficiente!')
  else:
    saldo -= valor
    extrato += f' [-] R$ {valor:.2f}\n'
    num_saques += 1
    print('Saque efetuado com sucesso!')


def exibir_extrato():
  global extrato
  if not extrato:
    print('Não há movimentações!')
  else:
    print('Extrato:')
    linhas = extrato.split('\n')
    for linha in linhas:
      if linha.startswith(' [+]'):
        print('\033[92m' + linha + '\033[0m')
      elif linha.startswith(' [-]'):
        print('\033[91m' + linha + '\033[0m')
      else:
        print(linha)
    print(f'Saldo: R$ {saldo:.2f}')


def criar_usuario():
  cpf = input('Informe o CPF: ')
  usuario = buscar_usuario(cpf)

  if usuario:
    print('Usuário já cadastrado!')
  else:
    nome = input('Informe o nome completo: ').upper()
    data = input('Informe a data de nascimento: ')
    logradouro = input('Informe o logradouro: ').upper()
    numero = input('Informe o número: ')
    bairro = input('Informe o bairro: ').upper()
    cidade = input('Informe a cidade: ').upper()
    estado = input('Informe o estado: ').upper()

    usuarios.append({
      'cpf': cpf,
      'nome': nome,
      'data': data,
      'endereco': {
        'logradouro': logradouro,
        'numero': numero,
        'bairro': bairro,
        'cidade': cidade,
        'estado': estado
      }
    })
    print('Usuário cadastrado com sucesso!')


def buscar_usuario(cpf):
  for usuario in usuarios:
    if usuario['cpf'] == cpf:
      return usuario
  return None


def criar_conta():
  cpf = input('Informe o CPF do usuário: ')
  usuario = buscar_usuario(cpf)

  if not usuario:
    print('Usuário não encontrado!')
  else:
    num_conta = len(contas) + 1
    contas.append({
      'agencia': AGENCIA,
      'conta': num_conta,
      'cpf': cpf
    })
    print('Conta criada com sucesso!')


def main():
  while True:
    menu()
    opcao = input()

    if opcao == '1':
      print(' DEPÓSITO '.center(32, '#'))
      valor = float(input('Valor a ser depositado: '))
      depositar(valor)

    elif opcao == '2':
      print(' SAQUE '.center(32, '#'))
      valor = float(input('Valor a ser sacado: '))
      sacar(valor)

    elif opcao == '3':
      print(' EXTRATO '.center(32, '#'))
      exibir_extrato()

    elif opcao == '4':
      print(' CRIAR USUÁRIO '.center(32, '#'))
      criar_usuario()
      print(usuarios)

    elif opcao == '5':
      print(' CRIAR CONTA '.center(32, '#'))
      criar_conta()
      print(contas)

    elif opcao == '0':
      print('Agradeçemos a preferência, volte sempre!')
      break

    else:
      print('Opção inválida, por favor selecione novamente a operação desejada!')


if __name__ == "__main__":
  main()
