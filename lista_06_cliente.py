import socket
import struct
import lista_06_comum as comum

socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_cliente.connect(("localhost", comum.PORTA_SERVICO))


def vendas():
    print("\n==============================================================================\n")
    opcao = int(input("Escolha sua opção:\n"
                      "0 - Sair do programa\n"
                      "1 - Cadastrar uma venda\n"
                      "2 - Mostrar uma venda a partir de seu código\n"
                      ">>"))
    if opcao == 0:
        pacote_operacao = struct.pack(comum.FORMATO_OPERACAO, opcao, 0, 0, 0, 0, 0)
        socket_cliente.sendall(pacote_operacao)
        return True
    elif opcao == 1:
        while True:
            cod = int(input("Digite o código da venda: "))
            valor = float(input("Digite o valor da venda(R$): "))
            dia = int(input("Digite o dia da venda(dd): "))
            mes = int(input("Digite o mês da venda(mm): "))
            ano = int(input("Digite o ano da venda(aaaa): "))
            if (0 < dia < 32) and (0 < mes < 13) and (1950 < ano < 2022):
                pacote_operacao = struct.pack(comum.FORMATO_OPERACAO, opcao, cod, valor, dia, mes, ano)
                socket_cliente.sendall(pacote_operacao)
                break
            else:
                print("Um dos valores é inválido!")
    elif opcao == 2:
        cod = int(input("Digite o código da venda a ser consultada: "))
        pacote_operacao = struct.pack(comum.FORMATO_OPERACAO, opcao, cod, 0, 0, 0, 0)
        socket_cliente.sendall(pacote_operacao)

        pacote_resposta = socket_cliente.recv(comum.TAMANHO_RESPOSTA)
        cod, valor, dia, mes, ano = struct.unpack(comum.FORMATO_RESPOSTA, pacote_resposta)
        print("\n>>>>>>>>>> Consulta <<<<<<<<<<\n"
              f"Código: {cod}\n" 
              f"Valor: R$ {valor}\n"
              f"Data: {dia}/{mes}/{ano}")
    else:
        print("Operação inválida, tente novamente!")


while True:
    a = vendas()
    if a:
        socket_cliente.close()
        break
