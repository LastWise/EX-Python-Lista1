dias = float(input("Insira aqui a quantidade de dias que o carro foi alugado: "))

quilometros = float(input("Insira aqui a quantidade de quilometros rodados: "))

valor = dias*60 + 0.15*quilometros

print("Este é o valor a ser pago:",str(valor) + " reais")