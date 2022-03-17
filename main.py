import win32com
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tkinter import *
from datetime import date, datetime, timedelta
import sys
import os
import pythoncom
from win32com.client import Dispatch

#Find the path to where the program is from on the user's machine
cwd = os.getcwd()
#THIS SECTION IS TO FIND THE PATH OF THE CHROME DRIVER

#A place holder to find where in the path to stop and find the chrome driver
end = "\K-Registration-Automation-master"
#Putting the file path for the chromedriver together
pathfind = (cwd[0:cwd.index(end)+len(end)]) + "\chromedriver.exe"
path = ''

#THIS SECTION IS TO FIND THE PATH TO WHERE THE SHORTCUT TO THE EXE OF THE PROGRAM WILL BE

#To serve as an index
end1="\Downloads"
#Creating the whole path to the startup folder on PCs
startpath = (cwd[0:cwd.index(end1)]) + "\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup"

#THIS FUNCTION CREATES A TIMER BEFORE WHICH THE PROGRAM WILL RUN

def timerForRegistration():
    x = datetime.today()
    y = x.replace(month=int(mmonth), day=int(mday), hour=int(mhour), minute=int(mminute)) - timedelta(minutes=1)
    delta_t = y - x

    secs = delta_t.total_seconds()
    print("Number of minutes before the program starts running: " + str(secs/60))

    time.sleep(secs)
    registerME()

#THIS IS THE FUNCTION WITH ALL THE CODE TO EXECUTE THE AIM OF THE PROGRAM

def registerME():
    # A variable to get the chrome driver
    driver = webdriver.Chrome(path)
    # The driver then opens the website to register on (Hornet HQ)
    driver.get("https://hornethq.kzoo.edu/Student/Account/Login")
    # Wait 5 seconds -- for the page to load
    time.sleep(5)
    # Finds the username element on the webpage -- which should be a textfield
    username = driver.find_element_by_id("UserName")
    # Fills the textfield with the username entered by the user
    username.send_keys(usernameinput, Keys.TAB)
    # Wait 3 seconds
    time.sleep(3)
    # Finds the username element on the webpage -- which should be a textfield
    password = driver.find_element_by_id("Password")
    # Fills the textfield with the password entered by the user
    # This built-in functions automatically hit the 'Enter' key afterwards
    # which advances to Hornet HQ's homepage
    password.send_keys(passwordinput)
    # Waits 3 seconds
    time.sleep(3)
    # password.send_keys(Keys.RETURN)


    # This is a series of code that will navigate from the homepage to the
    # registration section
    try:
        # Waits 5 seconds and then tries to find and store the
        # element (button) 'academic-planning' on the homepage
        studplanning = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.ID, "academic-planning"))
        )
        # If the page loads completely and element is located, it will
        # be clicked which advances to the 'academic planning' section
        studplanning.click()
        # Wait for 5 seconds for the 'acadmeic-planning' page to load
        time.sleep(5)
        # Waits 5 seconds and then tries to find and store the
        # element (button) 'home-step2' on the 'acadmeic-planning' page
        goToPlanAndSchedule = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.ID, "home-step2"))
        )
        # If the page loads completely and element is located, it will
        # be clicked which advances to the 'Plan and Schedule' section
        goToPlanAndSchedule.click()
        # Wait for 4 seconds for the 'Plan and Schedule' page to load
        time.sleep(4)

        # The 'Plan and Schedule' page will load on the current term so
        # this will wait 5 seconds and then try to find and store the
        # element (button) 'schedule-next-term' on the 'Plan and Schedule' page
        nextTerm = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.ID, "schedule-next-term"))
        )
        # If the page loads completely and element is located, it will
        # be clicked which advances to the next term
        nextTerm.click()
        # time.sleep(3)

    # If any of the elements fail to be found, the webpage will close
    except:
        driver.close()

    # This section of the code will register the user

    # Firstly, it checks that the user is not registered
    registered = False
    while not registered:
        try:
            # Waits 5 seconds and then checks if the register button is clickable
            # and if so, stores the element (button) 'register-button'
            register = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.ID, "register-button"))
            )
            # If the page loads completely and element is clickable, it will
            # be clicked which registers the user
            register.click()
            # Convert the boolean that checks if the user is already registered
            registered = True
            print("You have successfully registered!")
            time.sleep(30)
            # Closes the webpage now that the user is registered
            driver.close()
        except:
            # If the register button is not clickable yet, the webpage is reloaded
            driver.refresh()
            # Waits 3 seconds, the ngo back to the 'next term' to re-attempt registering
            time.sleep(3)
            nextTerm = WebDriverWait(driver, 3).until(
                EC.presence_of_element_located((By.ID, "schedule-next-term"))
            )
            nextTerm.click()
            time.sleep(2)

#THE MAIN PART OF THE CODE THAT PUTS ALL THE FUNCTIONS TOGETHER

if __name__ == '__main__':
    # Initializes the 'path' to be that which was determined at the top
    path = pathfind
    # Stores the path of the executable file for the program
    exepath = cwd + "\main.exe"
    print("Hello there, just checking to see if it is time to register and/or everything is in place...")
    time.sleep(5)
    # This checks if the user had already opened the program before and filled in the login info it asks for
    file_exists = os.path.exists('logininfoe.txt')
    # If that one file with their credentials exists then all of the others do
    # and as such the program has all the necessary info it needs to run
    if (file_exists):
        # Stores the function that opens the 'logininfoe' textfile
        f = open("logininfoe.txt", "rt")
        # Stores the function that opens the 'logininfop' textfile
        f1 = open("logininfop.txt", "rt")
        # Stores the function that opens the 'dateinfo' textfile
        g = open("dateinfo.txt", "rt")
        # Stores the function that opens the 'timeinfo' textfile
        g1 = open("timeinfo.txt", "rt")
        # Stores the information from 'dateinfo' textfile
        datt = g.readline()
        # Checks if the date stored in the text file is the same as the day the program is running
        if datt == str(date.today()):
            # If it is, then send a print statement that it is and extract the information from
            # all the textfiles stored by the program (done further down). The 'timerForRegistration'
            # and 'registerMe' functions will need these information
            print("Yes, it is...")
            usernameinput = f.readline()
            passwordinput = f1.readline()
            mmonth = g1.readline()
            mday = g1.readline()
            mhour = g1.readline()
            mminute = g1.readline()
            timerForRegistration()
        # If the dates are not the same it means that it is not the day to register,
        # and the program will close
        else:
            print("No, not today\n")
            time.sleep(3)
            sys.exit()
    # If that one file with their credentials does not exist then none of the others do
    # and as such we know this is the first time the program is being ran and needs to
    # ask for the necessary info
    else:
        print("No, not yet\n")
        # Asks the user if they want to schedule for later
        decider = input("Do you want to schedule for later?(y/n) ")
        # If the user replied with yes, we will need to ask for some more information than if
        # they said no -- which means they would want to run it the same day they are using it
        if (decider == 'y'):
            # Creates and stores the path to where the shortcut to the program's executable
            # will be stored -- in the user's pc's startup folder
            shrotcutpath = startpath + "\startmainexe.lnk"
            # Stores the path to the program's executable
            target = exepath

            # Creates and store the shortcut in the previously determined location on the user's pc
            shell = win32com.client.Dispatch('WScript.Shell')
            shortcut = shell.CreateShortCut(shrotcutpath)
            shortcut.Targetpath = target
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
            f.write(usernameinput+"\n")
            # User's password
            f1 = open("logininfop.txt", "w")
            f1.write(passwordinput+"\n")
            # User's date of registration
            g = open("dateinfo.txt", "w")
            g.write(datee)
            # User's time of registration (The date is a redundancy here)
            g1 = open("timeinfo.txt", "w")
            g1.write(mmonth+"\n")
            g1.write(mday + "\n")
            g1.write(mhour + "\n")
            g1.write(mminute + "\n")

            # Tells the user that the program has everything it needs to run on the date of registration
            # then closes after 15 seconds
            print("You are all set! The program will start running two minutes before your registration "
                  "time - just make sure to have your pc booted up on the day")
            time.sleep(15)
            sys.exit()
        # If the user does not want to schedule the program to run at a later date but want to do
        # it at the time of opening, the program will only need their login information (username and password)
        else:
            usernameinput = input("Please type in your K ID: ")
            passwordinput = input("Please type in your password: ")
            # Stores the path of the Chromedriver
            path = pathfind
            # Calls the 'registerMe' function which will use the usernameinput and passwordinput to run
            registerME()