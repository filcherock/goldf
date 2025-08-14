"""
GOLDF EXPLORER V0.0.1
filcher, 2025 Copyright
"""

import os

from colorama import *

def main():
    os.system('clear')
    # os.system('cls') <- For Windows
    print(Fore.BLACK + Back.WHITE + os.getcwd() + Fore.RESET + Back.RESET)
    elements = os.listdir()
    sorted_elements = sorted(elements, key=lambda x: (not os.path.isdir(x), x.startswith('.'), x.lower()))
    for element in sorted_elements:
        if os.path.isdir(element):
            print(f"{Fore.CYAN}[DIR]{Fore.RESET} {element}")
        else:
            print(f"{Fore.YELLOW}[FILE]{Fore.RESET} {element}")
    while True:
        path = input(os.getcwd() + ": ").lower()
        try:
            if path == "..":
                os.chdir("..")
                main()
            elif path == ":cdir:":
                try:
                    dirName = input("Enter directory name: ")
                    path = os.path.join(os.getcwd(), dirName)
                    os.mkdir(path)
                    main()
                except FileExistsError:
                    print(Fore.RED + "[ERROR] This folder has already been created" + Fore.RESET)
            elif path == ":cfile:":
                    fileName = input("Enter file name: ")
                    if os.path.exists(fileName):
                        print(Fore.RED + "[ERROR] This folder has already been created" + Fore.RESET)
                    else:
                        file = open(fileName, "w")
                        file.close()                  
            else:
                print(path[0])
                os.chdir(path)
                main()
        except FileNotFoundError:
            print(Fore.RED + "[ERROR] File or Directory not found" + Fore.RESET)
        except PermissionError:
            print(Fore.RED + "[ERROR] You do not have access to this file or directory." + Fore.RESET)
        except NotADirectoryError:
            print(Fore.RED + "[ERROR] This is file." + Fore.RESET)

if __name__ == '__main__':
    main()