from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tkinter import *
from datetime import datetime, timedelta

# Press the green button in the gutter to run the script.
# This is a script to register for classes

usernameinput = ''
passwordinput = ''
path = ''

def timerForRegistration():
    print("Enter year of registration")
    myear: int = input()
    print("Enter month of registration, in numbers")
    mmonth: int = input()
    print("Enter day of registration, in numbers")
    mday: int = input()
    print("Enter hour of registration, in numbers")
    mhour: int = input()
    print("Enter minute of registration, in numbers")
    mminute: int = input()

    print("Please type in your K ID")
    usernameinput = input()

    print("Please type in your password")
    passwordinput = input()

    print("Copy path for chrome driver")
    path = input() + "\chromedriver.exe"

    x = datetime.today()
    y = x.replace(month=int(mmonth), day=int(mday), hour=int(mhour), minute=int(mminute)) - timedelta(minutes=3)
    delta_t = y - x

    secs = delta_t.total_seconds()
    print(secs)

    time.sleep(secs)

    registerME()

def registerME():
    # PATH = "C:/Program Files (x86)/chromedriver.exe"

    # print("Copy path for chrome driver")
    # path = input() + "\chromedriver.exe"

    driver = webdriver.Chrome(path)

    driver.get("https://hornethq.kzoo.edu/Student/Account/Login")

    time.sleep(5)
    # print("Hello, please type in your K ID")
    # usernameinput = input()
    #
    #
    # print("Please type in your password")
    # passwordinput = input()


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
    timerForRegistration()
