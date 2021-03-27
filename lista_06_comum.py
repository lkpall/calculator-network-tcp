import struct

# Pacote para requisição (cliente -> servidor)
FORMATO_OPERACAO = "!i i f i i i"
TAMANHO_OPERACAO = struct.calcsize(FORMATO_OPERACAO)

FORMATO_RESPOSTA = "!i f i i i"
TAMANHO_RESPOSTA = struct.calcsize(FORMATO_RESPOSTA)

# Porta do serviço
PORTA_SERVICO = 5000
