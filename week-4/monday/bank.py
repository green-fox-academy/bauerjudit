class Bank_account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def pay(self, amount):
        self.balance -= amount

    def receive(self, amount):
        self.balance += amount

    def current_balance(self):
        print("balance of ")
        print(self.name)
        print("is")
        print(self.balance)

    def transfer(self, other_account, amount):
        self.pay(amount)
        other_account.receive(amount)


szamla = Bank_account("Bela", 1000)
feri = Bank_account("Feri", 7000000)

szamla.transfer(feri, 10000)



szamla.pay(50)
szamla.receive(100)
szamla.current_balance()
