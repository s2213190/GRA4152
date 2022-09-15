class customer: 
    
    def __init__(self):
        self._accumulation = 0 

    def getAccumulation(self):
        return self._accumulation

    def makePurchase(self, amount):

        ## keep adding amount until discount is reached

        if not self.discountReacher():
            self._accumulation = self._accumulation + amount
        
        ##  reduce amount as the discount levels have reached

        else:
            amount = amount - 10
            self._accumulation = amount

    def discountReacher(self):
        if self._accumulation <= 100:
            return False
        else:
            print("You got discount!")
            return True


customer1 = customer()

customer1.makePurchase(200) 
print(customer1.getAccumulation()) # prints 200

customer1.makePurchase(200) 

print(customer1.getAccumulation()) # prints 190

customer1.makePurchase(10)
customer1.makePurchase(20)
