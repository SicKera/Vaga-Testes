# Identificador de Caractere

import os
os.system('cls')

texto = input("Insira seu texto aqui: ")

contador = 0

for caractere in texto:
    if caractere == "a" or caractere == "A":
        contador = contador + 1

if contador > 0:
    print(f"A letra 'a' ou 'A' aparece {contador} vezes no texto")
else:
    print("A letra 'a' ou 'A' não aparece no texto.")