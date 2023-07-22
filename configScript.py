import os
import sys
import ctypes
import click
import json
import time
import winreg

def main():

    repository_url = 'https://github.com/LopezIgnacio2201/appBlocker'
    click.echo("Welcome! Before starting, be sure to read the README on GitHub.")
    print()
    click.echo(f"To view the README, click on the link below or copy and paste it into your browser (Or CTRL + click):")
    click.echo(repository_url)
    print()
    input("Press enter to start.")
    os.system('cls')
    print("Running checks...")
    time.sleep(2)

    if not checkExplorer():
        print("Creating explorer and disallowrun keys.")
        time.sleep(1)
        createExplorer()
        time.sleep(4)
        createDisallowRun()
    else:
        print("Keys already created, proceeding.")
        print()

    if not checkScriptAdded():
        print("Adding program to startup.")
        time.sleep(1)
        addScriptStartUp()
    else:
        print("Program already on startup.")
        print()

    print("Checks done succesfully, proceeding to configuration.")
    input("Press enter to start.")
    os.system('cls')

    timer_data = get_timer()
    
    print("Timer succesful.")
    time.sleep(2)
    os.system('cls')

    blocked_app = addProgramToBlock()
    print("App succesfully added.")

    config_data = load_from_json("json/config.json")
    if "apps" not in config_data:
        config_data["apps"] = []  # Create an empty list for apps if it doesn't exist

    new_app_config = {
        "name": blocked_app["name"],
        "status": blocked_app["status"],
        "timer": timer_data
    }

    config_data["apps"].append(new_app_config)  # Add the new app config to the list

    save_to_json(config_data, "json/config.json")
    os.system('cls')
    print("Configuration succesfully added.")


def save_to_json(data, file_path):
    try:
        with open(file_path, 'w') as json_file:
            json.dump(data, json_file, indent=4)
    except Exception as e:
        print(f"Error. {e}")
        os._exit(1)

def load_from_json(file_path):
    try:
        if os.path.exists(file_path):
            with open(file_path, 'r') as json_file:
                return json.load(json_file)
    except Exception as e:
        print(f"Error: {e}")
    return {}  # Return an empty dictionary if the file doesn't exist or there's an error



# checks if explorer key is created
def checkExplorer():

    try:
        key_path = r"SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\explorer"
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_READ)
        print("explorer key found.")
        time.sleep(2)
        return True
    except FileNotFoundError:
        print("explorer key not found.")
        time.sleep(2)
        return False

    
# check if the script is added to startup
def checkScriptAdded():
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Run", 0, winreg.KEY_READ)

    try:
        value, _ = winreg.QueryValueEx(key, "silentMode.py")
        return True
    except WindowsError:
        return False
    finally:
        winreg.CloseKey(key)

# get timer from user
def get_timer():
    timer = {}
    timer["hours"] = int(input("Enter the number of hours: "))
    timer["minutes"] = int(input("Enter the number of minutes: "))
    timer["seconds"] = int(input("Enter the number of seconds: "))

    return timer

    
# get app to block
def addProgramToBlock():

    print("Enter the name of the program to block (Read README): ")

    app = {}
    app["name"] = input()
    app["status"] = 0

    return app



# FUNCTION CALLS TO OTHER SCRIPTS ---------------------------------------------------------

def createExplorer():
    if sys.platform == 'win32':
        script = os.path.abspath('configScripts/createExplorer.py')
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, script, None, 1)


def createDisallowRun():
    if sys.platform == 'win32':
        script = os.path.abspath('configScripts/createDisallowRun.py')
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, script, None, 1)


def addScriptStartUp():
    if sys.platform == 'win32':
        script = os.path.abspath('configScripts/addScriptStartUp.py')
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, script, None, 1)


if __name__ == "__main__":
    main()