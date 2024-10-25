class BankAccount:
    def __init__(self, account_holder, balance=0, category="Standard"):
        self.account_holder = account_holder  # Public attribute
        self.__balance = balance  # Private attribute
        self.__category = category  # Private attribute for account category
        self.__withdrawal_limit = self.__set_withdrawal_limit()  # Private method to set withdrawal limit based on category

    def __set_withdrawal_limit(self):
        """Private method to set withdrawal limits based on account category"""
        if self.__category == "Standard":
            return 500
        elif self.__category == "Premium":
            return 1000
        elif self.__category == "Gold":
            return 5000
        else:
            return 300  # Default limit for undefined categories

    def deposit(self, amount):
        """Deposit money into the account"""
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance: {self.__balance}")
        else:
            print("Deposit amount must be positive!")

    def withdraw(self, amount):
        """Withdraw money from the account"""
        if 0 < amount <= self.__balance and amount <= self.__withdrawal_limit:
            self.__balance -= amount
            print(f"Withdrew {amount}. New balance: {self.__balance}")
        elif amount > self.__withdrawal_limit:
            print(f"Cannot withdraw more than your limit of {self.__withdrawal_limit}!")
        else:
            print("Insufficient balance or invalid amount!")

    def get_balance(self):
        """Check the account balance"""
        return self.__balance

    def get_account_info(self):
        """Get account details including category and limits"""
        return f"Account holder: {self.account_holder}, Category: {self.__category}, Withdrawal limit: {self.__withdrawal_limit}"

    def transfer_to(self, receiver, amount):
        if self.__balance >= amount and amount >= 0:
            self.withdraw(amount)
            receiver.deposit(amount)
        else:
            print("Error")

# Inherited Account Classes
class StandardAccount(BankAccount):
    def __init__(self, account_holder, balance=0):
        super().__init__(account_holder, balance, category="Standard")


class PremiumAccount(BankAccount):
    def __init__(self, account_holder, balance=0):
        super().__init__(account_holder, balance, category="Premium")

    def __set_withdrawal_limit(self):
        """Override to set a higher withdrawal limit for Premium"""
        return 1000  # Custom limit for premium accounts


class GoldAccount(BankAccount):
    def __init__(self, account_holder, balance=0):
        super().__init__(account_holder, balance, category="Gold")

    def __set_withdrawal_limit(self):
        """Override to set an even higher withdrawal limit for Gold"""
        return 5000  # Custom limit for gold accounts


# Card Class
class Card:
    def __init__(self, card_holder, card_type, account):
        self.card_holder = card_holder
        self.card_type = card_type
        self.account = account

    def get_card_info(self):
        """Get information about the card and associated account"""
        return f"Card Holder: {self.card_holder}, Card Type: {self.card_type}, Account Info: {self.account.get_account_info()}"


def transfer_money(sender, receiver, amount):
    if sender.get_balance() >= amount and amount >= 0:
        sender.withdraw(amount)
        receiver.deposit(amount)
    else:
        print("Error")



# Example usage
standard_account = StandardAccount("Alice", 1000)
premium_account = PremiumAccount("Bob", 2000)
gold_account = GoldAccount("Charlie", 5000)

# Creating cards for each account
standard_card = Card("Alice", "Debit", standard_account)
premium_card = Card("Bob", "Credit", premium_account)
gold_card = Card("Charlie", "Gold", gold_account)

eli = gold_account
bob = premium_account
#transfer_money(eli,bob,1000)
eli.transfer_to(bob, 1000)