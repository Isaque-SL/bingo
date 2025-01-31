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

print("Bem vindo ao nosso bingo :)\n")
print("Qual modo você gostaria de jogar?")
print("Nível acelerado: digite 1")
print("Nível demorado: digite 2")
nivel=int(input())
niveis = [1, 2]
print("")

# linhas = 2
# colunas = 3
# bingo = criar_cartela(linhas,colunas)

if nivel not in niveis:
    while nivel not in niveis:
        print("Esse número não equivale a um nível, digite apenas 1 ou 2:\n")
        nivel=int(input())
        print("")
  

if nivel==1:
  linhas = 2
  colunas = 3

  print("Jogador 1:")
  cartelajog1 = criar_cartela(linhas,colunas)
  for i in range(linhas):
    print('|', end=" ")
    for j in range(colunas):
        print(cartelajog1[i][j], end=" ")
    print('|')
  print("")

  print("Jogador 2:")
  bingo = criar_cartela(linhas,colunas)
  for i in range(linhas):
    print('|', end=" ")
    for j in range(colunas):
        print(bingo[i][j], end=" ")
    print('|')

if nivel==2:
  linhas = 3
  colunas = 4
  bingo = criar_cartela(linhas,colunas)
  





  

  