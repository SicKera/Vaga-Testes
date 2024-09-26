# Sequencia de Fibonacci
import os
os.system('cls')
n = int (input("Insira um numero inteiro: "))

f1 = int (0)
f2 = int (1)

pertence = False


print("Sequencia: ")
while f1 <=  n:
    print(f"-{f1}")
    if n == f1:
        pertence = True
    f1, f2 = f2, f1 + f2

if pertence == True:
    print(f"O número {n} pertence á sequencia de Fibonacci.")
else:
    print(f"O número {n} não pertence á sequencia de Fibonacci.")