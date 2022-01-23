from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tkinter import *

# Press the green button in the gutter to run the script.
# This is a script to register for classes

def registerME():
    PATH = "C:/Program Files (x86)/chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    driver.get("https://hornethq.kzoo.edu/Student/Account/Login")
    # print(driver.title)
    time.sleep(5)
    print("Hello, please type in your K ID")
    usernameinput = input()

    print("Please type in your password")
    passwordinput = input()

    # passwordinput = ("Twenty20Tw0p@$$")
    username = driver.find_element_by_id("UserName")
    username.send_keys(usernameinput)
    # username.send_keys("k19hs02")

    password = driver.find_element_by_id("Password")
    password.send_keys(passwordinput)
    # password.send_keys("Twenty20Tw0p@$$")
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
        driver.quit()

    # Registering
    registered = False
    while not registered:
        try:
            register = WebDriverWait(driver, 1).until(
                EC.element_to_be_clickable((By.ID, "register-button"))
            )
            register.click()
            registered = True
            driver.quit()
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
    registerME()
