# #TO BE COMPLETED
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.service import Service
# from registration import driver
#
#
# def addifopen(kid, kpassword):
#
#     # This is a series of code that will navigate from the homepage to the
#     # registration section
#     try:
#         # Waits 5 seconds and then tries to find and store the
#         # element (button) 'academic-planning' on the homepage
#         studplanning = WebDriverWait(driver, 5).until(
#             EC.presence_of_element_located((By.ID, "academic-planning"))
#         )
#         # If the page loads completely and element is located, it will
#         # be clicked which advances to the 'academic planning' section
#         studplanning.click()
#         # Wait for 5 seconds for the 'acadmeic-planning' page to load
#         time.sleep(5)
#         # Waits 5 seconds and then tries to find and store the
#         # element (button) 'home-step2' on the 'acadmeic-planning' page
#         goToPlanAndSchedule = WebDriverWait(driver, 5).until(
#             EC.presence_of_element_located((By.ID, "home-step2"))
#         )
#         # If the page loads completely and element is located, it will
#         # be clicked which advances to the 'Plan and Schedule' section
#         goToPlanAndSchedule.click()
#         # Wait for 4 seconds for the 'Plan and Schedule' page to load
#         time.sleep(4)
#
#         # The 'Plan and Schedule' page will load on the current term so
#         # this will wait 5 seconds and then try to find and store the
#         # element (button) 'schedule-next-term' on the 'Plan and Schedule' page
#         nextTerm = WebDriverWait(driver, 5).until(
#             EC.presence_of_element_located((By.ID, "schedule-next-term"))
#         )
#         # If the page loads completely and element is located, it will
#         # be clicked which advances to the next term
#         nextTerm.click()
#         # time.sleep(3)
#
#     # If any of the elements fail to be found, the webpage will close
#     except:
#         driver.close()
#
#     # This section of the code will register the user
#
#     # Firstly, it checks that the user is not registered
#     registered = False
#     while not registered:
#         try:
#             # Waits 5 seconds and then checks if the register button is clickable
#             # and if so, stores the element (button) 'register-button'
#             registerbutton = WebDriverWait(driver, 5).until(
#                 EC.element_to_be_clickable((By.ID, "register-button"))
#             )
#             # If the page loads completely and element is clickable, it will
#             # be clicked which registers the user
#             registerbutton.click()
#             # Convert the boolean that checks if the user is already registered
#             registered = True
#             print("You have successfully registered!")
#             time.sleep(30)
#             # Closes the webpage now that the user is registered
#             driver.close()
#         except:
#             # If the register button is not clickable yet, the webpage is reloaded
#             driver.refresh()
#             # Waits 3 seconds, the ngo back to the 'next term' to re-attempt registering
#             time.sleep(3)
#             nextTerm = WebDriverWait(driver, 3).until(
#                 EC.presence_of_element_located((By.ID, "schedule-next-term"))
#             )
#             nextTerm.click()
#             time.sleep(2)
#
#
