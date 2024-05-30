consumo = float(input("\033[32m Digite a quantiade de consumo médio mensal em GB que voce usa: \033[m "))
def recomendar_plano(consumo_med):
  if consumo_med <= 10:
    return f"""Com o consumo medio de {consumo}GB no mês indicamos voce usar o \033[35mPlano Essencial Fibra - 50Mbps.\033[m 
Este plano ideal para você!."""
  elif consumo_med >= 10 and consumo <= 20:
    return f"""Com o consumo medio de {consumo}GB no mês indicamos voce usar o \033[30:47mPlano Prata Fibra - 100Mbps\033[m
Este plano ideal para você!."""
  elif consumo_med >=20:
      return f"""Com o consumo medio de {consumo}GB no mês indicamos voce usar o \033[33mPlano Premium Fibra - 300Mbps.\033[m
Este plano ideal para você!."""

     
print(recomendar_plano(consumo))