'''
The colored package is used to bring more color to the printed outputs of the app on the terminal. It helps to differentiate different outputs such as different accounts (savings or checking) and to highlight important prompts of inputs. 
'''

from colored import Fore, Back, Style # type: ignore

# Different colors to call for printing on console
error_color: str = f"{Back.red}{Style.underline}{Style.bold}"
reset: str = f"{Style.reset}"
checking_account_color: str = f"{Back.blue}"
saving_account_color: str = f"{Back.yellow}"
propmt_color: str = f"{Back.red}"
successful_input_color: str = f"{Back.green}"