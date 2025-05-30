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
            print(f"[{Fore.GREEN}+{Fore.RESET}] Message {i+1} sent successfully!")
        else: # Unsuccessful request
            print(f"[{Fore.RED}-{Fore.RESET}] Failed to send message {i+1}.")


# Rename Webhook Function
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


# Change Webhook Avatar Function
def change_webhook_avatar(webhook):

    image_url = input("avatar@NEXTHOOK > Enter Image URL: ")

    try:
        # Get the image
        response = requests.get(image_url)
        if response.status_code != 200:
            print(f"[{Fore.RED}-{Fore.RESET}] Failed to download image. Status Code: {response.status_code}")
            return

        # Convert image to base64
        image_data = base64.b64encode(response.content).decode('utf-8')
        
        # Guess image type from headers
        content_type = response.headers.get('Content-Type', '')
        if 'png' in content_type:
            image_type = 'png'
        elif 'jpeg' in content_type or 'jpg' in content_type:
            image_type = 'jpeg'
        else:
            print(f"\n[{Fore.RED}-{Fore.RESET}] Unsupported image format. Please use PNG or JPEG.")
            return

        avatar_data = f"data:image/{image_type};base64,{image_data}"

        # Send PATCH request to Discord webhook
        payload = {
            "avatar": avatar_data
        }

        r = requests.patch(webhook, json=payload)
        if r.status_code == 200:
            print(f"\n[{Fore.GREEN}+{Fore.RESET}] Webhook avatar updated successfully!")
        else:
            print(f"\n[{Fore.RED}-{Fore.RESET}] Failed to update avatar. Status Code: {r.status_code}.")

    except Exception as e:
        print()
        print(f"An error occurred: {e}")
