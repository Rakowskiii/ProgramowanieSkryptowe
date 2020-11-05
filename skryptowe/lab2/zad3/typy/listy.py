from . import lista
def zapisz():
    for i in input().split():
        try:
            a = int(i)
            for j in range(0,len(lista)):
                if lista[j][0] == a:
                    lista[j] = (a,lista[j][1]+1)
                    break
            else:
                lista.append((a,1))
        except:
            pass


def wypisz():
    for i in lista:
        print(f"{i[0]}:{i[1]}")
