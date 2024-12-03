from colored import Fore, Back, Style # type: ignore

# Different colors to call for printing on console
error_color: str = f"{Back.red}{Style.underline}{Style.bold}"
reset: str = f"{Style.reset}"
checking_account_color: str = f"{Back.blue}"
saving_account_color: str = f"{Back.yellow}"
propmt_color: str = f"{Back.red}"
successful_input_color: str = f"{Back.green}"