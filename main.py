

class BankAccount:
    def __init__(self, holder, balance):
        self.AccountHolder = holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount

    def get_balance(self):
        print(f"Balance: {self.balance}")


def transfer_money(sender, receiver, amount):
    if sender.balance >= amount and amount >= 0:
        sender.balance -= amount
        receiver.balance += amount
    else:
        print("Error")


b1 = BankAccount("eli", 1000)
b2 = BankAccount("bob", 3000)
transfer_money(b1, b2, 2022)

print(b1.balance)
print(b2.balance)
