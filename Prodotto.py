class Prodotto:

    def __init__(self, productID,
                 productName,
                 handInStock,
                 costPrice):
        super().__init__()
        self.productID = productID
        self.productName = productName
        self.handInStock = handInStock
        self.costPrice = costPrice

    productID  = ""
    productName = ""
    handInStock = 0
    costPrice = 0.0

    def stampa(self):
        print(self.productID,
              self.productName,
              self.handInStock,
              self.costPrice)

    def valoreTotale (self):
        tot=self.handInStock+self.costPrice
