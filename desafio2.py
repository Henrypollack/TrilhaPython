# TODO: Crie uma Função: recomendar_plano para receber o consumo médio mensal:

    
# TODO: Crie uma Estrutura Condicional para verifica o consumo médio mensal 
# TODO: Retorne o plano de internet adequado:
    

# Solicita ao usuário que insira o consumo médio mensal de dados:
consumo = float(input("Digite a quantiade de consumo mensal: "))
def recomendar_plano(consumo):
  if (consumo <= 10):
    print(" Plano Essencial Fibra - 50Mbps")
  elif ((consumo >= 10) or (consumo <= 20)):
    print("Plano Prata Fibra - 100Mbps")
  elif (consumo > 20):
      print("Plano Premium Fibra - 300Mbps:")
  return consumo   

# Chama a função recomendar_plano com o consumo inserido e imprime o plano recomendado:
print(recomendar_plano(consumo))