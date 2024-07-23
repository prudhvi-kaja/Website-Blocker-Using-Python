import os
import platform

# Determine the host file path based on the operating system
if platform.system() == "Windows":
    host_path = r"C:\Windows\System32\drivers\etc\hosts"
else:
    host_path = '/etc/hosts'

test_host_path = 'test_hosts.txt'  # For testing purposes

# Check if the hosts file exists, else use the test path
if not os.path.exists(host_path):
    print(f"{host_path} does not exist or is not accessible. Using {test_host_path} for testing.")
    host_path = test_host_path

ip_address = '127.0.0.1'

def extract_domain(url):
    if url.startswith("http://") or url.startswith("https://"):
        domain = url.split("//")[1].split("/")[0]
        print(f"Extracted domain: {domain}")  # Debugging line
        return domain
    return url

def display_blocked_websites():
    print("Blocked websites:")
    if not os.path.exists(host_path):
        print("No blocked websites found.")
        return
    with open(host_path, 'r') as host_file:
        lines = host_file.readlines()
        for line in lines:
            if line.startswith(ip_address):
                print(line.strip())

def block_website(website):
    domain = extract_domain(website)
    print(f"Attempting to block: {domain}")  # Debugging line
    try:
        with open(host_path, 'a+') as host_file:
            host_file.seek(0)
            lines = host_file.readlines()
            if any(domain in line for line in lines):
                print(f"Website '{domain}' is already blocked.")
            else:
                host_file.write(ip_address + " " + domain + '\n')
                print(f"Website '{domain}' has been blocked.")
    except PermissionError:
        print("Permission denied. Please run the script as an administrator.")

def unblock_website(website):
    domain = extract_domain(website)
    print(f"Attempting to unblock: {domain}")  # Debugging line
    if not os.path.exists(host_path):
        print("No blocked websites found.")
        return
    try:
        with open(host_path, 'r') as host_file:
            lines = host_file.readlines()
        with open(host_path, 'w') as host_file:
            for line in lines:
                if not (line.startswith(ip_address) and domain in line):
                    host_file.write(line)
            print(f"Website '{domain}' has been unblocked.")
    except PermissionError:
        print("Permission denied. Please run the script as an administrator.")

def main():
    while True:
        print("\nWebsite Blocker")
        print("1. Display blocked websites")
        print("2. Block a website")
        print("3. Unblock a website")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            display_blocked_websites()
        elif choice == '2':
            website = input("Enter the website to block: ")
            block_website(website)
        elif choice == '3':
            website = input("Enter the website to unblock: ")
            unblock_website(website)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
