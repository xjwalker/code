


# recursion
# [1,2,3,4,5]

def mi_function(): # LINEA POR LINEA
    numberos = [1,2,3,4,5] # 15

    acum = 0
    for num in numberos:
        acum = acum + num

    print(acum)


def mi_function_recursiva(numberos): # necesitan un caso base: detenie la ejecucion de la funcion
    if len(numberos) == 0: # 5
        return 0

    numbero_actual = numberos.pop() # saca el ultimo elemento de la lista. # 5

    return mi_function_recursiva(numberos) + numbero_actual

# [1,2,3,4,5] = len = 5

# valor = parse()
# if(valor) # if(parse()

# call

# if    #parse

# recursion: rescursion: recursion:

# call stack <--
# recursion # [1, 2, 3, 4, 5] =    15
# rescursion [1,2,3,4] = 10 + 5 : 15
# rescursion [1,2,3] = 6 + 4 : 6
# rescursion [1,2] = 3 + 3  : 3
# rescursion [1] = 0 + 1 : 1
# rescursion [] = 0      : 0


if __name__ == '__main__':
    # mi_function()
    numberos = [1,2,3,4,5] # 5, 4 , 3...
    suma  = mi_function_recursiva(numberos)
    print(suma)
