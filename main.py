# #Using terminal only
# import os
# import sys
# import time
# from datetime import date
# import registration
# import schedule
# import json

# # Find the path to where the program is from on the user's machine
# cwd = os.getcwd()
# #exepath = cwd + "\main.exe"
# exepath = cwd + "\RegisterMe.exe"


# # THIS SECTION IS TO FIND THE PATH TO WHERE THE SHORTCUT TO THE EXE OF THE PROGRAM WILL BE

# # To serve as an index
# #end1="\Downloads"
# # Creating the whole path to the startup folder on PCs
# #startpath = (cwd[0:cwd.index(end1)]) + "\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup"
# startpath = os.path.join(os.environ['APPDATA'], r'Microsoft\Windows\Start Menu\Programs\Startup')


# # THE MAIN PART OF THE CODE THAT PUTS ALL THE FUNCTIONS TOGETHER

# if __name__ == '__main__':
#     # Initializes the 'path' to be that which was determined at the top
#     # Stores the path of the executable file for the program
#     exepath = cwd + "\RegisterMe.exe"
#     print("Hello there, just checking to see if it is time to register and/or everything is in place...")
#     time.sleep(5)
#     # This checks if the user had already opened the program before and filled in the login info it asks for
#     file_exists = os.path.exists('data.json')
#     # If the json exists then the program has all the necessary info it needs to run
    
#     if (file_exists):
#         with open('data.json', 'r') as f:
#             userData = json.load(f)
#         #registrationdate = g.readline()
#         registrationdate = userData["date"]
#         # Checks if the date stored in the text file is the same as the day the program is running
#         if registrationdate == str(date.today()):
#             # If it is, then send a print statement that it is and extract the information from the json file
#             # The 'timer' and 'register' functions will need these information
#             print("Yes, it is...")
#             usernameinput = userData["username"]
#             passwordinput = userData["password"]
#             mmonth = userData["month"]
#             mday = userData["day"]
#             mhour = userData["hour"]
#             mminute = userData["minute"]
#             schedule.timer(usernameinput, passwordinput, mmonth, mday, mhour, mminute)
#         # If the dates are not the same it means that it is not the day to register,
#         # and the program will close
#         else:
#             print("No, not today\n")
#             time.sleep(3)
#             sys.exit()
#     # If the json doesn't exist we know this is the first time the program is being ran and needs to
#     # ask for the necessary info
#     else:
#         print("No, not yet\n")
#         # Asks the user if they want to schedule for later
#         decider = input("Do you want to schedule for later?(y/n) ")
#         # If the user replied with yes, we will need to ask for some more information than if
#         # they said no -- which means they would want to run it the same day they are using it
#         if decider == 'y':
#             schedule.getinfo(exepath, startpath)
#             time.sleep(15)
#             sys.exit()
#         # If the user does not want to schedule the program to run at a later date but want to do
#         # it at the time of opening, the program will only need their login information (username and password)
#         else:
#             usernameinput = input("Please type in your K ID: ")
#             passwordinput = input("Please type in your password: ")
#             # Stores the path of the Chromedriver
#             # Calls the 'register' function which will use the usernameinput and passwordinput to run
#             registration.register(usernameinput, passwordinput)
