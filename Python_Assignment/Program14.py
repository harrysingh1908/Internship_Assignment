class BankAccount:
   

    def __init__(self, account_holder, initial_balance=0):
        
        self.account_holder = account_holder
        self.balance = initial_balance

    def deposit(self, amount):
        
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}")
            else:
                print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")

    def check_balance(self):
        
        print(f"Current balance: ${self.balance:.2f}")

# Example usage
account = BankAccount("John Doe", 100)
account.check_balance()
account.deposit(50)
account.withdraw(30)
account.withdraw(200)
account.check_balance()
