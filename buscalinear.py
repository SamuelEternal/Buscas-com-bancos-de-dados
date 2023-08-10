import pandas as pd

#------------------------------------------------------------------------------------------------------------------------------

dataset = pd.read_excel('Vendas.xlsx')
companylist = dataset['Valor Final']
lista_numeros = []
for i, num  in enumerate(companylist):
    lista_numeros.append(int(num))


#------------------------------------------------ busca linear -----------------------------------------------------------------

def linear_search(arr, target):
    for i, num  in enumerate(arr):
        if num == target:
            return i, num
        
    print("não encontrado")

print(f'{linear_search(lista_numeros, 1000)} resultado da busca linear')
