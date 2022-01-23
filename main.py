from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tkinter import *
from datetime import datetime, timedelta
import os

cwd = os.getcwd()
end = "pythonProject"
pathfind = (cwd[0:cwd.index(end)+len(end)])
# This is a script to register for classes

usernameinput = ''
passwordinput = ''
path = ''

def timerForRegistration():

    #myear: int = input("Enter year of registration (E.g: 2023): ")
    mmonth: int = input("Enter month of registration (E.g: 1): ")
    mday: int = input("Enter day of registration (E.g: 23): ")
    mhour: int = input("Enter hour of registration (E.g: 9): ")
    mminute: int = input("Enter minute of registration (E.g: 45): ")

    print()
    usernameinput = input("Please enter your K ID: ")
    passwordinput = input("Please enter your password: ")

    print()
    path = pathfind + "\chromedriver.exe"


    x = datetime.today()
    y = x.replace(month=int(mmonth), day=int(mday), hour=int(mhour), minute=int(mminute)) - timedelta(minutes=3)
    delta_t = y - x

    secs = delta_t.total_seconds()
    print(secs)

    time.sleep(secs)

    registerME()

def registerME():
    driver = webdriver.Chrome(path)
    driver.get("https://hornethq.kzoo.edu/Student/Account/Login")

    time.sleep(5)
    username = driver.find_element_by_id("UserName")
    username.send_keys(usernameinput)

    password = driver.find_element_by_id("Password")
    password.send_keys(passwordinput)

    password.send_keys(Keys.RETURN)

    time.sleep(5)

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
            register = WebDriverWait(driver, 1).until(
                EC.element_to_be_clickable((By.ID, "register-button"))
            )
            register.click()
            registered = True
            driver.close()
        except:
            driver.refresh()
            # To be removed for actual register code [to 73]
            time.sleep(3)
            nextTerm = WebDriverWait(driver, 1).until(
                EC.presence_of_element_located((By.ID, "schedule-next-term"))
            )
            nextTerm.click()
            time.sleep(3)

if __name__ == '__main__':
    print(pathfind)
    decider = input("Do you want to schedule for later?(y/n) ")
    if (decider == 'y'):
        timerForRegistration()
    else:
        usernameinput = input("Please type in your K ID: ")
        passwordinput = input("Please type in your password: ")
        path = pathfind + "\chromedriver.exe"
        registerME()
