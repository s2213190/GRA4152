## A bank account has a balance that can be changed by deposits and withdrawals.

class BankAccount:
    
    def __init__(self, initialBalance = 0.0):
        self._balance = initialBalance
     
    

    def addInterest(self, rate) :
        self._balance = self._balance + self._balance * rate / 100.0
    
    def deposit(self, amount) :
        self._balance = self._balance + amount

    def withdraw(self, amount) :
        PENALTY = 10.0
        if amount > self._balance :
            self._balance = self._balance - PENALTY
        else :
            self._balance = self._balance - amount

    def getBalance(self):
        return self._balance

    
## A Portfolio of the above type of bank accounts

class Portfolio:
    
    def __init__(self):
        self._checking = BankAccount()
        self._savings = BankAccount()
        
    def deposit (self,amount,account):    
        if account == "C":
            self._checking.deposit(amount)
        else:
            self._savings.deposit(amount)


    def withdraw(self, amount, account):
        if account == "C":
            self._checking.withdraw(amount)
        else:
            self._savings.withdraw(amount)

            
    def transfer(self, amount, account):
        if account == "C":
            if self._checking.getBalance() >= amount: 
                self._checking.withdraw(amount)
                self._savings.deposit(amount)
            else:
                print("Not enough balance.")
        else:
            if self._savings.getBalance() >= amount: 
                self._savings.withdraw(amount)
                self._checking.deposit(amount)
            else:
                print("Not enough balance.")

    def getBalance(self, account):
        if account == "C":
            return self._checking.getBalance()
        else:
            return self._savings.getBalance()

#TESTING

my_portfolio = Portfolio()
my_portfolio.deposit(199, "C")
my_portfolio.deposit(299, "S")
print(my_portfolio.getBalance("C")) # prints 199
print(my_portfolio.getBalance("S")) # prints 299
my_portfolio.transfer(50, "S")
print(my_portfolio.getBalance("C")) # prints 249
print(my_portfolio.getBalance("S")) # prints 249
my_portfolio.transfer(499, "C") # prints "Not enough balance"
my_portfolio.withdraw(499, "C")
print(my_portfolio.getBalance("C")) # prints 239