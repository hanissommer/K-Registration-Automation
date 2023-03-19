import os
import time
import win32com
from win32com.client import Dispatch
import registration
from datetime import datetime, timedelta



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
        print("The program will start running in " + str(secs/60) + " minute(s)")
        time.sleep(secs)
        registration.register(username1, password1)


# THIS FUNCTION RETURNS THE NUMBER OF HOURS LEFT
def timer2(month, day, hour, minute):
    x = datetime.today()
    y = x.replace(month=int(month), day=int(day), hour=int(hour),
                  minute=int(minute)) - timedelta(minutes=1)
    delta_t = y - x

    mins = delta_t.total_seconds()/60
    return str(mins/60)

# THIS FUNCTION CREATES A SHORTCUT TO THE PROGRAM IN THE STARTUP FOLDER
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
