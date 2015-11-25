balance = 0

def make_account():
    return ("balance" : 0)

def deposit(amount):
    global balance
    balance += amount
    return balance

def withdraw(amount):
    global balance
    balance -= amount
    return balance
