#!/usr/bin/python3
import time
import webbrowser
menu='''
 press 1 to check current time and date:
 press 2 to scan all your mac address in your current connected network:
 press 3 to shutdown your machine after 15 minutes: 
 press 4 to search something on google:
 press 5 to logout your current machine:
 press 6 to shutdown all connected system in your current  network:
 press 7 to update status in facebook:
 press 8 to list ip address of given website 
 '''
print(menu)
choice =input()

if choice == '1':
      print("current date and time is :",time.ctime())
    
elif choice =='4':
      find =input("enter your query:")
      webbrowser.open_new_tab("https://www.google.com/search?q=" +find)
elif choice == '3':
      print("machine will be shutdown in 1 minute")
      commands.getoutput("shutdown +1")
else:
      print("Invalid option")

