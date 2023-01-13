name = input('Qual é o seu nome ?')
lastname = input('Qual é o seu sobrenome?')

#print(name, lastname)


# Exercícios do Módulo 1 - Operações, Variáveis e Input

### Parte 1 - Operações e Variáveis
# Crie um programa que imprima (print) os principais indicadores da loja Hashtag&Drink no último ano.
# Obs: faça tudo usando variáveis.

# Valores do último ano:

# Quantidade de Vendas de Coca = 150
# Quantidade de Vendas de Pepsi = 130
# Preço Unitário da Coca = 1,50
# Preço Unitário da Pepsi = 1,50
# Custo da Loja: 2.500,00

# Use o bloco abaixo para criar todas as variáveis que precisar.

qtd_sales_coca = 150
qtd_sales_pepsi = 130
coca_unit_price = 1.50
pepsi_unit_price = 1.50
store_cost = 2500

# """1. Qual foi o faturamento de Pepsi da Loja?"""

pepsi_billing =  pepsi_unit_price * qtd_sales_pepsi
print(f'faturamento da pepsi {pepsi_billing}')

# """2. Qual foi o faturamento de Coca da Loja?"""

coca_billing = coca_unit_price * qtd_sales_coca
print(f'faturamento da coca {coca_billing}')

# """3. Qual foi o Lucro da loja?"""

total_billing = pepsi_billing + coca_billing
store_profit = total_billing - store_cost
print(f'Lucro da loja {store_profit}')

# """4. Qual foi a Margem da Loja? (Lembre-se, margem = Lucro / Faturamento). Não precisa formatar em percentual"""

store_edge = store_profit / total_billing
print(f'margem da loja {store_edge}')

### Parte 2 - Inputs e Strings

# A maioria das empresas trabalham com um Código para cada produto que possuem. A Hashtag&Drink, por exemplo, tem mais de 1.000 produtos e possui um código para cada produto.
# Ex: 
# Coca -> Código: BEB1300543
# Pepsi -> Código: BEB1300545
# Vinho Primitivo Lucarelli -> Código: BAC1546001
# Vodka Smirnoff -> Código: BAC17675002

# Repare que todas as bebidas não alcóolicas tem o início do Código "BEB" e todas as bebidas alcóolicas tem o início do código "BAC".

# Crie um programa de consulta de bebida que, dado um código qualquer, identifique se a bebida é alcóolica. O programa deve responder True para bebidas alcóolicas e False para bebidas não alcóolicas. Para inserir um código, use um input.

# Dica: Lembre-se do comando in para strings e sempre insira os códigos com letra maiúscula para facilitar.

code = input('Qual é o código do produto ?')
is_alcoholic = 'BAC' in code
print(f'A bebida é alcoolica? {is_alcoholic}')


