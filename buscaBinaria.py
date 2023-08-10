import pandas as pd

#------------------------------------------------------------------------------------------------------------------------------

dataset = pd.read_excel('Vendas.xlsx')
companylist = dataset['Valor Final']
lista_numeros = []
for i, num  in enumerate(companylist):
    lista_numeros.append(int(num))

#------------------------------------------------ busca binaria ----------------------------------------------------------------

def binary_search_strings(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1  # Elemento não encontrado

#------------------------------------------------ bucket sort------------------------------------------------------------------

def bucket_sort(arr):
    max_value = max(arr)
    min_value = min(arr)
    
    bucket_size = (max_value - min_value) // len(arr) + 1
    bucket_count = (max_value - min_value) // bucket_size + 1
    
    buckets = [[] for _ in range(bucket_count)]
    
    for num in arr:
        bucket_index = (num - min_value) // bucket_size
        buckets[bucket_index].append(num)
    
    for i in range(bucket_count):
        insertion_sort(buckets[i])
    
    sorted_arr = []
    for bucket in buckets:
        sorted_arr += bucket
    
    index = binary_search_strings(sorted_arr, 1000)
    if index != -1:
        print(f"{index} é o endereço do elemento, resultado de uma busca binária")
       # print(sorted_arr[-1])
    else:
        print(f"Element not found")

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key_item = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key_item:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key_item


#------------------------------------------------ chamando funções ----------------------------------------------------------------

bucket_sort(lista_numeros)
