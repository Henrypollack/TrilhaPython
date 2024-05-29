# TODO: Crie uma Função: recomendar_plano para receber o consumo médio mensal:

    
# TODO: Crie uma Estrutura Condicional para verifica o consumo médio mensal 
# TODO: Retorne o plano de internet adequado:
    

# Solicita ao usuário que insira o consumo médio mensal de dados:
consumo = float(input("\033[32m Digite a quantiade de consumo médio mensal em GB que voce usa: \033[m "))
def recomendar_plano(consumo):
  if consumo <= 10:
    print(f"""Com o consumo medio de {consumo}GB no mês indicamos voce usar o \033[35mPlano Essencial Fibra - 50Mbps.\033[m 
Este plano ideal para você!.""")
  elif consumo >= 10 and consumo <= 20:
    print(f"""Com o consumo medio de {consumo}GB no mês indicamos voce usar o \033[30:47mPlano Prata Fibra - 100Mbps\033[m
Este plano ideal para você!.""")
  elif consumo >=20:
      print(f"""Com o consumo medio de {consumo}GB no mês indicamos voce usar o \033[33mPlano Premium Fibra - 300Mbps.\033[m
Este plano ideal para você!.""")
     

# Chama a função recomendar_plano com o consumo inserido e imprime o plano recomendado:
print(recomendar_plano(consumo))