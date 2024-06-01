# TODO: Crie uma Lista 'itens' para armazenar os equipamentos:


# TODO: Crie um loop para solicita os itens ao usuário:

# TODO: Solicite o item e armazena na variável "item":

# TODO: Adicione o item à lista "itens":


# Exibe a lista de itens
item = []
i = 0
while (i < 3):
  item.append(str(input()))
  i += 1
  
itens = item
  
print("Lista de Equipamentos:")
for item in itens:
    # Loop que percorre cada item na lista "itens"
    print(f"- {item}")