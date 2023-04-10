"""
enumerate - enumera iteráveis (índices)
"""
lista = ['Maria','Helena', 'Luiz']
lista.append('João')

lista_enumerada = enumerate(lista)

for item in lista_enumerada:
    print(item)

    '''or 
    
    lista_enumerada = list(enumerate(lista))
    
    print(lista_enumerada)
    
    or
    
    for indice, nome in enumerate(lista)
        print(indice,nome)'''