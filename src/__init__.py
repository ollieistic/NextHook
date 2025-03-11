from pystyle import Colorate, Colors, Center
from colorama import Fore, init
import requests
import time
import os

# Clear Terminal Function
def clear():
    if os.name == "nt": # Windows
        os.system('cls')
    elif os.name == "posix": # Linux
        os.system('clear')
    else:
        input("You are using an unsupported operating system. Press ENTER to exit.")


# Set Terminal Title Function
def title(name):
    os.system(f'title {name}')


# ASCII
ascii = r"""
███╗   ██╗███████╗██╗  ██╗████████╗██╗  ██╗ ██████╗  ██████╗ ██╗  ██╗
████╗  ██║██╔════╝╚██╗██╔╝╚══██╔══╝██║  ██║██╔═══██╗██╔═══██╗██║ ██╔╝
██╔██╗ ██║█████╗   ╚███╔╝    ██║   ███████║██║   ██║██║   ██║█████╔╝ 
██║╚██╗██║██╔══╝   ██╔██╗    ██║   ██╔══██║██║   ██║██║   ██║██╔═██╗ 
██║ ╚████║███████╗██╔╝ ██╗   ██║   ██║  ██║╚██████╔╝╚██████╔╝██║  ██╗
╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝

"""

banner = Center.XCenter(ascii) # Center ASCII banner

def print_banner():
    print(Colorate.Vertical(Colors.blue_to_cyan, banner)) # Color and print ASCII banner


# Choices
choices = """
[01] > Send Message     [02] > Delete Webhook       [03] > Spam Webhook
[04] > Coming Soon      [05] > Source Code          [06] > Exit
"""

choices = Center.XCenter(choices) # Center choices

def print_choices():
    print(Colorate.Horizontal(Colors.blue_to_cyan, choices))


# Socials
socials = f"~ GitHub: @ollieistic | Discord: @ollieistic | YouTube: @ollieistic ~"

socials = Center.XCenter(socials) # Center socials

def print_socials():
    print(socials)


# NextHook is open-source but falls under the GNU GPL-v3 license. Few things to note:

# - You are free to use, modify, and distribute this code as long as you provide proper attribution and use the same license.
# - You are not allowed to use this code for commercial purposes (cannot sell).
# - You are not allowed to remove the license from this code.
# - You are not allowed to hold the author liable for any damages caused by this code.
# - You are not allowed to sublicense this code.
# - You are not allowed to use this code for illegal purposes.