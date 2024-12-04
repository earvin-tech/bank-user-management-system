#Import colors.py
from colors import error_color, reset, checking_account_color, saving_account_color, propmt_color, successful_input_color

'''
The purpose of the account class is to store information such as balance of account, its ID, and account type. It's methods will perform operations on the balance.

Methods: 
- deposit: When called will add an amount user inputs to the current balance
- withdraw: When called will subtract an amount user inputs from the current balance
- compound: when called will apply the rate already determined when instance of the account is created (checking or savings). Rate is applied by multiplying the current balance by the rate.
'''
class Account:
    # Initialising the parameters of the class
    def __init__(self, account_type, id, balance=0.0): 
        # 'checking', 'savings', etc.
        self.account_type = account_type  
        # Balance of the account
        self.balance = balance 
        # Account ID
        self.id = id 
        # Determines rates for checking and savings accounts
        self.rate = 1.03 if account_type == 'checking' else 1.05 

    def deposit(self, amount): 
        # Checks for valid deposit amount, must be positive
        if amount > 0:  
            # Adds input to current balance
            self.balance += amount 
        else:
            # Prints if not valid
            print(f"{error_color}Deposit amount must be positive.{reset}") 

    def withdraw(self, amount): 
        # Checks for valid withdrawl amount, must be positive
        if 0 < amount <= self.balance: 
            # Subtracts input amount from balance
            self.balance -= amount
        else:
            # Prints if not valid amount
            print(f"{error_color}Invalid withdrawal amount.{reset}") 

    def compound(self):
        # Multiplies rate to account
        self.balance *= self.rate 

    def __str__(self):
        # When returning the instance f string returned
        return f"ID: {self.id} {self.account_type.capitalize()} Account: ${self.balance:.2f}" 

class User:
    # Initialize a user with first name, last name, and date of birth (month, day, year)
    def __init__(self, firstname, lastname, dobm, dobd, doby):
        # First name of the user
        self.firstname = firstname  
        # Last name of the user
        self.lastname = lastname  
        # Month of the user's date of birth
        self.dobm = dobm  
        # Day of the user's date of birth
        self.dobd = dobd  
        # Year of the user's date of birth
        self.doby = doby  
         # List to store the user's accounts (checking/savings)
        self.accounts = [] 

     # Adds a new account (either 'checking' or 'savings') to the user's accounts
    def add_account(self, account_type, id):
        # Create a new account instance
        account = Account(account_type, id)  
        # Add the account to the user's accounts list
        self.accounts.append(account)  
    # Deposits a specified amount into the user's account at the given index
    def deposit(self, amount, ind):
        
        try:
            # Check if the account index is valid
            if 0 <= ind < len(self.accounts):  
                # Perform the deposit
                self.accounts[ind].deposit(amount)  
            else:
                # Invalid index message
                print(f"{error_color}Invalid account index.{reset}")  
        # Handle any exceptions during the deposit process
        except Exception as e:
            
            print(f"{error_color}Error occurred: {e}{reset}")

    # Withdraws a specified amount from the user's account at the given index
    def withdraw(self, amount, ind):
        
        try:
            # Check if the account index is valid
            if 0 <= ind < len(self.accounts):  
                # Perform the withdrawal
                self.accounts[ind].withdraw(amount)  
            else:
                # Invalid index message
                print(f"{error_color}Invalid account index.{reset}")  
        # Handle any exceptions during the withdrawal process
        except Exception as e:
            
            print(f"{error_color}Error occurred: {e}{reset}")
    
    # Prints all the user's accounts with details
    def get_accounts(self):
        # Display the user's name
        print(f"{self.firstname} {self.lastname}")  
        # Display each account with corresponding color based on account type
        for account in self.accounts:
            
            if account.account_type == "savings":
                print(f"{saving_account_color}{account}{reset}")
            elif account.account_type == "checking":
                print(f"{checking_account_color}{account}{reset}")

    # Applies the interest rate to all the user's accounts
    def compound_accounts(self):
        
        # Call the compound method for each account
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
        # Asks user to choose action from main menu
        action = input(f"{propmt_color}Choose an action:{reset}\n(1) Deposit (2) Withdraw (3) Show Accounts (4) Exit:\n") 
        print()
        # Selecting 1 is to deposit
        if action == "1": 
            # Limit user input to existing users
            user_index = int(input(f"{propmt_color}Enter user index:{reset} "))  
            print()
            # Checks for valid user within the index of all users
            if 0 <= user_index < len(clients): 
                # Asks for checking or savings account to deposit into
                account_index = int(input(f"{propmt_color}Enter account index (0 for checking, 1 for savings):{reset}")) 
                # Asks for amount to deposit from user
                amount = float(input(f"\n{propmt_color}Enter amount to deposit:{reset} ")) 
                # For the relevant user index adds the amount into the account specified before in the inputs
                clients[user_index].deposit(amount, account_index) 
                # Print if successful
                print(f"\n{successful_input_color}Deposit successful{reset}\n") 
            else:
                # Prints if invalid user index is entered by user, returns to main menu.
                print(f"{error_color}Invalid user index.{reset}\n") 
        # Selecting 2 is to withdraw
        elif action == "2":
            user_index = int(input(f"{propmt_color}Enter user index:{reset} "))
            print()
            # Checks for valid user within the index of all users
            if 0 <= user_index < len(clients): 
                # Asks user checking or savings
                account_index = int(input(f"{propmt_color}Enter account index (0 for checking, 1 for savings):{reset} ")) 
                # Asks for amount to withdraw from user
                amount = float(input(f"\n{propmt_color}Enter amount to withdraw:{reset} "))
                # For the relevant user index removes the amount from the account specified before in the inputs
                clients[user_index].withdraw(amount, account_index) 
                # Prints if valid withdrawal
                print(f"\n{successful_input_color}Withdrawal successful{reset}\n") 
            else:
                # Prints if invalid user index
                print(f"{error_color}Invalid user index.{reset}\n") 
        # If user wants to see accounts
        elif action == "3": 
            # Asks user for account index
            user_index = int(input(f"{propmt_color}Enter user index:{reset} ")) 
            print()
            # checks for valid index within index of all users
            if 0 <= user_index < len(clients): 
                # calls get_accounts method
                clients[user_index].get_accounts() 
            else:
                # Prints if user index input is invalid
                print(f"{error_color}Invalid user index.{reset}\n") 
        elif action == "4":
            # Prints after successful exit of app
            print(f"{successful_input_color}Exiting the system.{reset}") 
            break
        else:
            # Prints if user inputs invalid choice
            print(f"{error_color}Invalid choice. Please try again.{reset}") 

# Call the main function to start the program
main()