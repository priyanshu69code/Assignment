import winreg
import os

# Revert Objective 2: Unblock USB Ports
def unblock_usb_ports():
    key_path = r'SYSTEM\\CurrentControlSet\\Services\\USBSTOR'
    key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key_path, 0, winreg.KEY_WRITE)
    winreg.SetValueEx(key, 'Start', 0, winreg.REG_DWORD, 3)  # Set 'Start' value back to 3
    winreg.CloseKey(key)

# Revert Objective 2: Enable Bluetooth
def enable_bluetooth():
    key_path = r'SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\ActionCenter\\Quick Actions\\All\\SystemSettings_Device_BluetoothQuickAction'
    key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key_path, 0, winreg.KEY_WRITE)
    winreg.SetValueEx(key, 'Type', 0, winreg.REG_DWORD, 0)  # Set 'Type' value back to 0
    winreg.CloseKey(key)

# Revert Objective 2: Allow Command Prompt
def allow_command_prompt():
    key_path = r'Software\\Policies\\Microsoft\\Windows\\System'
    key = winreg.CreateKey(winreg.HKEY_CURRENT_USER, key_path)
    winreg.SetValueEx(key, 'DisableCMD', 0, winreg.REG_DWORD, 0)
    winreg.CloseKey(key)

# Revert Objective 3: Unblock "facebook.com"
def unblock_facebook():
    hosts_path = r'C:\\Windows\\System32\\drivers\\etc\\hosts'
    try:
        with open(hosts_path, 'r') as hosts_file:
            lines = hosts_file.readlines()
        
        with open(hosts_path, 'w') as hosts_file:
            for line in lines:
                if not line.strip().endswith('facebook.com'):
                    hosts_file.write(line)
    except FileNotFoundError:
        pass  # Ignore if the hosts file doesn't exist

if __name__ == "__main__":
    try:
        # Revert the security measures
        unblock_usb_ports()
        enable_bluetooth()
        allow_command_prompt()
        unblock_facebook()
        
        print("Security measures reverted successfully.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
    
    input("Press Enter to exit...")
