from src import *

# Send Message Function
def send_message(webhook):
    clear()
    title("NextHook - Send Message")
    print_banner()

    message = input("message@NEXTHOOK > Enter message: ").strip()

    data = {
        'content': message
    }

    response = requests.post(webhook, json=data)

    if response.status_code == 204: # Successful request
        print(f"\n[{Fore.GREEN}+{Fore.RESET}] Message sent successfully.")
    else: # Unsuccessful request
        print(f"\n[{Fore.RED}-{Fore.RESET}] Failed to send message.")


# Delete Webhook Function
def delete_webhook(webhook):
    clear()
    title("NextHook - Delete Webhook")
    print_banner()

    response = requests.delete(webhook)

    if response.status_code == 204: # Successful request
        print(f"\n[{Fore.GREEN}+{Fore.RESET}] Webhook deleted successfully.")
    else: # Unsuccessful request
        print(f"\n[{Fore.RED}-{Fore.RESET}] Failed to delete webhook.")


# Spam Webhook Function
def spam_webhook(webhook):
    clear()
    title("NextHook - Spam Webhook")
    print_banner()

    message = input("spam@NEXTHOOK > Enter message: ").strip() # Message to send
    amount = int(input("spam@NEXTHOOK > Enter amount: ").strip()) # Amount of messages to send

    print() # New line

    data = {
        'content': message
    }

    # For loop to send multiple messages
    for i in range(amount):
        response = requests.post(webhook, json=data)

        if response.status_code == 204: # Successful request
            print(f"[{Fore.GREEN}+{Fore.RESET}] Message {i+1} sent successfully.")
        else: # Unsuccessful request
            print(f"[{Fore.RED}-{Fore.RESET}] Failed to send message {i+1}.")


# Not tested - might come in future updates
def rename_webhook(webhook):
    clear()
    title("NextHook - Rename Webhook")
    print_banner()

    name = input("rename@NEXTHOOK > Enter new name: ").strip()

    data = {
        'name': name
    }

    response = requests.patch(webhook, json=data)

    if response.status_code == 200: # Successful request
        print(f"\n[{Fore.GREEN}+{Fore.RESET}] Webhook renamed successfully.")
    else: # Unsuccessful request
        print(f"\n[{Fore.RED}-{Fore.RESET}] Failed to rename webhook.")
