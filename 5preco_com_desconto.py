preco = float(input("Este é o preço em reais: "))
desconto = float(input("Este é o valor do desconto em porcentagem: "))

novo_preco = preco - (preco*desconto/100)

print("Este é o preço final em reais: " + str(novo_preco))