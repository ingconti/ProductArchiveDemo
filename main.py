from Prodotto import Prodotto

with open("Inventory-Records-Sample-Data.csv", "r") as f:
    header = f.readline()
    for riga in f:
        riga        = riga.strip()
        parts       = riga.split(",")
        productID   = parts[0]
        productName = parts[1]
        handInStock = int(parts[2])
        costPrice = int(parts[3])

        p = Prodotto(productID,"|" productName, handInStock, costPrice)
        p.stampa()
        tot = p.valoreTotale()
        print(tot)

