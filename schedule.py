import os
import time
import win32com
from win32com.client import Dispatch
import registration
import main
from datetime import datetime, timedelta


# THIS FUNCTION CREATES A TIMER BEFORE WHICH THE PROGRAM WILL RUN
def timer(path, username1, password1, month, day, hour, minute):
    x = datetime.today()
    y = x.replace(month=int(month), day=int(day), hour=int(hour),
                  minute=int(minute)) - timedelta(minutes=1)
    delta_t = y - x

    secs = delta_t.total_seconds()
    print("Number of minutes before the program starts running: " + str(secs/60))

    time.sleep(secs)
    registration.register(path, username1, password1)

def getinfo(epath, spath):
    # Creates and stores the path to where the shortcut to the program's executable
    # will be stored -- in the user's pc's startup folder
    shrotcutpath = spath + "\startmainexe.lnk"
    # Stores the path to the program's executable
    target = epath

    # Creates and store the shortcut in the previously determined location on the user's pc
    shell = win32com.client.Dispatch('WScript.Shell')
    shortcut = shell.CreateShortCut(shrotcutpath)
    shortcut.Targetpath = target
    cwd = os.getcwd()
    shortcut.WorkingDirectory = cwd
    shortcut.WindowStyle = 1
    shortcut.save()

    # Asks the user for information that the program will need to run at a later date
    usernameinput = input("Please type in your K ID: ")
    passwordinput = input("Please type in your password: ")
    datee = input("Enter date to run in yyyy-mm-dd format: ")
    mmonth = input("Enter month of registration (E.g: 1): ")
    mday = input("Enter day of registration (E.g: 23): ")
    mhour = input("Enter hour of registration (E.g: 17)[Use military time]: ")
    mminute = input("Enter minute of registration (E.g: 45): ")

    # Creates and write to text files with each information asked for from the user

    # User's email
    f = open("logininfoe.txt", "w")
    f.write(usernameinput + "\n")
    # User's password
    f1 = open("logininfop.txt", "w")
    f1.write(passwordinput + "\n")
    # User's date of registration
    g = open("dateinfo.txt", "w")
    g.write(datee)
    # User's time of registration (The date is a redundancy here)
    g1 = open("timeinfo.txt", "w")
    g1.write(mmonth + "\n")
    g1.write(mday + "\n")
    g1.write(mhour + "\n")
    g1.write(mminute + "\n")

    # Tells the user that the program has everything it needs to run on the date of registration
    # then closes after 15 seconds
    print("You are all set! The program will start running two minutes before your registration "
          "time - just make sure to have your pc booted up on the day")
