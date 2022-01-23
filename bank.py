class Bank:
    def __init__(self, name, balance = 0):
        self.__name = name
        self.__balance = balance
        
    def deposit(self, add_money):
        if add_money > 0:
            self.__balance = self.__balance + add_money             
        
    def withdraw(self, spend_money):
        if spend_money < self.__balance:
            self.__balance = self.__balance - spend_money
 
    def __str__(self):
        return (self.__name) +", you" + " have $" + str(self.__balance) + " available in your account."

myAccount = Bank('Kalle', 20)
myAccount.deposit(10) 
myAccount.withdraw(5)
print(myAccount)