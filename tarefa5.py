# Função para inverter a string
def inverter_string(s):
    # Converte a string em uma lista para manipulação
    lista = list(s)
    # Inicializa as variáveis para as posições inicial e final
    inicio = 0
    fim = len(lista) - 1
    
    # Troca os caracteres das posições inicio e fim até que se encontrem
    while inicio < fim:
        # Troca os caracteres
        lista[inicio], lista[fim] = lista[fim], lista[inicio]
        # Move os índices
        inicio += 1
        fim -= 1
    
    # Converte a lista de volta para string e retorna
    return ''.join(lista)

# Solicita ao usuário para inserir a string ou define uma string previamente
entrada_usuario = input("Digite a string para inverter (ou deixe em branco para usar uma string padrão): ")
if entrada_usuario.strip() == "":
    entrada_usuario = "exemplo"

# Inverte a string
resultado = inverter_string(entrada_usuario)

# Exibe o resultado
print("String invertida:", resultado)
