import time
import winreg

# create disallowrun key
def createDisallowRun():
    
    print("Creating DisallowRun key.")
    time.sleep(2)

    key_path = r"SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\explorer\DisallowRun"

    try:
        with winreg.CreateKey(winreg.HKEY_CURRENT_USER, key_path) as key:
            print("DisallowRun key created succesfully.")
            time.sleep(2)

    except Exception as e:
        print(f"Error creating the subkey. {e}")

if __name__ == "__main__":
    createDisallowRun()