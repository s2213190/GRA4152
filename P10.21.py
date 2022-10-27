#  This module defines several classes that implement a banking account class hierarchy.
## A bank account has a balance and a mechanism for applying interest or fees at the end of the month.

class BankAccount :
    
## Constructs a bank account with zero balance.
    def __init__(self):
        self._balance = 0.0

   ## Makes a deposit into this account.
   #  @param amount the amount of the deposit
   #
    def deposit(self, amount):
        self._balance = self._balance + amount
   
   ## Makes a withdrawal from this account, or charges a penalty if
   #  sufficient funds are not available.
   #  @param amount the amount of the withdrawal
   #
    def withdraw(self, amount):
        if amount > self._balance:
            print("Low Balance")
        else:
            self._balance = self._balance - amount
   
#    ## Carries out the end of month processing that is appropriate
#    #  for this account.
#    #
#     def monthEnd(self):
#         return None
   
   ## Gets the current balance of this bank account.
   #  @return the current balance
   #
    def getBalance(self):
        return self._balance
      
## A savings account earns interest on the minimum balance.

class SavingsAccount(BankAccount) :
   ## Constructs a savings account with a zero balance.
   #
    def __init__(self):
        super().__init__()
        self._interestRate = 0.0
        self._minBalance = 0.0

   ## Sets the interest rate for this account.
   #  @param rate the monthly interest rate in percent
   #
    def setInterestRate(self, rate):
        self._interestRate = rate

   ## Overrides superclass method.
   #
    def withdraw(self, amount):
        super().withdraw(amount)
        balance = self.getBalance()
        if balance < self._minBalance:
            self._minBalance = balance

   ## Overrides superclass method.
   #
    def monthEnd(self):
        interest = self._minBalance * self._interestRate / 100
        self.deposit(interest)
        self._minBalance = self.getBalance()
      
      
## A checking account has a limited number of free deposits and withdrawals.
#
class CheckingAccount(BankAccount) :
   ## Constructs a checking account with a zero balance.
   #
    def __init__(self):
        super().__init__()
        self._freeTransactions = 3
        self._FeePerTransaction = 1

    def getFees(self):
        if self._freeTransactions < 0:
            super().withdraw(self._FeePerTransaction)
        
   ## Overrides superclass method.### P10.21 requires that we modify the withdraw and deposit method to allow only 3 free transactions
   ## Also included an additional method of getFees that is invoked in the withdraw and deposit method

    def withdraw(self, amount):
        super().withdraw(amount)  
        self._freeTransactions = self._freeTransactions -1
        self.getFees()
            
    def deposit(self,amount):
        DEPOSIT_FEE=1
        super().deposit(amount)
        self._freeTransactions = self._freeTransactions -1
        self.getFees() 
            
## Overrides superclass method.

    def monthEnd(self):
        self._freeTransactions = 3   #Every MonthEnd the transactions are set back to 3
      

### Testing CODE
C1 = CheckingAccount()
C1.deposit(100)
C1.withdraw(20)
C1.withdraw(30)
C1.deposit(100) 

C1.getBalance()  # Expected answer is 149