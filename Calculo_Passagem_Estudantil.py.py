import math, os
os.system('cls')

print('Essa ferramenta auxilia no cálculo da sua passagem, supondo que você usa o Bilhete de Estudante de escola particular.\nEquivalente à meia-passagem comum.')

conducao = int(input('Quantas conduções você pega por dia? '))

valor = float(input('Digite o valor que você colocará no bilhete: '))

pass1 = 2.20

# diario = quantidade de dinheiro que eu gasto com condução por dia
diario = conducao * pass1
# rent = dias que o meu passe vai durar
rent = valor / diario
# sobra = quanto vai sobrar no meu bilhete em 1 dia de uso
sobra = valor - diario
# qqpu = quantidade que posso usar com o valor da recarga
qqpu = diario * math.floor(rent)
# sobra_geral = quanto vai sobrar no meu bilhete até eu não conseguir mais usa-lo
sobra_geral = valor - qqpu

if diario > valor:
    print('O valor que você inseriu não é o suficiente para completar sua rota.')

elif diario < valor:
    print(f'Se você recarregar R${valor}, com base na quantidade de conduções que você pega por dia, seu passe vai durar {math.floor(rent)} dias, e vai sobrar {sobra_geral:.2f} no seu bilhete.')
