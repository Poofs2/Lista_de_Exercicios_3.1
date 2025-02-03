# Reverter os Caracteres de uma String

'''
Exercicio 1:
Escreva uma Função Recursiva Chamada 
reverter_caracteres(s) que Recebe uma
String s e Devolve a String Invertida.
Não use Laços (for ou while).
'''

# --- Exercise 1 ---
print("--- Exercise 1 ---")

# --- Function ---
def reverter_caracteres(s: str) -> str:
    if len(s) == 0:
        return s
    return s[-1] + reverter_caracteres(s[:-1])
# --- Function ---

print(reverter_caracteres('batata'))
print("------------------")
# --- Exercise 1 ---