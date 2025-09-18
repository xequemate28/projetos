import random

porta_secreta = random.randint(1, 6)
tentativas = 0

print("🎯 Tente adivinhar a porta secreta entre 1 e 5!")

while True:
    tentativa = int(input("Digite seu palpite: "))
    tentativas += 1

    if tentativa < 1 or tentativa > 5:
        print("⛔ Número fora do intervalo! Tente entre 1 e 5.")
        continue  # pula para a próxima tentativa sem contar como erro

    if tentativa == porta_secreta:
        print(f"✅ Parabéns, Paulo! Você acertou em {tentativas} tentativas.")
        break  # encerra o jogo
    elif tentativa < porta_secreta:
        print("🔼 Tente um número maior.")
    else:
        print("🔽 Tente um número menor.")
        
# random é um módulo, não uma função nem um método.