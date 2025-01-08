import random
import re


def rolar_dado(tipo, quantidade):
    resultado = []
    for i in range(quantidade):
        res = random.randint(1, tipo)
        resultado.append(res)
    return resultado


def interpretar_entrada(entrada):
    padrao = r"(\d+)d(\d+)([+-]\d+)?"
    match = re.match(padrao, entrada)

    if match:
        quantidade = int(match.group(1))
        tipo = int(match.group(2))
        modificador = match.group(3)

        if modificador:
            modificador = int(modificador)
        else:
            modificador = 0

        return quantidade, tipo, modificador
    else:
        return None


def main():
    
    print(f"Bem vindo ao D20Py")
    
    while True:
        entrada = input("Digite o lançamento desejado (ex:1d20+3): ")

        resultado = interpretar_entrada(entrada)

        continuar = ''

        if resultado:
            quantidade, tipo, modificador = resultado
            lancamentos = rolar_dado(tipo, quantidade)

            soma = sum(lancamentos) + modificador

            print(f"Você rolou {quantidade} dado(s) de {
                  tipo} faces: {lancamentos}")
            print(
                f"Soma dos lançamentos + modificador ({modificador}): {soma}")

        else:
            print("Entrada inválida! Por favor, use o formato correto.")

        continuar = input("Deseja lançar novamente? (s/n): ")

        if continuar.lower() != 's':
            print("Obrigado por jogar!")
            break



main()
