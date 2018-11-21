def pop(lista):
    return lista.pop()

def push(lista,v):
    return lista.append(v)

def topo(lista):
    return lista[len(lista)-1]

def isEmpty(lista):
    if(len(lista) == 0):
        return True
    return False

def soma(lista):

    soma = 0

    while(not isEmpty(lista)):
        soma += topo(lista)
        pop(lista)

    return soma

lista = [1,2,3,4,5]

print(soma(lista))
print(isEmpty(lista))
