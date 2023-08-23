# Security Measures Automation

This Python script is designed to automate various security measures on a Windows system. It provides functionalities to block USB ports, disable Bluetooth, restrict the Command Prompt, and block access to specific websites like "facebook.com" by modifying the Windows Registry and Hosts file.

## Usage

Before running this script, it's essential to take some precautions:

1. **Disable Antivirus**: Temporarily disable your antivirus software as it might interfere with the script's ability to make changes to system settings.

2. **Run as Administrator**: To make changes to the Windows Registry, run the script as an administrator. Right-click on the script file and select "Run as administrator" from the context menu.

**Warning**: Be extremely cautious when modifying the Windows Registry. Incorrect changes can lead to system issues, and it is recommended to create backup copies of registry keys before making any changes. Ensure that your code adheres to best practices and security considerations.

## Functionality

### Block USB Ports

This script can block USB ports by modifying a Registry key:

```python
block_usb_ports()
```

### Disable Bluetooth

You can disable Bluetooth on your system with this function:

```python
disable_bluetooth()
```

### Restrict the Command Prompt

To restrict the Command Prompt, use this function:

```python
restrict_command_prompt()
```

### Block Access to "facebook.com"

The script can block access to specific websites, like "facebook.com," by modifying the Hosts file:

```python
block_facebook()
```

## Reverting Changes

If you need to revert all the changes made by this script, you can use the provided "revert_changes" folder. Inside this folder, you will find a script or instructions to reverse the security measures applied by this script.

**Note**: Always use the revert option carefully, and ensure you have backups of your system settings before making any changes.

## Running the Script

1. Download the script file to your system.

2. Disable your antivirus temporarily.

3. Right-click on the script file and select "Run as administrator."

4. The script will apply the selected security measures, and you will receive a success message.

5. Press Enter to exit the script.

Please use this script responsibly and only on systems you have permission to modify.
