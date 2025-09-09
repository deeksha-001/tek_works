class bank:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        
    def withdraw(self, amount):
        self.balance -= amount
        
    def get_balance(self):
        print(f"Current balance is {self.balance}.")

account = bank("Deeksha", 1000)
account.deposit(500)
account.withdraw(200)
account.get_balance()