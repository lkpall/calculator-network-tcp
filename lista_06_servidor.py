import socket
import struct
import threading
import lista_06_comum as comum


def tratar_cliente(socket_conexao, endereco_cliente):
    while True:
        print("\n==============================================================================\n")
        pacote_opcao = socket_conexao.recv(comum.TAMANHO_OPERACAO)
        opcao, cod, valor, dia, mes, ano = struct.unpack(comum.FORMATO_OPERACAO, pacote_opcao)
        print(f"Recebido opcão: {opcao}")

        if opcao == 0:
            print("Conexão finalizada!")
            socket_conexao.close()
            break
        elif opcao == 1:
            venda = [cod, valor, dia, mes, ano]
            listaVendas.append(venda)
            print(f"Dados recebidos de {endereco_cliente}.")
        elif opcao == 2:
            tamListBuy = len(listaVendas)
            for i in range(tamListBuy):
                teste = listaVendas[i][0]
                if teste == cod:
                    consulta = listaVendas[i]
                    pacote_operacao = struct.pack(comum.FORMATO_RESPOSTA, consulta[0], consulta[1], consulta[2],
                                                  consulta[3], consulta[4])
                    socket_conexao.sendall(pacote_operacao)
                    break


socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_servidor.bind(("0.0.0.0", comum.PORTA_SERVICO))
socket_servidor.listen()

listaVendas = []

while True:
    print("Esperando cliente...")
    socket_conexao, endereco_cliente = socket_servidor.accept()
    print(f"Cliente {endereco_cliente} conectou!")

    threading.Thread(target=tratar_cliente, args=(socket_conexao, endereco_cliente)).start()
    print(f"Thread criada para o cliente {endereco_cliente}!")

