"""
Além dos tipos básicos, outros tipos muito comum são.
*   List (list)
        *   Suporta múltiplos tipos de dados inclusive variaveis, pode ser heterogênea 
        *   É possível inserir elementos utilizando append e insert
        *   Remover elementos utilizando remove
*   Tuple
        *   Utilizado para dados imutaveis, após a atribuição objeto é imutável.    
        *
*   Dictionary (dic)
        *   Conhecido nas outras linguagens como array associativo chave : valor
        *   No dicionário diferente da List utilizamos a chave para tratar 

"""

# ==========================    Type List   ========================== 
print("==========================    Result Type List   ========================== ")
print("\n")
cores = ["Amarelo", "Azul", "Vermelho"]
misturado = [cores, 1, 3, 4.5, "lista"]


print(misturado)

"""
output print(misturado)
[['Amarelo', 'Azul', 'Vermelho'], 1, 3, 4.5, 'lista']
"""

cores.append("Branco")
cores.insert(2, "Preto")

print(cores)
"""
output print(cores)
['Amarelo', 'Azul', 'Preto', 'Vermelho', 'Branco']
"""

cores.remove("Branco")

print(cores)
"""
output print(cores)
['Amarelo', 'Azul', 'Preto', 'Vermelho']
"""

# ==========================    Type Tuple   ==========================
print("\n")
print("==========================    Result Type Tuple   ========================== ")
print("\n")

identidade = ("Maria", "24578974896-8", 30)

print(f"Nome é {identidade[0]}")
print(f"Idade é {identidade[2]}")
print(f"Cpf Cadastrado é {identidade[1]}")

# unpacking desempacotar
nome, cpf, idade = identidade
print(nome)
print(cpf)
print(idade)
# ==========================    Type Dictionary   ==========================
print("\n")
print("==========================    Result Type Dictionary   ========================== ")
print("\n")

pessoa = {
    "nome": "Mario",
    "idade": 50,
    "cpf": 4578987458-9
}

print(pessoa)

pessoa["idade"] = 51

print(pessoa)

pessoa[0] = "João"