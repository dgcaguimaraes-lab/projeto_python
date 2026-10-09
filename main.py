
from datetime import date


def calcular_idade(data_nascimento):
    hoje = date.today()
    idade = hoje.year - data_nascimento.year

    if (hoje.month, hoje.day) < (data_nascimento.month, data_nascimento.day):
        idade -= 1

    return idade


def dias_ate_data(data_futura):
    hoje = date.today()
    return (data_futura - hoje).days


if __name__ == "__main__":
    nascimento = date(1990, 5, 15)
    futuro = date(2026, 12, 31)

    print("Idade:", calcular_idade(nascimento))
    print("Dias até a data futura:", dias_ate_data(futuro))