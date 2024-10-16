# 7: Soma de números pares de 1 a 100
soma_pares = 0

for i in range(2, 101, 2):  # Começa no 2 e pula de 2 em 2 até 100
    soma_pares += i

print(f"A soma de todos os números pares de 1 a 100 é {soma_pares}.")
