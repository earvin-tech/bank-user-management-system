from colors import error_color, reset
class Account:
    def __init__(self, account_type, id, balance=0.0):
        self.account_type = account_type  # 'checking', 'savings', etc.
        self.balance = balance
        self.id = id
        self.rate = 1.03 if account_type == 'checking' else 1.05

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            print(f"{error_color}Deposit amount must be positive.{reset}")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
        else:
            print(f"{error_color}Invalid withdrawal amount.{reset}")

    def compound(self):
        self.balance *= self.rate

    def __str__(self):
        return f"ID: {self.id} {self.account_type.capitalize()} Account: ${self.balance:.2f}"

class User:
    def __init__(self, firstname, lastname, dobm, dobd, doby):
        self.firstname = firstname
        self.lastname = lastname
        self.dobm = dobm
        self.dobd = dobd
        self.doby = doby
        self.accounts = []

    def add_account(self, account_type, id):
        account = Account(account_type, id)
        self.accounts.append(account)

    def deposit(self, amount, ind):
        try:
            if 0 <= ind < len(self.accounts):
                self.accounts[ind].deposit(amount)
            else:
                print(f"{error_color}Invalid account index.{reset}")
        except Exception as e:
            print(f"{error_color}Error occurred: {e}{reset}")

    def withdraw(self, amount, ind):
        try:
            if 0 <= ind < len(self.accounts):
                self.accounts[ind].withdraw(amount)
            else:
                print(f"{error_color}Invalid account index.{reset}")
        except Exception as e:
            print(f"{error_color}Error occurred: {e}{reset}")

    def get_accounts(self):
        print(f"{self.firstname} {self.lastname}")
        for account in self.accounts:
            print(account)

    def compound_accounts(self):
        for account in self.accounts:
            account.compound()

# Initialize empty list to store clients' classes
clients = []

clients.append(User('John', 'Doe', 1, 15, 1990))
clients[0].add_account('checking', '000001')
clients[0].add_account('savings', '000002')

clients.append(User('Sue', 'Doe', 2, 22, 1985))
clients[1].add_account('checking', '000003')
clients[1].add_account('savings', '000004')

clients.append(User('Bob', 'Saget', 5, 17, 1956))
clients[2].add_account('checking', '000005')
clients[2].add_account('savings', '000006')

# Main program function
def main():
    while True:
        action = input("Choose an action: (1) Deposit (2) Withdraw (3) Show Accounts (4) Exit:\n")
        print()
        if action == "1":
            user_index = int(input("Enter user index: "))  # Limit user input to existing users
            print()
            if 0 <= user_index < len(clients):
                account_index = int(input("Enter account index (0 for checking, 1 for savings): "))
                amount = float(input("Enter amount to deposit: "))
                clients[user_index].deposit(amount, account_index)
            else:
                print(f"{error_color}Invalid user index.{reset}")
        elif action == "2":
            user_index = int(input("Enter user index: "))
            print()
            if 0 <= user_index < len(clients):
                account_index = int(input("Enter account index (0 for checking, 1 for savings): "))
                amount = float(input("Enter amount to withdraw: "))
                clients[user_index].withdraw(amount, account_index)
            else:
                print(f"{error_color}Invalid user index.{reset}")
        elif action == "3":
            user_index = int(input("Enter user index: "))
            print()
            if 0 <= user_index < len(clients):
                clients[user_index].get_accounts()
            else:
                print(f"{error_color}Invalid user index.{reset}")
        elif action == "4":
            print("Exiting the system.")
            break
        else:
            print(f"{error_color}Invalid choice. Please try again.{reset}")

# Call the main function to start the program
main()