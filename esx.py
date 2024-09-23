import os

# ANSI color codes for styling
A = '\x1b[1;97m'   # White
A16 = '\x1b[1;92m\x1b[38;5;208m'   # Orange and Green combo
A22 = '\x1b[38;5;46m'   # Green
BLUE_LIGHT = '\x1b[38;5;87m'  # Light Blue
GREEN = '\x1b[38;5;82m'  # Green

# Banner function to display welcome message with logo
def banner():
    os.system('clear')
    print(f"{BLUE_LIGHT}    ██╗░░██╗░█████╗░███╗░░██╗██╗███████╗")
    print(f"{BLUE_LIGHT}    ██║░░██║██╔══██╗████╗░██║██║██╔════╝")
    print(f"{BLUE_LIGHT}    ███████║███████║██╔██╗██║██║█████╗░░")
    print(f"{BLUE_LIGHT}    ██╔══██║██╔══██║██║╚████║██║██╔══╝░░")
    print(f"{BLUE_LIGHT}    ██║░░██║██║░░██║██║░╚███║██║██║░░░░░")
    print(f"{BLUE_LIGHT}   ╚═╝ ░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝╚═╝╚═╝░░░░░")
    print(f"{GREEN}==============================")
    print(f"{A16}   WELCOME TO HANIFx TERMUX TOOL")
    print(f"{GREEN}==============================")

# Function to run shell commands
def run_command(command):
    result = os.system(f'sh -c "{command}"')
    if result != 0:
        print(f"{A16}Error executing: {command}")

# Function to uninstall pip package
def pip_uninstall(package_name):
    run_command(f'pip uninstall -y {package_name}')
    print(f"{A16}{package_name} uninstalled successfully!")

# Function to uninstall pkg package
def pkg_uninstall(package_name):
    run_command(f'pkg uninstall -y {package_name}')
    print(f"{A16}{package_name} uninstalled successfully!")

# Menu function for Termux setup
def menu():
    os.system('clear')
    banner()
    print(f"{GREEN} [1] Update & Upgrade Termux")
    print(f"{BLUE_LIGHT} [2] Install Python and Pip")
    print(f"{GREEN} [3] Install Metasploit")
    print(f"{BLUE_LIGHT} [4] Install Ngrok")
    print(f"{GREEN} [5] Install Basic Utilities")
    print(f"{BLUE_LIGHT} [6] Install Extra Pip Modules")
    print(f"{GREEN} [7] Install Hanifx Package")
    print(f"{BLUE_LIGHT} [8] Uninstall a Pip Package")
    print(f"{GREEN} [9] Uninstall a Pkg Package")
    print(f"{A16} [00/X] EXIT ")

    choice = input(f"{BLUE_LIGHT}Select an option: ")

    if choice == '1':
        if confirm_action("update and upgrade Termux"):
            run_command('pkg update -y && pkg upgrade -y')
            print(f"{BLUE_LIGHT}Termux updated and upgraded successfully!")
    elif choice == '2':
        run_command('pkg install python -y && pkg install python-pip -y')
        print(f"{BLUE_LIGHT}Python and Pip installed successfully!")
    elif choice == '3':
        run_command('pkg install unstable-repo -y && pkg install metasploit -y')
        print(f"{BLUE_LIGHT}Metasploit installed successfully! To run: msfconsole")
    elif choice == '4':
        run_command('wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-arm.zip && unzip ngrok-stable-linux-arm.zip && mv ngrok $HOME')
        print(f"{BLUE_LIGHT}Ngrok installed! Use './ngrok authtoken [YOUR_AUTH_TOKEN]' to set up.")
    elif choice == '5':
        run_command('pkg install git -y && pkg install curl -y && pkg install wget -y && pkg install nano -y && pkg install openssh -y && pkg install zip -y && pkg install unzip -y')
        print(f"{BLUE_LIGHT}Basic utilities installed successfully!")
    elif choice == '6':
        additional_packages = [
            'aiohappyeyeballs',
            'aiohttp',
            'aiohttp-retry',
            'aiosignal',
            'anyio',
            'attrs',
            'beautifulsoup4',
            'bs4',
            'certifi',
            'chardet',
            'charset-normalizer',
            'colorama',
            'frozenlist',
            'h11',
            'hanifx',
            'html5lib',
            'httpcore',
            'httpx',
            'idna',
            'lolcat',
            'markdown-it-py',
            'mdurl',
            'mechanize',
            'multidict',
            'Pygments',
            'PyJWT',
            'pyotp',
            'python-telegram-bot',
            'requests',
            'rich',
            'setuptools',
            'six',
            'sniffio',
            'soupsieve',
            'twilio',
            'urllib3',
            'webencodings',
            'yarl'
        ]
        for package in additional_packages:
            run_command(f'pip install {package}')
        print(f"{A16}All additional pip modules installed successfully!")
    elif choice == '7':
        run_command('pip install hanifx')
        print(f"{BLUE_LIGHT}Hanifx package installed successfully!")
    elif choice == '8':
        package_name = input(f"{A16}Enter the pip package name to uninstall: ")
        pip_uninstall(package_name)
    elif choice == '9':
        package_name = input(f"{BLUE_LIGHT}Enter the pkg package name to uninstall: ")
        pkg_uninstall(package_name)
    elif choice in ['00', 'X', 'x']:
        print(f"{A16}Exiting... Goodbye!")
        exit()
    else:
        print(f"{BLUE_LIGHT}Invalid choice! Try again.")
        menu()

# Confirmation function
def confirm_action(action):
    confirm = input(f"{A16}Are you sure you want to {action}? (y/n): ")
    return confirm.lower() == 'y'

# Run the menu
menu()
