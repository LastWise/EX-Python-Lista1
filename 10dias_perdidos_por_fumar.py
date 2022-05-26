cigarros_dia = float(input("Está é a quantidade de cigarros fumados por dia: "))

anos = float(input("E está é a quantidade de anos que fuma: "))

dias_perdidos = cigarros_dia*(anos*365)*10 / 1440

print("Aqui está os dias perdidos de vida:",dias_perdidos)
