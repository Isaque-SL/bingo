import random


def criar_cartela(linhas, colunas):
    cartela = []
    numeros_usados = set()

    for i in range(linhas):
        linha = []

        while len(linha) < colunas:
            for j in range(colunas):
                arg1 = 1 + (j * 10)
                arg2 = arg1 + 9
                num = random.randint(arg1, arg2)
                if num not in numeros_usados:
                    linha.append(num)
                    numeros_usados.add(num)

        cartela.append(linha)

    return cartela

def mostrar_cartela(cartela):
    for linha in cartela:
        print("|", " ".join(f"{num:2}" if num != "X" else " X" for num in linha), "|")
    print("")

def verificar_vitoria(cartela):
    return all(num == "X" for linha in cartela for num in linha)

def marcar_numero(cartela, num_sorteado):
    for i in range(len(cartela)):
        for j in range(len(cartela[i])):
            if cartela[i][j] == num_sorteado:
                cartela[i][j] = "X"

print("Bem-vindo ao nosso bingo! :]\n")
print("Escolha um nível de jogo:")
print("1 - Nível acelerado")
print("2 - Nível demorado")

nivel = int(input("Digite o nível desejado: "))
while nivel not in [1, 2]:
    nivel = int(input("Opção inválida. Digite 1 ou 2: "))

print("\nCriando cartelas...\n")
if nivel == 1:
    linhas, colunas, num_jogadores = 2, 3, 2
else:
    linhas, colunas, num_jogadores = 3, 4, 4

jogadores = {f"Jogador {i+1}": criar_cartela(linhas, colunas) for i in range(num_jogadores)}

for jogador, cartela in jogadores.items():
    print(f"{jogador}:")
    mostrar_cartela(cartela)

sorteados = []
vencedor = None

print("\nO jogo começou! Sorteando os números...\n")

while not vencedor:
    num_sorteado = random.randint(1, 40)

    if num_sorteado not in sorteados:
        sorteados.append(num_sorteado)
        print(f"Número sorteado: {num_sorteado}")
        print(f"Números já sorteados: {sorted(sorteados)}\n")

        for jogador, cartela in jogadores.items():
            marcar_numero(cartela, num_sorteado)
            if verificar_vitoria(cartela):
                vencedor = jogador
                break

        for jogador, cartela in jogadores.items():
            print(f"{jogador}:")
            mostrar_cartela(cartela)

        input("Pressione ENTER para sortear o próximo número...")

print(f"\nBINGO! {vencedor} venceu o jogo!\n")