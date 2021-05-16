# KahootBot

This Project uses Selenium Webdriver and allows the user to create and control 5 Kahoot Bots

# Prerequisites

The only prerequisite for KahootBot is that the user must update to the latest version of Chrome and install the latest chromedriver from: https://sites.google.com/a/chromium.org/chromedriver/downloads

# Instructions

As shown on Line 11 of KahootBot.py, the first step is to set the chromedriver variable to the path of chromedriver.exe. In my case, chromedriver.exe is in my downloads folder, hence the path seen on Line 11:
"C:/Users/Abhi/Downloads/chromedriver_win32/chromedriver.exe"

Upon running KahootBot.py, the user will be prompted to enter the game code (Kahoot Game PIN) and the nickname. If the user enters "Abhi" as the nickname, the bots will be named "Abhi1", "Abhi2 etc.

After entering the game code and nickname, 5 chrome tabs will pop up and proceed to join the Kahoot Game. Once the game starts, the user will be prompted to enter their choice for each question*.

The Choices are "1" for Red/Triangle, "2" for Blue/Diamond, "3" for Yellow/Circle, "4" for Green/Square, "0" to exit and close all bots 

*Until the user enters "0"
