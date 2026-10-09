from datetime import date, datetime


def calcular_idade(data_nascimento) -> int:
  """Calcula a idade de uma pessoa com base na data de nascimento.

  Aceita string 'DD/MM/AAAA' ou objeto date.
  """
  if isinstance(data_nascimento, str):
    data_nascimento = datetime.strptime(data_nascimento, "%d/%m/%Y").date()

  hoje = date.today()

  # Calcula a diferença de anos e ajusta se o aniversário ainda não ocorreu este ano
  idade = (
      hoje.year
      - data_nascimento.year
      - (
          (hoje.month, hoje.day) < (data_nascimento.month, data_nascimento.day)
      )
  )
  return idade


def calcular_dias_faltantes(data_futura) -> int:
  """Calcula a quantidade de dias que faltam até uma data futura.

  Aceita string 'DD/MM/AAAA' ou objeto date.
  """
  if isinstance(data_futura, str):
    data_futura = datetime.strptime(data_futura, "%d/%m/%Y").date()

  hoje = date.today()
  delta = data_futura - hoje
  return delta.days