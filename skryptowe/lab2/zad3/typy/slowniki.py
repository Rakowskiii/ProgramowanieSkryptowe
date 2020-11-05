from . import slownik
def zapisz():
    for i in input().split():
        try:
            a = int(i)
            try:
                slownik[a]+=1
            except:
                slownik[a] = 1
        except:
            pass

def wypisz():
    for i in slownik.items():
        print(f"{i[0]}:{i[1]}")

