import os

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tkinter import *

#from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities



# Press the green button in the gutter to run the script.
# This is a script to register for classes

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.dirname(__file__)
    return os.path.join(base_path, relative_path)

def registerME():
    PATH = "C:/Program Files (x86)/chromedriver.exe"

    print("Copy path for chrome driver")
    path = input() + "\chromedriver.exe"
    driver = webdriver.Chrome(path)

    # driver = webdriver.Remote(
    #     command_executor='http://192.168.0.117:5556/wd/hub',
    #     desired_capabilities={'browserName': 'chrome',
    #                           'version': '2',
    #                           'javascriptEnabled': True})
    # selenium_grid_url = "http://192.168.0.117:5556"
    # print("Type in port number:")
    # portnumber = input()
    # selenium_grid_url = "http://192.168.0.117:" + portnumber + "/wd/hub"
    #
    # driver = webdriver.Remote(command_executor=selenium_grid_url, desired_capabilities=DesiredCapabilities.CHROME.copy())
    # driver.click(selenium_grid_url)

    # driver = webdriver.Chrome(resource_path('C:/Users/hanis/PycharmProjects/pythonProject/driver/chromedriver.exe'))

    driver.get("https://hornethq.kzoo.edu/Student/Account/Login")
    # print(driver.title)
    #time.sleep(5)
    #print("Hello, please type in your K ID")
    #usernameinput = input()
    usernameinput = "k19hs02"

    #print("Please type in your password")
    #passwordinput = input()
    passwordinput = "Twenty20Tw0p@$$"

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
    registerME()
