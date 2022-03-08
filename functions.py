"""
Funções são blocos de códigos que podemos chamar conforme necessidade da sua utilização.
No Python as funções são consideradas higher order functions.
As funções possui escopo local e variaveis declarados dentro das funções não podem ser acessadas externamente.
As funções podem ser tipadas como exemplo a função soma()
"""


def hello(name):
    print(f"Hello, {name}")


hello("Carlos")
hello("Magrão")
hello("Zé Doido")


def paulistao_time(nome_time, qtde_titulo, maiusculo=False):
    
    if maiusculo:
        msg = f"O {nome_time.upper()} tem {qtde_titulo} titulos paulista. "
    else:
         msg = f"O {nome_time} tem {qtde_titulo} titulos paulista. "
    
    print(msg)


paulistao_time("Corinthians", 30)
paulistao_time("São Paulo", 22)
paulistao_time("Palmeiras", 23, maiusculo=True)
paulistao_time("Santos", 22)


def soma(a: int, b: int) -> int:
    resultado = a + b
    return resultado

resultado = soma(5, 10)
print(resultado)