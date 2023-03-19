import datetime
import os
import sys
import threading
import time
from datetime import date
import registration
import schedule
import json
import tkinter as tk
from tkinter import messagebox

from ctypes import alignment
import difflib
import PySimpleGUI as sg
import keyboard
import os

# Find the path to where the program is from on the user's machine
cwd = os.getcwd()
#exepath = cwd + "\main.exe"
exepath = cwd + "\RegisterMe.exe"


# Creating the whole path to the startup folder on PCs
startpath = os.path.join(os.environ['APPDATA'], r'Microsoft\Windows\Start Menu\Programs\Startup')


def readyToRun():
    with open('dataToRegister.json', 'r') as f:
        userData = json.load(f)
    
    # Get the current year
    current_year = datetime.datetime.now().year

    # Extract the month and day from the JSON data
    month = int(userData['month'])
    day = int(userData['day'])

    # Create the date string in yyyy-mm-dd format
    date_str = f"{current_year:04d}-{month:02d}-{day:02d}"

    registrationdate = date_str
    if registrationdate == str(date.today()):
        return True


def yes_Run():
    with open('dataToRegister.json', 'r') as f:
        userData = json.load(f)
    
    usernameinput = userData["username"]
    passwordinput = userData["password"]
    mmonth = userData["month"]
    mday = userData["day"]
    mhour = userData["hour"]
    mminute = userData["minute"]
    schedule.timer(usernameinput, passwordinput, mmonth, mday, mhour, mminute)




# Main window/form layout construction
file_exists = os.path.exists('dataToRegister.json')
# If the json exists then the program has all the necessary info it needs to run
runMe = False
if (file_exists):
    with open('dataToRegister.json', 'r') as f:
            userData = json.load(f)
    
    #If the program is ready to run, then run it
    if(readyToRun()):
        runMe = True
        timeToShow = "{:.2f}".format(float(schedule.timer2(userData["month"], userData["day"], userData["hour"], userData["minute"])))
        column0 = [
        [sg.Text('Username:')], [sg.InputText(default_text=str(userData["username"]), size=(60, 1))],
        [sg.Text('Password:')], [sg.InputText(default_text=str(userData["password"]), size=(60, 1))],

        [sg.Text('You will be registered today' + ' at: ' + str(userData["hour"]) + ':' + str(userData["minute"]))], 
        [sg.Text('You have to wait: ' + timeToShow + ' more hour(s) to register.')],
        [sg.Button('Register Now')],
        ]

        layout = [
            [column0]]

        form = sg.FlexForm('Kzoo Course Registration', layout, default_element_size=(50, 1), resizable=True)
        
    #If the program is not ready to run, then show the user the time left
    else:
        timeToShow = schedule.timer2(userData["month"], userData["day"], userData["hour"], userData["minute"])
        column0 = [
        [sg.Text('Choose one:')],
        [sg.Radio('Schedule for later', "RADIO1", default=True), sg.Radio('Register now', "RADIO1")],
        [sg.Text('Note: If you choose to register now, you only need to input your username and password.')], 
        [sg.Text('Username:')], [sg.InputText(default_text=str(userData["username"]), size=(60, 3))],
        [sg.Text('Password:')], [sg.InputText(default_text=str(userData["password"]), size=(60, 3))],
        [sg.Text('Month:')], [sg.InputText(default_text=str(userData["month"]), size=(60, 3))],
        [sg.Text('Day:')], [sg.InputText(default_text=str(userData["day"]), size=(60, 3))],
        [sg.Text('Hour:')], [sg.InputText(default_text=str(userData["hour"]), size=(60, 3))],
        [sg.Text('Minute:')], [sg.InputText(default_text=str(userData["minute"]), size=(60, 3))],

        [sg.Text('You are all set, however it is not your turn to register yet.')], 
        [sg.Text('You have to wait: ' + timeToShow + ' more hour(s) to register.')],
        [sg.Button('Submit')],
        ]

        layout = [
            [column0]]

        form = sg.FlexForm('Kzoo Course Registration', layout, default_element_size=(50, 1), resizable=True)

# If the json does not exist, then the program needs to get all the necessary info from the user
else:
    column0 = [
    [sg.Text('Choose one:')],
    [sg.Radio('Schedule for later', "RADIO1", default=True), sg.Radio('Register now', "RADIO1")],
    [sg.Text('Note: If you choose to register now, you only need to input your username and password.')], 
    [sg.Text('Username:')], [sg.InputText(default_text="", size=(60, 3))],
    [sg.Text('Password:')], [sg.InputText(default_text="", size=(60, 3))],
    [sg.Text('Month (01 to 12):')], [sg.InputText(default_text="", size=(60, 3))],
    [sg.Text('Day:')], [sg.InputText(default_text="", size=(60, 3))],
    [sg.Text('Hour (00 to 23):')], [sg.InputText(default_text="", size=(60, 3))],
    [sg.Text('Minute:')], [sg.InputText(default_text="", size=(60, 3))],
    [sg.Button('Submit'), sg.Cancel()],
    ]

    layout = [
        [column0]]

    form = sg.FlexForm('Kzoo Course Registration', layout, default_element_size=(50, 1), resizable=True)

# Main window/form event loop
while True:
    if runMe == True:
        # Create a new thread
        t = threading.Thread(target=yes_Run)

        # Start the thread, which will run the function in the background
        t.start()

    event, values = form.read()
    

    if event in (sg.WIN_CLOSED, 'Cancel'):
        break

    if event == 'Register Now':
        registration.register(userData["username"], userData["password"])
        form.close()

    if event == 'Submit' and values[0]:
        usernameinput = values[2]
        passwordinput = values[3]
        mmonth = values[4]
        mday = values[5]
        mhour = values[6]
        mminute = values[7]

        data = {
        "username": usernameinput,
        "password": passwordinput,
        "month": mmonth,
        "day": mday,
        "hour": mhour,
        "minute": mminute
        }

        # Write the dictionary to a JSON file
        with open("dataToRegister.json", "w") as f:
            json.dump(data, f)

        schedule.setupShortcut(exepath, startpath)
        if(readyToRun()):
            # Create a new thread
            t = threading.Thread(target=yes_Run)

            # Start the thread, which will run the function in the background
            t.start()
            
        form.close()
    elif event == 'Submit' and values[1]:
        usernameinput = values[2]
        passwordinput = values[3]
        # Create a new thread
        t = threading.Thread(target=registration.register(usernameinput, passwordinput))

        # Start the thread, which will run the function in the background
        t.start()
        
            
        form.close()
form.close()