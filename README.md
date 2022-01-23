# registerBot
This is a python program that asks the user for their K credentials and logs into Hornet HQ and attempts to register for courses.

This program will allow for users to not have to manually register for classes but instead use this program to automate the process.

To start, click on the 'Register' file which is a shortcut to the executable for the program.
The command line/terminal should open as well as your Chrome browser with the Hornet HQ login page loaded up.
In the terminal, you will be prompted to type in your K ID, after which you will hit the enter key. You will then be prompted for your K password as well.
After inputing your credentials in the terminal, the program should log in and navigate to the Plan and Schedule page.
Here, it will attempt to click the 'Register Now' button and if it is not available to be clicked, it will refresh the page and try again.
The program will do this continually until that button is clickable and is clicked, meaning that you've successfully registered.
