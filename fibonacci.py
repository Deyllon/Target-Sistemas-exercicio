


def verifica_se_o_numero_esta_na_sequência():
    numero = int(input("Digite um numero para verificar se ele está na sequência de Fibonacci: "))
    penultimo = 0
    ultimo = 1
    termo = 0
    while(termo < numero):
        termo = ultimo + penultimo
        penultimo = ultimo
        ultimo = termo
        if termo == numero:
            return "O numero está na sequencia"
    return "O numero não está na sequência"

print(verifica_se_o_numero_esta_na_sequência())
    