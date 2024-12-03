from colors import error_color, reset, checking_account_color, saving_account_color, propmt_color, successful_input_color
class Account:
    def __init__(self, account_type, id, balance=0.0): # initialising the parameters of the class
        self.account_type = account_type  # 'checking', 'savings', etc.
        self.balance = balance # balannce of the account
        self.id = id # account id
        self.rate = 1.03 if account_type == 'checking' else 1.05 # rates for checking and savings accounts

    def deposit(self, amount): # deposit method
        if amount > 0:  # checks for valid deposit amount, must be positive
            self.balance += amount # adds input to current balance
        else:
            print(f"{error_color}Deposit amount must be positive.{reset}") # prints if not valid

    def withdraw(self, amount): # withdraw method
        if 0 < amount <= self.balance: # checks for valid withdrawl amount, must be positive
            self.balance -= amount
        else:
            print(f"{error_color}Invalid withdrawal amount.{reset}") # prints if not valid amount

    def compound(self):
        self.balance *= self.rate # assigns rate to account

    def __str__(self):
        return f"ID: {self.id} {self.account_type.capitalize()} Account: ${self.balance:.2f}" # when returning the instance f string returned

class User:
    def __init__(self, firstname, lastname, dobm, dobd, doby):
        # Initialize a user with first name, last name, and date of birth (month, day, year)
        self.firstname = firstname  # First name of the user
        self.lastname = lastname  # Last name of the user
        self.dobm = dobm  # Month of the user's date of birth
        self.dobd = dobd  # Day of the user's date of birth
        self.doby = doby  # Year of the user's date of birth
        self.accounts = []  # List to store the user's accounts (checking/savings)

    def add_account(self, account_type, id):
        # Adds a new account (either 'checking' or 'savings') to the user's accounts
        account = Account(account_type, id)  # Create a new account instance
        self.accounts.append(account)  # Add the account to the user's accounts list

    def deposit(self, amount, ind):
        # Deposits a specified amount into the user's account at the given index
        try:
            if 0 <= ind < len(self.accounts):  # Check if the account index is valid
                self.accounts[ind].deposit(amount)  # Perform the deposit
            else:
                print(f"{error_color}Invalid account index.{reset}")  # Invalid index message
        except Exception as e:
            # Handle any exceptions during the deposit process
            print(f"{error_color}Error occurred: {e}{reset}")

    def withdraw(self, amount, ind):
        # Withdraws a specified amount from the user's account at the given index
        try:
            if 0 <= ind < len(self.accounts):  # Check if the account index is valid
                self.accounts[ind].withdraw(amount)  # Perform the withdrawal
            else:
                print(f"{error_color}Invalid account index.{reset}")  # Invalid index message
        except Exception as e:
            # Handle any exceptions during the withdrawal process
            print(f"{error_color}Error occurred: {e}{reset}")

    def get_accounts(self):
        # Prints all the user's accounts with details
        print(f"{self.firstname} {self.lastname}")  # Display the user's name
        for account in self.accounts:
            # Display each account with corresponding color based on account type
            if account.account_type == "savings":
                print(f"{saving_account_color}{account}{reset}")
            elif account.account_type == "checking":
                print(f"{checking_account_color}{account}{reset}")

    def compound_accounts(self):
        # Applies the interest rate to all the user's accounts
        for account in self.accounts:
            account.compound()  # Call the compound method for each account

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
        action = input(f"{propmt_color}Choose an action:{reset}\n(1) Deposit (2) Withdraw (3) Show Accounts (4) Exit:\n") # Asks user to choose action from main menu
        print()
        if action == "1": # Selecting 1 is to deposit
            user_index = int(input(f"{propmt_color}Enter user index:{reset} "))  # Limit user input to existing users
            print()
            if 0 <= user_index < len(clients): # Checks for valid user within the index of all users
                account_index = int(input(f"{propmt_color}Enter account index (0 for checking, 1 for savings):{reset}")) # Asks for checking or savings account to deposit into
                amount = float(input(f"\n{propmt_color}Enter amount to deposit:{reset} ")) # Asks for amount to deposit from user
                clients[user_index].deposit(amount, account_index) # For the relevant user index adds the amount into the account specified before in the inputs
                print(f"\n{successful_input_color}Deposit successful{reset}\n") # Print if successful
            else:
                print(f"{error_color}Invalid user index.{reset}\n") # Prints if invalid user index is entered by user, returns to main menu.
        elif action == "2":
            user_index = int(input(f"{propmt_color}Enter user index:{reset} "))
            print()
            if 0 <= user_index < len(clients): # Checks for valid user within the index of all users
                account_index = int(input(f"{propmt_color}Enter account index (0 for checking, 1 for savings):{reset} ")) # Asks user checking or savings
                amount = float(input(f"\n{propmt_color}Enter amount to withdraw:{reset} ")) # Asks for amount to withdraw from user
                clients[user_index].withdraw(amount, account_index) # For the relevant user index removes the amount from the account specified before in the inputs
                print(f"\n{successful_input_color}Withdrawal successful{reset}\n") # Prints if valid withdrawal
            else:
                print(f"{error_color}Invalid user index.{reset}\n") # Prints if invalid user index
        elif action == "3": # If user wants to see accounts
            user_index = int(input(f"{propmt_color}Enter user index:{reset} ")) # Asks user for account index
            print()
            if 0 <= user_index < len(clients): # checks for valid index within index of all users
                clients[user_index].get_accounts() # calls get_accounts method
            else:
                print(f"{error_color}Invalid user index.{reset}\n") # Prints if user index input is invalid
        elif action == "4":
            print(f"{successful_input_color}Exiting the system.{reset}") # Prints after successful exit of app
            break
        else:
            print(f"{error_color}Invalid choice. Please try again.{reset}") # Prints if user inputs invalid choice

# Call the main function to start the program
main()