import getopt, sys
from typy import listy
from typy import slowniki
argv = sys.argv[1:]
opts, args = getopt.getopt(argv,"",longopts=['modul='])

if opts[0][0] == "--modul":
    if opts[0][1] == 'lista':
        listy.zapisz()
        listy.wypisz()
    if opts[0][1] == 'slownik':
        slowniki.zapisz()
        slowniki.wypisz()