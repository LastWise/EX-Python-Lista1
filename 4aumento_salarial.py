salario = float(input("Este é o valor do salario: "))
aumento = float(input("Este é aumento do salário em porcentagem: "))

novo_salario = salario + (salario * aumento/100)

print("Este é o salario com o aumento porcentual: " + str(novo_salario) + " reais")