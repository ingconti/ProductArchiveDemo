#with open("file.txt", "r") as f:
#    content = f.read()
#    print(content)

tot = 0
maxx = 0
with open("quantita.txt", "r") as f:
    for riga in f:
        riga = riga.strip()
        print(riga)
        valore = int(riga)
        if valore > maxx:
            maxx = valore
        tot+=valore

    print(tot)
    print(maxx)

