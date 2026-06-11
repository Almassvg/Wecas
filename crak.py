import os
import sys
import time

# Function to clear the Termux screen
def clear_screen():
    os.system('clear')

# ANSI Color Codes for styling
GREEN = "\033[92m"
CYAN = "\033[96m"
WHITE = "\033[97m"
RED = "\033[91m"
RESET = "\033[0m"

# Function to display the TARGET CRACK ASCII logo
def show_logo():
    clear_screen()
    print(f"{CYAN}=================================================={RESET}")
    print(f"{CYAN}  _______  ___   ____    ____  _______ ______   {RESET}")
    print(f"{CYAN} /__   __|/ _ \ |  _ \  / ___||  ____/|__  __|  {RESET}")
    print(f"{CYAN}    | |  / /_\ \| |_) || |  _ | |__      | |     {RESET}")
    print(f"{CYAN}    | |  |  _  ||  _  /| | |_||  __|     | |     {RESET}")
    print(f"{CYAN}    | |  | | | || | \ \| |__| | |____    | |     {RESET}")
    print(f"{CYAN}    |_|  |_| |_||_|  \_\\____/|______|   |_|     {RESET}")
    print(f"                                                ")
    print(f"   {RED}____  ____    _     ____  _  __{RESET}")
    print(f"  {RED}/ ___||  _ \  / \   / ___|| |/ /{RESET}")
    print(f" {RED}| |    | |_) |/ _ \ | |    | ' / {RESET}")
    print(f" {RED}| |___ |  _  / ___ \| |___ | . \ {RESET}")
    print(f"  {RED}\____||_| \_/_/   \_\____||_|\_\ {RESET}")
    print(f"                                          ")
    print(f"               {GREEN}TARGET CRACK TOOLS{CYAN}")
    print(f"{CYAN}=================================================={RESET}")

# Function to handle the main interactive menu
def show_menu():
    while True:
        show_logo()
        print(f"{WHITE}[1] Start Script{RESET}")
        print(f"{RED}[0] Exit{RESET}")
        print(f"{CYAN}--------------------------------------------------{RESET}")
        
        choice = input(f"{GREEN}Enter your choice (0/1): {RESET}").strip()
        
        if choice == '1':
            print(f"\n{GREEN}[*] Launching script... please wait...{RESET}")
            time.sleep(1.5)
            clear_screen()
            
            # Finds the directory of the executable
            script_dir = os.path.dirname(os.path.abspath(__file__))
            main_binary_path = os.path.join(script_dir, "target")
            
            # Automatically runs the compiled binary './target'
            if os.path.exists(main_binary_path):
                # Giving execution permission just in case, then running it
                os.system(f"chmod +x {main_binary_path}")
                os.system(f"{main_binary_path}")
            else:
                print(f"{RED}[!] Error: 'target' executable not found in this folder!{RESET}")
                time.sleep(3)
            break
        elif choice == '0':
            print(f"\n{RED}[!] Exiting... Goodbye!{RESET}\n")
            sys.exit()
        else:
            print(f"\n{RED}[!] Invalid choice! Please enter 1 or 0.{RESET}")
            time.sleep(1.5)

if __name__ == "__main__":
    try:
        show_menu()
    except KeyboardInterrupt:
        print(f"\n\n{RED}[!] Script interrupted and stopped.{RESET}\n")
        sys.exit()
