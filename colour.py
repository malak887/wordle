import colorama
from colorama import Fore,Back,Style
colorama.init(autoreset=True)
def colouring(input_char, output,col):
    if col=="green":
        output +=(Fore.GREEN + input_char +   
        Style.RESET_ALL)
    elif col=="yellow":
         output +=(Fore.YELLOW + input_char +   
        Style.RESET_ALL)
    

    return output

