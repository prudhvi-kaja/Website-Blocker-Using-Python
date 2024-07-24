# Website Blocker Script

## Overview

This Python script allows you to manage the blocking and unblocking of websites by modifying the hosts file on your computer. This can be useful for parental controls, productivity purposes, or simply for testing.

## Features

- **Display Blocked Websites**: Lists all the currently blocked websites.
- **Block a Website**: Adds a specified website to the hosts file to block it.
- **Unblock a Website**: Removes a specified website from the hosts file to unblock it.

## Requirements

- Python 3.x
- Administrator/Superuser privileges (required to modify the hosts file)
- Script should be run from `C:` directory on Windows

## How It Works

The script modifies the `hosts` file of your operating system to block or unblock websites. The `hosts` file is located at different paths depending on the OS:
- Windows: `C:\Windows\System32\drivers\etc\hosts`
- Unix/Linux/Mac: `/etc/hosts`

If the hosts file is not accessible or does not exist, the script will use a test file (`test_hosts.txt`) for demonstration purposes.

## Usage

### Running the Script

1. **Ensure Script is in C: Directory (Windows)**:
   - The script should be placed in the `C:` directory. This is because administrative permissions are more effectively managed when the script is run from this location.

2. **Run Command Prompt as Administrator**:
   - Open the Start menu.
   - Type `cmd`.
   - Right-click on `Command Prompt` and select `Run as administrator`.

3. **Navigate to C: Directory (if not already there)**:
   ```bash
   cd C:\
   ```

4. **Run the Script**:
   ```bash
   python website_blocker.py
   ```

### Choosing an Option

- **Display blocked websites**: View all the currently blocked websites.
- **Block a website**: Enter the URL of the website you want to block.
- **Unblock a website**: Enter the URL of the website you want to unblock.
- **Exit**: Terminate the script.

### Post Blocking/Unblocking

After blocking or unblocking a website, restart your browser to apply the changes.

## Functions

### `extract_domain(url)`

Extracts the domain from a given URL.

- **Parameters**: `url` (str): The URL from which to extract the domain.
- **Returns**: `str`: The extracted domain.

### `display_blocked_websites()`

Displays the list of currently blocked websites by reading the hosts file.

### `block_website(website)`

Blocks a specified website by adding an entry to the hosts file.

- **Parameters**: `website` (str): The website to block.

### `unblock_website(website)`

Unblocks a specified website by removing the corresponding entry from the hosts file.

- **Parameters**: `website` (str): The website to unblock.

### `main()`

Main function that provides a menu for the user to interact with the script.

## Permissions

Since modifying the hosts file requires administrative privileges, you may need to run the script with elevated permissions:
- On Windows, run the command prompt as an administrator.
- On Unix/Linux/Mac, use `sudo` to run the script.

## Debugging

The script includes print statements for debugging purposes, which provide feedback on the operations being performed, such as extracting domains and blocking/unblocking websites.

## Disclaimer

Be cautious when modifying the hosts file, as incorrect entries can affect your internet connectivity. Always make a backup of the hosts file before making changes.

## License

This script is provided "as is" without any warranty. Use it at your own risk.
