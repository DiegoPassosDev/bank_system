menu = '''
################################
Bem-vindo ao The Bank System!

[1] - Depositar
[2] - Sacar
[3] - Extrato
[0] - Sair

→ Selecione uma opção: '''	
saldo = 0
LIMITE = 500
extrato = ''
num_saques = 0
LIMITE_SAQUES = 3
depositar = ' DEPÓSITO '
saque = ' SAQUE '
extra = ' EXTRATO '


while True:
  opcao = input(menu)
  
  if opcao == '1':
    print(depositar.center(32, '#'))
    valor = float(input('Valor a ser depositado: '))
    if valor <= 0:      
      print('Valor inválido, por favor informe um valor maior que zero!')
      continue
    else:
      saldo += valor
      extrato += f' [+] R$ {valor:.2f}\n'
      print('Depósito efetuado com sucesso!') 

  elif opcao == '2':
    print(saque.center(32, '#'))
    valor = float(input('Valor a ser sacado: '))
    if valor <= 0:
      print('Valor inválido, por favor informe um valor maior que zero!')
      continue
    elif valor > LIMITE:
      print(f'O valor máximo por saque é de R$ {LIMITE:.2f}, saque não efetuado!')
      continue
    elif num_saques >= LIMITE_SAQUES:
      print('Você atingiu o limite de saques diários, saque não efetuado!')
      continue
    elif saldo < valor:
      print('Saldo insuficiente!')
      continue
    else:
      saldo -= valor
      extrato += f' [-] R$ {valor:.2f}\n'
      num_saques += 1
      print('Saque efetuado com sucesso!')

  elif opcao == '3':
    print(extra.center(32, '#'))
    print(f'Não há movimentações!' if not extrato else 'Extrato:\n' + extrato)
    print(f'Saldo: R$ {saldo:.2f}')    

  elif opcao == '0':
    print('Agradeçemos a preferência, volte sempre!')
    break

  else:
    print('Opção inválida, por favor selecione novamente a operação desejada!')
    continue