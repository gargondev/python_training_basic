"""
No tratamento de erros do python primeiro erro encontrado ele não passara para a proxima execução.
No bloco except sempre devemos colocar o erro atribuído, para não tratarmos erros genéricos.
Diferente de outras linguagens os erros no Python, são tratados como controle de fluxo, e aceitos para tomada de decisão.
Python em Tratamento de erros trabalha com abordagem EAFP - Easier to ask for forgiveness than permission.
"""
a = 0
b = 5


try:
    b.upper()
    print(b // a)
except AttributeError as e:
    print("Erro Atribuição variavel b", str(e))
except ZeroDivisionError as e:
    print("Erro na Divisão :", str(e))

    
