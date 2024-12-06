# Bank User Management System

## Table of contents
- [Description](#description)
- [Features](#features)
- [Installation Instructions](#installation-instructions)
- [Usage Instructions](#usage-instructions)
  - [Example Commands](#example-commands)
- [Dependencies](#dependencies)
  - [Python 3.x:](#python-3x)
  - [colored:](#colored)
- [Author](#author)
- [Collaborators](#collaborators)
  

## Description
The Bank User Management System is a Python application that allows users to manage their bank accounts effectively. Users can create accounts, deposit and withdraw funds, view account details, and compound interest on their accounts.

## Features
- User registration and account management
- Deposit and withdrawal functionality
- Interest compounding for savings and checking accounts
- User-friendly console interface

## Installation Instructions
1. Ensure you have Python 3.x installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).
2. Clone this repository to your local machine using:
   ```bash
   git clone https://github.com/yourusername/bank-user-management-system.git
   ```
3. Navigate to the project directory:
   ```bash
   cd bank-user-management-system
   ```
4. To use this app it requires external packages which should be run in a virtual environment. To create a virtual environment enter:
   ```bash
   python -m venv .venv
   ```
5. Activate the virtual environment:
   ```bash
   source .venv/bin/activate
   ```
6. Install all the required packages:
   ```bash
   pip install -r requirements.txt
   ```
  For more information about all the dependencies of the app or if you would like to install them individualy go to [dependencies](#dependencies).


## Usage Instructions
1. Run the application by executing the following command in your terminal:
   ```bash
   python main.py
   ```
2. Follow the prompts to choose actions such as depositing or withdrawing funds, or displaying account information.
3. Enter the required information when prompted (e.g., user index, account index, and amount).

### Example Commands
- **Deposit Funds:**
  - Choose action (1)
  
  ![deposit step 1](/images/deposit_feature1.png)

  - Enter user index (e.g., 0 for John Doe)
  
  ![deposit step 2](/images/deposit_feature2.png)

  - Enter account index (0 for checking)
  
  ![deposit step 3](/images/deposit_feature3.png) 

  - Enter amount to deposit (e.g., 500.00)
  
  ![deposit step 4](/images/deposit_feature4.png) 

  - If successful you will get a message:
  
  ![deposit success](/images/deposit_feature5.png) 

- **Withdraw Funds:**
  - Choose action (2)
  
  ![withdraw step 1](/images/withdraw_feature1.png)

  - Enter user index (e.g., 1 for Sue Doe)
  
  ![withdraw setp 2](/images/withdraw_feature2.png)

  - Enter account index (1 for savings)
  
  ![withdraw step 3](/images/withdraw_feature3.png)

  - Enter amount to withdraw (e.g., 200.00)
  
  ![withdraw step 4](/images/withdraw_feature4.png)

  - If successful you will get a message:

  ![withdraw success](/images/withdraw_feature5.png)

- **Show Accounts:**
  - Choose action (3)
  
  ![show accounts step 1](/images/show_accounts_feature1.png)

  - Enter user index (e.g., 0 for John Doe) to display accounts.

  ![](/images/show_accounts_feature2.png)

  - User selected will have accounts displayed:

  ![show accounts successful](/images/show_accounts_feature3.png)


## Dependencies
### Python 3.x: 
Any version of Python 3 will suffice.

### colored
  Official documentation: [colored](https://pypi.org/project/colored/)

  An external library for color and formatting in terminal. For this project it will help differentiate and highlight some important user prompts, messages for errors, successful operations and outputs. 

  To install colored enter in the command line:
  ```bash
  pip install colored
  ```
 Make sure to have your [virtual environment](#installation-instructions) activated when doing this.

 #### Usage
 Colors are imported in a seperate module (colors.py) and then stored as f string to be called upon later
 ```py
 from colored import Fore, Back, Style

 propmt_color: str = f"{Back.red}"
 reset: str = f"{Style.reset}"
 ```
 In the main module (main.py) the strings are imported

 ```py
 from colors import prompt_color, reset

 action = input(f"{propmt_color}Choose an action:{reset}\n(1) Deposit (2) Withdraw (3) Show Accounts (4) Add User (5) Exit:\n")
 ```
#### Output  
![colored example](/images/colored_example.png)

Here the prompt we want to highlight is red.

## Author
[Declan Whitty](https://github.com/declan-whitty)# bank-user-management-system

## Collaborators
[Earvin Tumpao](https://github.com/earvin-tech)