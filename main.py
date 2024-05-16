from funcoes import *

def main():
  clientes = []
  contas = []

  while True:
    menu()
    opcao = int(input('Digite a opção desejada: '))

    if opcao == 1:
      print(' DEPÓSITO '.center(32, '#'))
      deposito(clientes)
    elif opcao == 2:
      print(' SAQUE '.center(32, '#'))
      saque(clientes)
    elif opcao == 3:
      print(' EXTRATO '.center(32, '#'))
      imprimir_extrato(clientes)
    elif opcao == 4:
      print(' CRIAR USUÁRIO '.center(32, '#'))
      criar_cliente(clientes)
    elif opcao == 5:
      print(' CRIAR CONTA '.center(32, '#'))
      numero_conta = len(contas) + 1
      criar_conta(numero_conta, clientes, contas)
    elif opcao == 6:
      print(' LISTAR CONTAS '.center(32, '#'))
      listar_contas(contas)
    elif opcao == 0:
      linha()
      print('Obrigado por utilizar o The Bank System!')
      break
    else:
      linha()
      print('Opção inválida!')
  

if __name__ == '__main__':
  main()