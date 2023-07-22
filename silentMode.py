import json
import time
import winreg
import psutil
import re
import datetime
import os

def main():

    config_data = load_from_json("json/config.json")

    if "apps" in config_data and isinstance(config_data["apps"], list):
        current_date = datetime.date.today().strftime("%Y-%m-%d")

        for app in config_data["apps"]:
            app_name = app.get("name", "")
            timer_in_seconds = time_to_seconds(app.get("timer", {}))
            last_used_date = app.get("last_used_date", "")

            if app_name and timer_in_seconds > 0:
                if current_date != last_used_date:
                    # Reset timer for a new day
                    app["timer"]["remaining_seconds"] = timer_in_seconds
                    app["last_used_date"] = current_date
                    unblock_app()
                    save_to_json(config_data, "json/config.json")

                if app["timer"]["remaining_seconds"] > 0:
                    start_app_countdown(app_name, app["timer"]["remaining_seconds"])
                    # Update the remaining time for the next use
                    app["timer"]["remaining_seconds"] -= timer_in_seconds - app["timer"]["remaining_seconds"]
                    save_to_json(config_data, "json/config.json")

            
def load_from_json(file_path):
    try:
        if os.path.exists(file_path):
            with open(file_path, 'r') as json_file:
                return json.load(json_file)
    except Exception as e:
        print(f"Error: {e}")
    return {}  # Return an empty dictionary if the file doesn't exist or there's an error

def time_to_seconds(time_dict):
    hours = time_dict.get("hours", 0)
    minutes = time_dict.get("minutes", 0)
    seconds = time_dict.get("seconds", 0)
    return hours * 3600 + minutes * 60 + seconds

def start_app_countdown(app_name, timer_in_seconds):
    while True:
        try:
            # Get all processes
            processes = psutil.process_iter()

            # Create a case-insensitive regular expression pattern
            pattern = re.compile(r'.*' + re.escape(app_name) + r'.*', re.IGNORECASE)

            # Search for the process with a matching name using the pattern
            matching_processes = [
                process for process in processes if re.match(pattern, process.name())
            ]

            if matching_processes:
                time.sleep(timer_in_seconds)
                killProcess(app_name)
                break

        except KeyboardInterrupt:
            break


def killProcess(app_name):
    try:
        # Get all processes
        processes = psutil.process_iter()

        # Create a case-insensitive regular expression pattern
        pattern = re.compile(r'.*' + re.escape(app_name) + r'.*', re.IGNORECASE)

        # Find processes with a matching name using the pattern
        matching_processes = [
            process for process in processes if re.match(pattern, process.name())
        ]

        if matching_processes:
            for process in matching_processes:
                process.terminate()

            # Block the app after terminating the process
            block_app(app_name)

            # Update the app status in the JSON
            config_data = load_from_json(r"json\config.json")
            if "apps" in config_data and isinstance(config_data["apps"], list):
                for app in config_data["apps"]:
                    if app.get("name", "") == app_name:
                        app["status"] = 1
                        break
                save_to_json(config_data, r"json\config.json")

        else:
            print(f"No processes found for '{app_name}'.")
    except Exception as e:
        print(f"Error: {e}")

def save_to_json(data, file_path):
    try:
        with open(file_path, 'w') as json_file:
            json.dump(data, json_file, indent=4)
    except Exception as e:
        print(f"Error: {e}")
        os._exit(1)


def block_app(app_name):
    try:
        location = winreg.HKEY_CURRENT_USER
        key_path = r"SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\explorer\DisallowRun"

        registry_key = winreg.OpenKey(location, key_path, 0, winreg.KEY_SET_VALUE)
        # Add the app name to the blocked apps list
        winreg.SetValueEx(registry_key, "1", 0, winreg.REG_SZ, app_name)
        winreg.CloseKey(registry_key)
    except Exception as e:
        print(f"Error: {e}")

def unblock_app():
    try:
        location = winreg.HKEY_CURRENT_USER
        key_path = r"SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\explorer\DisallowRun"

        registry_key = winreg.OpenKey(location, key_path, 0, winreg.KEY_SET_VALUE)

        # Remove the app name from the blocked apps list
        winreg.DeleteValue(registry_key, "1")

        winreg.CloseKey(registry_key)
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()