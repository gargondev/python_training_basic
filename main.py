from datetime import date

'''
Calculando o ano de nascimento com base na idade digitada no input
'''

# Instancia uma variavel com string vazia
idade = ""

# Identifica o dia atual
dateToday = date.today()

# No while enquanto idade não for inteiro continua execução.
while not isinstance(idade, int):
  try:
      # input passa valor para variavel idade.
      idade = input("Digite a sua idade: ")
      # 
      print(f'Você nasceu no Ano de  {dateToday.year - int(idade)}')
      break
  except:
        print("Erro no calculo da idade, digite um número inteiro.");