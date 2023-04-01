from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

global driver

# This function will register the user on Hornet HQ
def register(kid, kpassword):
    global driver
    service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get("https://hornethq.kzoo.edu/Student/Account/Login")

    # Wait for the login page to load
    username = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "UserName"))
    )
    password = driver.find_element_by_id("Password")

    # Enter the login credentials and submit the form
    username.send_keys(kid)
    password.send_keys(kpassword)
    password.submit()

    # Wait for the dashboard page to load
    dashboard = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "academic-planning"))
    )

    # Navigate to the registration page
    dashboard.click()
    planning = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "home-step2"))
    )
    planning.click()

    # Wait for the planning page to load
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "schedule-next-term"))
    )

    # Attempt to register the user
    registered = False
    while not registered:
        try:
            # Check if the registration button is clickable
            registerbutton = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.ID, "register-button"))
            )
            # If the button is clickable, click it to register the user
            registerbutton.click()
            registered = True
            print("You have successfully registered!")
            time.sleep(30)
            driver.close()
        except:
            # If the registration button is not clickable yet, reload the page
            driver.refresh()
            time.sleep(2)

            # Navigate to the next term and try again
            nextTerm = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "schedule-next-term"))
            )
            nextTerm.click()
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "register-button"))
            )

    driver.close()

