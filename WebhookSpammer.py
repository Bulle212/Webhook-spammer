import keyboard
import requests
import subprocess
from dhooks import Webhook
import os
import time
import sys

def clear():
    os.system("cls")

def title():
    os.system("title Made by Bulle212")

def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.1)

#You can change if you want other kinds of username's and password's. Delete these if you don't use the login system.  
user = ["User", "user"]
pas = ["Pass", "pass"]


list2 = ["0.1", "0.2", "0.3", "0.4", "0.5", "0.6", "0.7", "0.8", "0.9"]

hwid = str(str(subprocess.check_output('wmic csproduct get uuid')).strip().replace(r"\r", "").split(r"\n")[1].strip())



r = requests.get("https://pastebin.com/raw/XVuu8GnW") #Your pastebin paste here. Remember to only copy the letters and number in the URL https://pastebin.com/ ----> XVuu8GnW <---- and then replace them with the ones in here.





#I just made this for fun you can just delete it and change. The mainlogin() to start() in the bottom of the code


def mainlogin():
        clear()
        delay_print("Username:") 
        username2 = input(" ")
        
        if username2 in user:
            delay_print("Password:")
            password2 = input(" ")
            if password2 in pas:
                start()

            elif password2 != pas:
                clear()
                print("Incorrect password")    
                time.sleep(1)
                mainlogin()
        elif username2 != user:
            clear()
            print("Incorrect username")    
            time.sleep(1)
            mainlogin()
# ^
# |       
# |     
#I just made this for fun you can just delete it and change. The mainlogin() to start() in the bottom of the code
        



def start():    
    clear()
    delay_print("Checking for your HWID...")
    time.sleep(1)
    if hwid in r.text:
        clear()
        delay_print("HWID Found!")
        time.sleep(1)
        main()
    else:
        clear()
        print("Error! HWID Not in Database")
        print("Contact (YOUR DISCORD USERNAME) on discord for help. Your HWID: " + hwid) #Put in your discord username
        os.system('pause >NUL')

def main():
    clear()

    title()
    clear()

    delay_print("Welcome to Bulle's Webhook spammer. Press any key to countinue...")
    os.system('pause >NUL')
    spammer()


#The spammer
def spammer():
    clear()
    print("""
            
         __          __  _     _                 _                                                        
         \ \        / / | |   | |               | |                                                       
          \ \  /\  / /__| |__ | |__   ___   ___ | | __      ___ _ __   __ _ _ __ ___  _ __ ___   ___ _ __ 
           \ \/  \/ / _ \ '_ \| '_ \ / _ \ / _ \| |/ /     / __| '_ \ / _` | '_ ` _ \| '_ ` _ \ / _ \ '__|
            \  /\  /  __/ |_) | | | | (_) | (_) |   <      \__ \ |_) | (_| | | | | | | | | | | |  __/ |   
             \/  \/ \___|_.__/|_| |_|\___/ \___/|_|\_\     |___/ .__/ \__,_|_| |_| |_|_| |_| |_|\___|_|   
                                                               | |                                        
                                                               |_|      
------------------------------------------------------------------------------------------------------------------------
    """)

    webhook2 = input("Webhook: ")
    clear()
    print("""
            
         __          __  _     _                 _                                                        
         \ \        / / | |   | |               | |                                                       
          \ \  /\  / /__| |__ | |__   ___   ___ | | __      ___ _ __   __ _ _ __ ___  _ __ ___   ___ _ __ 
           \ \/  \/ / _ \ '_ \| '_ \ / _ \ / _ \| |/ /     / __| '_ \ / _` | '_ ` _ \| '_ ` _ \ / _ \ '__|
            \  /\  /  __/ |_) | | | | (_) | (_) |   <      \__ \ |_) | (_| | | | | | | | | | | |  __/ |   
             \/  \/ \___|_.__/|_| |_|\___/ \___/|_|\_\     |___/ .__/ \__,_|_| |_| |_|_| |_| |_|\___|_|   
                                                               | |                                        
                                                               |_|      
------------------------------------------------------------------------------------------------------------------------
    """)
    message = input("Message: ")
    clear()
    print("""
            
         __          __  _     _                 _                                                        
         \ \        / / | |   | |               | |                                                       
          \ \  /\  / /__| |__ | |__   ___   ___ | | __      ___ _ __   __ _ _ __ ___  _ __ ___   ___ _ __ 
           \ \/  \/ / _ \ '_ \| '_ \ / _ \ / _ \| |/ /     / __| '_ \ / _` | '_ ` _ \| '_ ` _ \ / _ \ '__|
            \  /\  /  __/ |_) | | | | (_) | (_) |   <      \__ \ |_) | (_| | | | | | | | | | | |  __/ |   
             \/  \/ \___|_.__/|_| |_|\___/ \___/|_|\_\     |___/ .__/ \__,_|_| |_| |_|_| |_| |_|\___|_|   
                                                               | |                                        
                                                               |_|      
------------------------------------------------------------------------------------------------------------------------
    """)
    delay = input("Delay in second(s): ")


    hook = Webhook(webhook2)

    while True:
                    clear() 

                    
                    print("Hold S to stop spamming...")
                    if keyboard.is_pressed("s"):
                        clear()
                        print("Stopped... Press any key to countinue.\n")
                        time.sleep(2)
                        os.system('pause >NUL')
                        main()
                    hook.send(message)
                    if delay in list2:
                        time.sleep(float(delay))
                    else:
                        time.sleep(int(delay))
    return


# if __name__ == "__main__":
#    title()
#    mainlogin()<-- DELETE. start() <-- REPLACE. Only if you delete the login system.

if __name__ == "__main__":
    title()
    mainlogin()