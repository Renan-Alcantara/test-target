# 3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
# • O menor valor de faturamento ocorrido em um dia do mês;
# • O maior valor de faturamento ocorrido em um dia do mês;
# • Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

# IMPORTANTE:
# a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
# b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;

import json
from xml.dom import minidom

#--------------------------------------------------------------------------

# Trabalhando com .JSON:

print("\n","-"*75,"\n\n","Trabalhando com Arquivo .Json:\n")
with open ("dados.json") as dados:
	mes1 = json.load(dados)
	dias_list =[0]
	valores_list = [0]
	
for dias in mes1:
	valor = dias['valor']
	dia = dias['dia']
	dias_list.insert(0-1,dia)
	valores_list.insert(0-1,valor)

for x, y in enumerate(valores_list):
	if y == max(valores_list):
		print(f"No dia {x+1} foi gerado o valor máximo ({y})")

valores_list_val = []
for valores in valores_list:
    if valores > 0:
        valores_list_val.insert(0-1,valores)

media = sum(valores_list_val)/len(valores_list_val)
print(f"A média de faturamento neste mês foi de {media}")

min_val = min(valores_list_val)
for x, y in enumerate(valores_list):
    if y == min_val:
        print(f"No dia {x+1} foi gerado o valor minimo ({y})")

acima_media=[]
for x, y in enumerate (valores_list):
    if y > media:
        acima_media.insert(0-1,x)
acima_media = len(acima_media)
print(f"Neste mês, houveram {acima_media} dias em que o faturamento obtido foi acima da média")

print("\nATENÇÃO: Os dias em que o faturamento foi 0 (zero) não foram \nconsiderados no calculo da média de faturamento mensal.")

        

#----------------------------------------------------------------------------

# Trabalhando com .XML:

print("\n","-"*75,"\n\n","Trabalhando com Arquivo .xml: \n")
with open ("dados2.xml", "r", encoding='utf-8') as dados2:
	mes2 = minidom.parse(dados2)
	valores2 = mes2.getElementsByTagName("valor")
	valores_list2 = [0]
	
for valor2 in valores2:
	valor_list2 = float(valor2.firstChild.data)
	valores_list2.insert(0-1,valor_list2)
	
for x, y in enumerate(valores_list2):
	if y == max(valores_list2):
		print(f"No dia {x+1} foi gerado o valor máximo ({y})")

valores_list_val2 = []
for valores2 in valores_list2:
    if valores2 > 0:
        valores_list_val2.insert(0-1,valores2)

media2 = sum(valores_list_val2)/len(valores_list_val2)
print(f"A média de faturamento neste mês foi de {media2}")

min_val2 = min(valores_list_val2)
for x, y in enumerate(valores_list2):
    if y == min_val2:
        print(f"No dia {x+1} foi gerado o valor minimo ({y})")

acima_media2=[]
for x, y in enumerate (valores_list2):
    if y > media2:
        acima_media2.insert(0-1,x)
acima_media2 = len(acima_media2)
print(f"Neste mês, houveram {acima_media2} dias em que o faturamento obtido foi acima da média")

print("\nATENÇÃO: Os dias em que o faturamento foi 0 (zero) não foram \nconsiderados no calculo da média de faturamento mensal.")

print("\n","-"*75,"\n")