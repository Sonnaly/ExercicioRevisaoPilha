def pop(lista):
    return lista.pop()

def push(lista,v):

    for i in range(len(lista)):
        if(lista[i] == v):
            return "IMPOSSIVEL ADICIONAR ELEMENTO"

    return lista.append(v)

def topo(lista):
    return lista[len(lista)-1]

def isEmpty(lista):
    if(len(lista) == 0):
        return True
    return False


lista = [1]

print(push(lista,1))
