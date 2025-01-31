import random


def criar_cartela(linhas, colunas):
  cartela = []
  num_sortido = []
  for i in range(linhas):
    cartela.append([])
    item = 0
    arg1 = 1
    arg2 = 10
    while len(cartela[i]) != colunas:
      intervalo = [arg1, arg2]
      cartela[i].append(random.randint(*intervalo))
      if cartela[i][item] in num_sortido:
        cartela[i].pop(item)
        item -= 1
      else:
        num_sortido.append(cartela[i][item])
        arg1, arg2 = arg1 + 10, arg2 + 10
      item += 1
  return cartela

linhas = 2
colunas = 3
bingo = criar_cartela(linhas, colunas)

for i in range(linhas):
  for j in range(colunas):
    print(bingo[i][j], end=" ")
  print("\n")