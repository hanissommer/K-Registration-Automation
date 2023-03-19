import os
import time
import win32com
from win32com.client import Dispatch
import registration
from datetime import datetime, timedelta
# import os
import json
# import win32com.client


# THIS FUNCTION CREATES A TIMER BEFORE WHICH THE PROGRAM WILL RUN
def timer(username1, password1, month, day, hour, minute):
    x = datetime.today()
    y = x.replace(month=int(month), day=int(day), hour=int(hour),
                  minute=int(minute)) - timedelta(minutes=1)
    delta_t = y - x

    secs = delta_t.total_seconds()
    print("Number of minutes before the program starts running: " + str(secs/60))
    if secs <= 0:
        print("The program will start running now")
        registration.register(username1, password1)
    else:
        print("The program will start running in " + str(secs/60) + " minutes")
        time.sleep(secs)
        registration.register(username1, password1)

def timer2(month, day, hour, minute):
    x = datetime.today()
    y = x.replace(month=int(month), day=int(day), hour=int(hour),
                  minute=int(minute)) - timedelta(minutes=1)
    delta_t = y - x

    mins = delta_t.total_seconds()/60
    return str(mins/60)

def setupShortcut(epath, spath):

    # Path to the executable file
    executable_path = epath

    # Create a shell object
    shell = win32com.client.Dispatch("WScript.Shell")

    # Get the path to the Start Up folder
    startup_folder = shell.SpecialFolders("Startup")

    # Create a shortcut object
    shortcut = shell.CreateShortCut(os.path.join(startup_folder, "Kregister.lnk"))

    # Set the path and arguments for the executable
    shortcut.Targetpath = executable_path
    shortcut.Arguments = ""

    # Set the working directory for the shortcut
    shortcut.WorkingDirectory = os.path.dirname(executable_path)

    # Save the shortcut to the Start Up folder
    shortcut.save()



# def getinfo(epath, spath):
#     # Creates and stores the path to where the shortcut to the program's executable
#     # will be stored -- in the user's pc's startup folder
#     shrotcutpath = spath + "\startmainexe.lnk"
#     # Stores the path to the program's executable
#     target = epath

#     # Creates and store the shortcut in the previously determined location on the user's pc
#     shell = win32com.client.Dispatch('WScript.Shell')
#     shortcut = shell.CreateShortCut(shrotcutpath)
#     shortcut.Targetpath = target
#     cwd = os.getcwd()
#     shortcut.WorkingDirectory = cwd
#     shortcut.WindowStyle = 1
#     shortcut.save()

#     # Asks the user for information that the program will need to run at a later date
#     usernameinput = input("Please type in your K ID: ")
#     passwordinput = input("Please type in your password: ")
#     datee = input("Enter date to run in yyyy-mm-dd format: ")
#     mmonth = input("Enter month of registration (E.g: 1): ")
#     mday = input("Enter day of registration (E.g: 23): ")
#     mhour = input("Enter hour of registration (E.g: 17)[Use military time]: ")
#     mminute = input("Enter minute of registration (E.g: 45): ")

#     # Creates a dictionary with the user's information
#     data = {
#         "username": usernameinput,
#         "password": passwordinput,
#         "date": datee,
#         "month": mmonth,
#         "day": mday,
#         "hour": mhour,
#         "minute": mminute
#     }

#     # Write the dictionary to a JSON file
#     with open("data.json", "w") as f:
#         json.dump(data, f)

#     # Tells the user that the program has everything it needs to run on the date of registration
#     # then closes after 15 seconds
#     print("You are all set! The program will start running two minutes before your registration "
#           "time - just make sure to have your pc booted up on the day")
