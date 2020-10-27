def split_numbers(numeros,pares,impares):  
    for num in numeros:
        if num % 2 == 0:
            pares.append(num)
        else:
            impares.append(num)
        

pares = list()
impares = list()
numeros = [2,8,1,-6,25,48]

split_numbers(numeros,pares,impares)