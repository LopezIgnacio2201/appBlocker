import winreg
import os
import sys
import time 


# create explorer key and dword DisallowRun
def createExplorer():
    key_path = r"SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\explorer"
    value_name = "DisallowRun"
    value_data = 1

    print("Creating explorer key and DisallowRun dword.")
    time.sleep(2)

    try:
        explorer_key = winreg.CreateKey(winreg.HKEY_CURRENT_USER, key_path)
        winreg.SetValueEx(explorer_key, value_name, 0, winreg.REG_DWORD, value_data)

        print("Key succesfully created.")
        time.sleep(2)
    except Exception as e:
        print(F"Error creating the key. {e}")
        input("Press enter.")

if __name__ == "__main__":
    createExplorer()