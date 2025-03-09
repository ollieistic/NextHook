from src import *
from src.webhook import *

# Initialize colorama with autoreset
init(autoreset=True)

webhook_url = None

# Login function
def login():
    global webhook_url  # Use the global webhook_url variable
    clear()
    title("NextHook - Login")
    print_banner()

    webhook_url = input("login@NEXTHOOK > Enter Webhook URL: ").strip()
    response = requests.get(webhook_url)
    if response.status_code == 200 and "discord.com" in response.url: # Successful request and Discord URL
        print(f"\n[{Fore.GREEN}+{Fore.RESET}] Webhook URL is valid. Logging in...")
        time.sleep(1) # Wait for 1 second
    else: # Unsuccessful request or invalid URL
        print(f"\n[{Fore.RED}-{Fore.RESET}] Invalid webhook URL. Exiting...")
        time.sleep(2) # Wait for 2 seconds
        exit() # Exit the program

# Call login function
login()

# Program
while True:
    clear() # Clear terminal
    title("NextHook - Menu") # Set terminal title
    print_banner()  # Print banner
    print_socials() # Print socials
    print_choices() # Print choices
    print() # New line

    choice = input("menu@NEXTHOOK > Choice: ").strip() # User input

    # Choice handler
    if choice == "1":
        send_message(webhook_url)
    elif choice == "2":
        delete_webhook(webhook_url)
    elif choice == "3":
        spam_webhook(webhook_url)
    elif choice == "4":
        print("Coming soon...")
    elif choice == "5":
        print() # New line
        print(f"[{Fore.GREEN}+{Fore.RESET}] NextHook's source code can be found here: https://github.com/ollieistic/NextHook")
    elif choice == "6":
        exit()
    else:
        print(f"[{Fore.RED}-{Fore.RESET}] Invalid choice. Please try again.")
    
    input("\nPress ENTER to return.") # Press ENTER to re-run the program