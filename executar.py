from calculadora import calcular_dias_faltantes, calcular_idade


def main():
  print("--- TESTE INTERATIVO DE DATAS ---")

  # 1. Testando o cálculo de idade
  print("\n[1/2] Cálculo de Idade")
  nascimento = input(
      "Digite sua data de nascimento (no formato DD/MM/AAAA, ex: 15/10/1995): "
  )

  try:
    idade = calcular_idade(nascimento)
    print(f"-> A idade calculada é: {idade} anos.")
  except ValueError:
    print(
        "Erro: Formato de data inválido. Certifique-se de usar o padrão"
        " DD/MM/AAAA."
    )

  # 2. Testando o cálculo de dias faltantes
  print("\n[2/2] Cálculo de Dias Faltantes")
  futuro = input(
      "Digite uma data no futuro (no formato DD/MM/AAAA, ex: 31/12/2026): "
  )

  try:
    dias = calcular_dias_faltantes(futuro)
    if dias >= 0:
      print(f"-> Faltam {dias} dias para essa data.")
    else:
      print(
          f"-> Essa data já passou (está a {-dias} dias no passado relative a"
          " hoje)."
      )
  except ValueError:
    print(
        "Erro: Formato de data inválido. Certifique-se de usar o padrão"
        " DD/MM/AAAA."
    )


if __name__ == "__main__":
  main()