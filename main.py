# Import json
import json
# Import colors.py
from colors import error_color, reset, checking_account_color, saving_account_color, propmt_color, successful_input_color

'''
The purpose of the account class is to store information such as balance of account, its ID, and account type. It's methods will perform operations on the balance.

Attributes:
- account_type: can be checking or savings
- id: unique ID for the account
- balance: Stores balance of the account
- rate: determined depending on the account_type

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
            # Prints if valid withdrawal
            print(f"\n{successful_input_color}Withdrawal successful{reset}\n") 
        else:
            # Prints if not valid amount
            print(f"\n{error_color}Invalid withdrawal amount.{reset}")
             

    def compound(self):
        # Multiplies rate to account
        self.balance *= self.rate 

    def __str__(self):
        # When returning the instance f string returned
        return f"ID: {self.id} {self.account_type.capitalize()} Account: ${self.balance:.2f}" 

'''
The purpose of the User class is to store user information such as their name and date of birth, 
and to manage their associated accounts. Users can perform operations on their accounts such as 
adding accounts, depositing, withdrawing, viewing account details, and applying interest rates.

Attributes:
- firstname: First name of the user
- lastname: Last name of the user
- dobm, dobd, doby: Month, day, and year of the user's date of birth
- accounts: A list storing the user's accounts

Methods:
- add_account: Creates and adds a new account (checking or savings) for the user
- deposit: Deposits a specified amount into a specific user account
- withdraw: Withdraws a specified amount from a specific user account
- get_accounts: Displays all the user's accounts with details
- compound_accounts: Applies interest rates to all the user's accounts
'''
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

    '''
    Adds a new account (either 'checking' or 'savings') to the user's accounts.

    Parameters:
    - account_type (str): The type of account to create ('checking' or 'savings').
    - id (str): A unique identifier for the account.
    '''
    def add_account(self, account_type, id):
        account = Account(account_type, id)  
        self.accounts.append(account)  

    '''
    Deposits a specified amount into the user's account at the given index.

    Parameters:
    - amount (float): The amount to deposit.
    - ind (int): The index of the account in the user's accounts list.
    '''
    def deposit(self, amount, ind):
        try:
            if 0 <= ind < len(self.accounts):  
                self.accounts[ind].deposit(amount)  
            else:
                print(f"{error_color}Invalid account index.{reset}")  
        except Exception as e:
            print(f"{error_color}Error occurred: {e}{reset}")

    '''
    Withdraws a specified amount from the user's account at the given index.

    Parameters:
    - amount (float): The amount to withdraw.
    - ind (int): The index of the account in the user's accounts list.
    '''
    def withdraw(self, amount, ind):
        try:
            if 0 <= ind < len(self.accounts):  
                self.accounts[ind].withdraw(amount)  
            else:
                print(f"{error_color}Invalid account index.{reset}")  
        except Exception as e:
            print(f"{error_color}Error occurred: {e}{reset}")
    
    '''
    Prints all the user's accounts with details.
    Displays the user's name and each account's information with corresponding color
    based on account type.
    '''
    def get_accounts(self):
        print(f"{self.firstname} {self.lastname}")  
        for account in self.accounts:
            if account.account_type == "savings":
                print(f"{saving_account_color}{account}{reset}")
            elif account.account_type == "checking":
                print(f"{checking_account_color}{account}{reset}")

    '''
    Applies the interest rate to all the user's accounts.
    Calls the compound method on each account.
    '''
    def compound_accounts(self):
        for account in self.accounts:
            account.compound()

# Helper function to load data from a JSON file
# This function reads the contents of a specified JSON file.
# If the file does not exist or contains invalid JSON, it handles the error gracefully.
def load_data(filename):
    try:
        with open(filename, 'r') as file:
            return json.load(file)  # Load and return the JSON data
    except FileNotFoundError:
        return []  # Return an empty list if the file does not exist
    except json.JSONDecodeError:
        print("Error reading JSON file. Starting fresh.")  # Notify user of a JSON error
        return []

# Helper function to save data to a JSON file
# This function writes the provided data into a specified JSON file.
# It ensures the JSON data is formatted for readability with indentation.
def save_data(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)  # Save data to the file with indentation

# Convert client objects into JSON-compatible data
# This function takes a list of User objects and converts them into a format that can be saved as JSON.
# Each user and their accounts are represented as nested dictionaries.
def convert_clients_to_json(clients):
    json_data = []
    for client in clients:
        client_data = {
            'firstname': client.firstname,
            'lastname': client.lastname,
            'dobm': client.dobm,
            'dobd': client.dobd,
            'doby': client.doby,
            'accounts': [
                {
                    'account_type': account.account_type,
                    'id': account.id,
                    'balance': account.balance
                }
                for account in client.accounts
            ]
        }
        json_data.append(client_data)
    return json_data

# Convert JSON data back into client objects
# This function takes a list of dictionaries from a JSON file and converts them into User objects with Account objects.
# It handles cases where the JSON data might contain empty or invalid entries.
def convert_json_to_clients(data):
    clients = []
    for user_data in data:
        if user_data is None:  # Skip invalid or empty data
            continue
        user = User(
            user_data['firstname'],
            user_data['lastname'],
            user_data['dobm'],
            user_data['dobd'],
            user_data['doby']
        )
        for account_data in user_data['accounts']:
            account = Account(
                account_data['account_type'],
                account_data['id'],
                account_data['balance']
            )
            user.accounts.append(account)  # Add accounts to the user
        clients.append(user)
    return clients

# Load existing client data from a JSON file
# This step initializes the application with data from the 'users.json' file, if it exists.
clients_data = load_data('users.json')
clients = convert_json_to_clients(clients_data)

# Main function to run the banking application
# This function provides a menu-driven interface for the user to interact with the application.
# Users can perform actions like depositing, withdrawing, viewing accounts, adding new users, or exiting.
def main():
    while True:
        # Display menu options to the user
        action = input(f"{propmt_color}Choose an action:{reset}\n(1) Deposit (2) Withdraw (3) Show Accounts (4) Add User (5) Exit:\n") 
        print()
        if action == "1":
            # Handle deposit operation
            if len(clients) == 0:
                print(f"{error_color}No users available. Please add a user first.{reset}\n")
                continue
            user_index = int(input(f"{propmt_color}Enter user index:{reset} "))  
            print()
            if 0 <= user_index < len(clients): 
                account_index = int(input(f"{propmt_color}Enter account index (0 for checking, 1 for savings):{reset}")) 
                amount = float(input(f"\n{propmt_color}Enter amount to deposit:{reset} ")) 
                clients[user_index].deposit(amount, account_index) 
                print(f"\n{successful_input_color}Deposit successful{reset}\n") 
            else:
                print(f"{error_color}Invalid user index.{reset}\n") 
        elif action == "2":
            # Handle withdrawal operation
            if len(clients) == 0:
                print(f"{error_color}No users available. Please add a user first.{reset}\n")
                continue
            user_index = int(input(f"{propmt_color}Enter user index:{reset} "))
            print()
            if 0 <= user_index < len(clients): 
                account_index = int(input(f"{propmt_color}Enter account index (0 for checking, 1 for savings):{reset} ")) 
                amount = float(input(f"\n{propmt_color}Enter amount to withdraw:{reset} "))
                clients[user_index].withdraw(amount, account_index) 
                # print(f"\n{successful_input_color}Withdrawal successful{reset}\n") 
            else:
                print(f"{error_color}Invalid user index.{reset}\n") 
        elif action == "3": 
            # Handle displaying account information
            if len(clients) == 0:
                print(f"{error_color}No users available.{reset}\n")
                continue
            user_index = int(input(f"{propmt_color}Enter user index:{reset} ")) 
            print()
            if 0 <= user_index < len(clients): 
                clients[user_index].get_accounts() 
                print()
            else:
                print(f"{error_color}Invalid user index.{reset}\n") 
        elif action == "4":
            # Add a new user to the system
            firstname = input(f"{propmt_color}Enter first name:{reset} ")
            lastname = input(f"{propmt_color}Enter last name:{reset} ")
            dobm = int(input(f"{propmt_color}Enter birth month (1-12):{reset} "))
            dobd = int(input(f"{propmt_color}Enter birth day (1-31):{reset} "))
            doby = int(input(f"{propmt_color}Enter birth year (e.g., 1990):{reset} "))
            new_user = User(firstname, lastname, dobm, dobd, doby)
            clients.append(new_user)
            print(f"\n{successful_input_color}User added successfully!{reset}\n")
        elif action == "5":
            # Save data and exit the application
            print(f"{successful_input_color}Saving data...{reset}")
            save_data(convert_clients_to_json(clients), 'users.json')
            print(f"{successful_input_color}Data saved. Exiting the system.{reset}") 
            break
        else:
            # Handle invalid menu selection
            print(f"{error_color}Invalid choice. Please try again.{reset}") 

# Call the main function to start the program
main()