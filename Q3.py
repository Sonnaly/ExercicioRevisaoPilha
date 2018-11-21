def pop(lista):
    return lista.pop()

def push(lista,v):

    if(len(lista) < 10):
        lista.append(v)
        return "ADICIONE ELEMENTO"
    else:
        return "NAO FOI POSSIVEL ADICIONAR"

def topo(lista):
    return lista[len(lista)-1]

def isEmpty(lista):
    if(len(lista) == 0):
        return True
    return False


lista = [1,2,3,4,5]

print(push(lista,1))
