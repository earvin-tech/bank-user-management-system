'''
The colored package is used to bring more color to the printed outputs of the app on the terminal. It helps to differentiate different outputs such as different accounts (savings or checking) and to highlight important prompts of inputs. 
'''

from colored import Fore, Back, Style # type: ignore

# Different colors to call for printing on console
# Color of error message
error_color: str = f"{Back.red}{Style.underline}{Style.bold}"
# Shortcut for style reset
reset: str = f"{Style.reset}"
# Color of checking account info
checking_account_color: str = f"{Back.blue}"
# Color of saving account info
saving_account_color: str = f"{Back.yellow}"
# Color of prompt message
propmt_color: str = f"{Back.red}"
# Color of successful operation
successful_input_color: str = f"{Back.green}"