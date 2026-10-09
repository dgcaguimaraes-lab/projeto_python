from datetime import date, timedelta
from calculadora import calcular_dias_faltantes, calcular_idade


def test_calcular_idade_aniversario_ja_passado():
  # Simula alguém que nasceu em 1º de janeiro de 20 anos atrás usando o formato DD/MM/AAAA
  ano_passado = date.today().year - 20
  data_nasc = f"01/01/{ano_passado}"

  # Se hoje for após 1 de janeiro, a idade deve ser 20
  if date.today() > date(date.today().year, 1, 1):
    assert calcular_idade(data_nasc) == 20


def test_calcular_idade_com_objeto_date():
  # Testa passando diretamente um objeto date fixo no passado
  data_nasc = date(2000, 5, 15)
  idade_esperada = (
      date.today().year
      - 2000
      - ((date.today().month, date.today().day) < (5, 15))
  )
  assert calcular_idade(data_nasc) == idade_esperada


def test_calcular_dias_faltantes_futuro():
  # Testa uma data futura exata de 10 dias à frente (passando como objeto date)
  data_futura = date.today() + timedelta(days=10)
  assert calcular_dias_faltantes(data_futura) == 10


def test_calcular_dias_faltantes_passado():
  # Testa uma data no passado (deve retornar um valor negativo, passando como objeto date)
  data_passada = date.today() - timedelta(days=5)
  assert calcular_dias_faltantes(data_passada) == -5