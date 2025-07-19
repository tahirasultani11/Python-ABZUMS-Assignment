class BankAccount:
    # Class attribute
    bank_name = "First National Bank"
    
    def __init__(self, account_holder: str, initial_balance: float = 0.0):
        self.account_holder = account_holder
        self.balance = initial_balance
        self.transactions = []

    def deposit(self, amount: float) -> None:
        if self.validate_amount(amount):
            self.balance += amount
            self.transactions.append(f"Deposit: +${amount}")
            print(f"${amount} deposited. New balance: ${self.balance}")
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount: float) -> None:
        if self.validate_amount(amount) and amount <= self.balance:
            self.balance -= amount
            self.transactions.append(f"Withdrawal: -${amount}")
            print(f"${amount} withdrawn. New balance: ${self.balance}")
        else:
            print("Invalid withdrawal amount")
    def show_transactions(self) -> None:
        print(f"Transactions for {self.account_holder}")
        for transaction in self.transactions:
            print(transaction)
    
    def __str__(self) -> str:
        return f"Account Holder: {self.account_holder}, Balance: ${self.balance}"

    @classmethod
    def change_bank_name(cls, new_name: str) -> None:
        cls.bank_name = new_name

    @staticmethod
    def validate_amount(amount: float) -> bool:
        return amount > 0
# Test your code here
# Create accounts
account1 = BankAccount("Alice", 1200)
account2 = BankAccount("Bob", 500)

# Perform transaction
account1.deposit(200)
account2.withdraw(100)

# Change bank name
BankAccount.change_bank_name("New Bank Name")

# Print accounts
print(account1)
print(account2)

# Validate amounts
print(BankAccount.validate_amount(100))  # True
print(BankAccount.validate_amount(-50))  # False

# Show transactions
account1.show_transactions()
account2.show_transactions()
class SavingsAccount(BankAccount):
    def __init__(self, account_holder: str, initial_balance: float = 0.0, interest_rate: float = 0.01):
        # Initialize parent class and add new attribut       
        super().__init__(account_holder, initial_balance)
        self.interest_rate = interest_rate
    
    def add_interest(self) -> None:
        # Calculate and deposit interest
        interest = self.balance * self.interest_rate
        self.deposit(interest)
        print(f"interest of ${interest} added. New balance: ${self.balance}")
    
    def __str__(self) -> str:
        # Enhanced string representation
        return f"{super().__str__()}, Interest Rate: {self.interest_rate * 100}%"
    
savings = SavingsAccount("Charlie", 1000, 0.05)
savings.deposit(500)
savings.add_interest()
print(savings)