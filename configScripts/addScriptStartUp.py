import os
import time
import win32com.client


def addScriptStartUp():
    print("Getting path of program.")
    time.sleep(1)
    executable_path = os.path.abspath("silentMode.exe")  

    if not os.path.isabs(executable_path):
        executable_path = os.path.abspath(os.path.join(os.getcwd(), executable_path))

    startup_folder = os.path.join(os.environ["APPDATA"], "Microsoft", "Windows", "Start Menu", "Programs", "Startup")
    shortcut_path = os.path.join(startup_folder, "silentMode.lnk")

    # Create a shortcut to the executable in the startup folder
    if not os.path.exists(shortcut_path):
        shell = win32com.client.Dispatch("WScript.Shell")
        shortcut = shell.CreateShortCut(shortcut_path)
        shortcut.Targetpath = executable_path
        shortcut.WorkingDirectory = os.path.dirname(executable_path)
        shortcut.IconLocation = executable_path
        shortcut.save()

if __name__ == "__main__":
    addScriptStartUp()