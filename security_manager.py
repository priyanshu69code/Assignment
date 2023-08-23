import winreg
import os

# Objective 2: Block USB Ports
def block_usb_ports():
    key_path = r'SYSTEM\\CurrentControlSet\\Services\\USBSTOR'
    key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key_path, 0, winreg.KEY_WRITE)
    winreg.SetValueEx(key, 'Start', 0, winreg.REG_DWORD, 4)
    winreg.CloseKey(key)

# Objective 2: Disable Bluetooth
def disable_bluetooth():
    key_path = r'SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\ActionCenter\\Quick Actions\\All\\SystemSettings_Device_BluetoothQuickAction'
    key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key_path, 0, winreg.KEY_WRITE)
    winreg.SetValueEx(key, 'Type', 0, winreg.REG_DWORD, 1)
    winreg.CloseKey(key)

# Objective 2: Restrict the Command Prompt
def restrict_command_prompt():
    key_path = r'Software\\Policies\\Microsoft\\Windows\\System'
    key = winreg.CreateKey(winreg.HKEY_CURRENT_USER, key_path)
    winreg.SetValueEx(key, 'DisableCMD', 0, winreg.REG_DWORD, 1)
    winreg.CloseKey(key)

# Objective 3: Block Access to "facebook.com"
def block_facebook():
    hosts_path = r'C:\\Windows\\System32\\drivers\\etc\\hosts'
    with open(hosts_path, 'a') as hosts_file:
        hosts_file.write('127.0.0.1 facebook.com\n')

if __name__ == "__main__":
    try:
        # Run the security measures
        block_usb_ports()
        disable_bluetooth()
        restrict_command_prompt()
        block_facebook()
        
        print("Security measures applied successfully.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
    
    input("Press Enter to exit...")
