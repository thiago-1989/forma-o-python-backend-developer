# Recebe a entrada e armazena na variável "entrada"
entrada = input("Emails: ")

# Função reponsável por extrair os domínios dos emails
def extrair_dominios(emails):
    # Separa os emails por ponto e vírgula
    lista_emails = emails.split(';')

    # TODO: Implemente a lógica necessária para extrair os domínios
    dominios = []
    for item in range(0, len(lista_emails)):
        dominios.append(lista_emails[item].split('@')[1])

    return dominios


# Imprime a lista de strings com os domínios
print(extrair_dominios(entrada))
