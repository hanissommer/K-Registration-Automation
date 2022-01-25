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

cwd = os.getcwd()
end = "\K-Registration-Automation-master"
pathfind = (cwd[0:cwd.index(end)+len(end)]) + "\chromedriver.exe"
# This is a script to register for classes
path = ''
end1="\Downloads"
startpath = (cwd[0:cwd.index(end1)]) + "\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup"
batchpath = cwd + "\startbatch.Bat"


target = batchpath
wDir = cwd
icon = batchpath

shell = Dispatch('WScript.Shell')
shortcut = shell.CreateShortCut(startpath)
shortcut.Targetpath = target
shortcut.WorkingDirectory = wDir
shortcut.IconLocation = icon
shortcut.save()

def timerForRegistration():

    # myear: int = input("Enter year of registration (E.g: 2023): ")
    # mmonth = input("Enter month of registration (E.g: 1): ")
    # mday = input("Enter day of registration (E.g: 23): ")
    # mhour = input("Enter hour of registration (E.g: 17)[Use military time]: ")
    # mminute = input("Enter minute of registration (E.g: 45): ")

    # print()
    # usernameinput = input("Please enter your K ID: ")
    # passwordinput = input("Please enter your password: ")

    # path = input("Paste path for chromedriver.exe: ") + "\chromedriver.exe"

    x = datetime.today()
    y = x.replace(month=int(mmonth), day=int(mday), hour=int(mhour), minute=int(mminute)) - timedelta(minutes=1)
    delta_t = y - x

    secs = delta_t.total_seconds()
    print(secs)
    print("Time before the program starts running: " + str(secs))

    time.sleep(secs)
    registerME()


def registerME():
    driver = webdriver.Chrome(path)
    driver.get("https://hornethq.kzoo.edu/Student/Account/Login")

    time.sleep(5)
    username = driver.find_element_by_id("UserName")
    username.send_keys(usernameinput, Keys.TAB)
    time.sleep(3)
    password = driver.find_element_by_id("Password")
    password.send_keys(passwordinput)
    time.sleep(3)
    #password.send_keys(Keys.RETURN)

    # time.sleep(5)

    try:
        studplanning = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.ID, "academic-planning"))
        )
        studplanning.click()
        time.sleep(5)
        goToPlanAndSchedule = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.ID, "home-step2"))
        )
        goToPlanAndSchedule.click()
        time.sleep(4)

        # To be disabled for the actual registering
        nextTerm = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.ID, "schedule-next-term"))
        )
        nextTerm.click()
        # time.sleep(3)

    except:
        driver.close()

    # Registering
    registered = False
    while not registered:
        try:
            register = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.ID, "register-button"))
            )
            register.click()
            registered = True
            driver.close()
        except:
            driver.refresh()
            # To be removed for actual register code [to 73]
            time.sleep(3)
            nextTerm = WebDriverWait(driver, 3).until(
                EC.presence_of_element_located((By.ID, "schedule-next-term"))
            )
            nextTerm.click()
            time.sleep(2)

    # if str(date.today()) == "2022-01-24":
    #     print("yes")
if __name__ == '__main__':
    path = pathfind
    exepath = cwd + "\main.exe"
    print("Hello, checking to see if it is time to run..")
    time.sleep(5)

    path = input("Paste path for chromedriver.exe: ") + "\chromedriver.exe"
    file_exists = os.path.exists('logininfoe.txt')
    if (file_exists):
        f = open("logininfoe.txt", "rt")
        f1 = open("logininfop.txt", "rt")
        g = open("dateinfo.txt", "rt")
        g1 = open("timeinfo.txt", "rt")
        datt = g.readline()
        if datt == str(date.today()):
            print("yes")
            usernameinput = f.readline()
            passwordinput = f1.readline()
            mmonth = g1.readline()
            mday = g1.readline()
            mhour = g1.readline()
            mminute = g1.readline()
            timerForRegistration()
        else:
            print("No, not today\n")
            time.sleep(3)
            sys.exit()
    else:
        print("No, not yet\n")
        decider = input("Do you want to schedule for later?(y/n) ")
        if (decider == 'y'):
            # z = open("startbatch.Bat", "w")
            # z.write("start \"\" \"" + exepath + "\"")
            shell = Dispatch('WScript.Shell')
            shortcut = shell.CreateShortCut(startpath)
            shortcut.Targetpath = target
            shortcut.WorkingDirectory = wDir
            shortcut.IconLocation = icon
            shortcut.save()
            usernameinput = input("Please type in your K ID: ")
            passwordinput = input("Please type in your password: ")
            datee = input("Enter date to run in yyyy-mm-dd format: ")
            mmonth = input("Enter month of registration (E.g: 1): ")
            mday = input("Enter day of registration (E.g: 23): ")
            mhour = input("Enter hour of registration (E.g: 17)[Use military time]: ")
            mminute = input("Enter minute of registration (E.g: 45): ")
            f = open("logininfoe.txt", "w")
            f1 = open("logininfop.txt", "w")
            f.write(usernameinput+"\n")
            f1.write(passwordinput+"\n")
            g = open("dateinfo.txt", "w")
            g.write(datee)
            g1 = open("timeinfo.txt", "w")
            g1.write(mmonth+"\n")
            g1.write(mday + "\n")
            g1.write(mhour + "\n")
            g1.write(mminute + "\n")
            print("You are all set! The program will start running two minutes before your registration time - just make sure to have your pc booted up on the day")
            time.sleep(15)
            sys.exit()
        else:
            usernameinput = input("Please type in your K ID: ")
            passwordinput = input("Please type in your password: ")
            # path = input("Paste path for chromedriver.exe: ") + "\chromedriver.exe"
            path = pathfind
            registerME()
