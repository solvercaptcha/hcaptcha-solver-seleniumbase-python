# print_project_info.py

import colorama
from colorama import Fore, Back, Style

def print_project_info():
    # Инициализация colorama (на Windows требуется, на Unix-подобных системах может не требоваться)
    colorama.init(autoreset=True)
    
    text = r""" _                     _       _                        _                
| |__   ___ __ _ _ __ | |_ ___| |__   __ _    ___  ___ | |_   _____ _ __ 
| '_ \ / __/ _` | '_ \| __/ __| '_ \ / _` |  / __|/ _ \| \ \ / / _ \ '__|
| | | | (_| (_| | |_) | || (__| | | | (_| |  \__ \ (_) | |\ V /  __/ |   
|_| |_|\___\__,_| .__/ \__\___|_| |_|\__,_|  |___/\___/|_| \_/ \___|_|   
                |_|                                                      
"""
    print(Fore.CYAN + "==========================================================================")
    print(Fore.YELLOW + text)
    print(Fore.CYAN + "==========================================================================")
    print(Fore.GREEN + "Version 1.0.0")
    print(Fore.WHITE + "\nEmail: " + Fore.LIGHTMAGENTA_EX + "info@solvecaptcha.com")
    print(Fore.WHITE + "Telegram: " + Fore.LIGHTMAGENTA_EX + "https://t.me/solvecaptcha")
    print(Fore.WHITE + "Site: " + Fore.LIGHTMAGENTA_EX + "https://solvecaptcha.com\n")

if __name__ == "__main__":
    print_project_info()