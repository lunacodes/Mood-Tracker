#!/usr/bin/python

#Note: Replace String Queries with Variables for Security Reasons
#Add an Undo Delete Function - This would involve a backup Database

import sys
import sqlite3 as lite

con = lite.connect('mood_history.sqlite')



"""Add User Profiles???"""
"""Deleted Colors from this version due to Dev Glitches"""

date = "10/7/15" #Note: There are Python Modules to pull the Date & Time 
time = "6pm"


def menu():
    """Main Menu"""
    menu_choice = input("1.  Log Your Mood \n2.  View Your History \n3.  Quote of the Day \n4.  Delete Log Entry \n5.  Delete Entire History \n6.  Quit\n\n")

    if menu_choice == "1":
        log_mood(date, time)
    elif menu_choice == "2":
        view_history()
    elif menu_choice == "3":
        quote_of_the_day()
    elif menu_choice =="4":
        delete_log_entry()
    elif menu_choice =="5":
        delete_entire_history()
    elif menu_choice == "6":
        quit()

def log_mood(date, time):
    """Logs the User's Mood & Saves to Database"""
    print("") #Spacing

    mood = input("What is your Mood?\n")
    intensity = input("On a Scale of 1-10, How Intense is your Mood?\n")
    notes = input("Wanna add any Notes about this?\n")

    con.execute("INSERT INTO MOOD_HISTORY_LOG (LOG_DATE, MOOD, INTENSITY, NOTES) \
        VALUES (?, ?, ?, ?)", (date, mood, intensity, notes));
    con.commit()
    print("Data Logged")
    print("\n")


def view_history():
    "Views User's Mood History from Database"
    #Add in Pagination

    print("") #Spacing

    cur.execute("SELECT * FROM MOOD_HISTORY_LOG")
    for row in cur:
        print("Log Number:", row[0])
        print("Date: ", row[1])
        print("Mood: ", row[2])
        print("Intensity: ", row[3])
        print("Time: ", row[4], "\n")


def quote_of_the_day(): #Maybe we can Align the Text to Center??
    """Pulls quotes from a Giant Text File & Display One at Random"""
    """Does it make sense to write this in JSON?  Is it reasonable to pull a dictionary or list from JSON for this???"""

    cur.execute("SELECT * FROM QUOTES ORDER BY RANDOM() LIMIT 1;")
    for row in cur:
        print(row[1], "\n")
        print(row[2], "\n")


def delete_log_entry():
    """This will have to list all the logs & be able to modify them via their list position"""
    #This doesn't adjust the numbers in ID - I may just have to live with that ...

    print("")
    log_number_to_delete = int(input('Enter the number of the Log you wish to delete.  If you don\'t know the number, press "v" to View log, or "m" for Main Menu \n\n'))
    # log_number_to_delete = int(log_number_to_delete)
    if log_number_to_delete == "v":
        view_history()
    elif log_number_to_delete == "m":
        pass
    else:
        cur.execute("SELECT * FROM MOOD_HISTORY_LOG")
        for row in cur:
            cur.execute("DELETE FROM MOOD_HISTORY_LOG WHERE ID=?;", (log_number_to_delete,))
            con.commit()
        
        print("Log %d Deleted!" % log_number_to_delete, "\n")

def delete_entire_history():
    user_delete_decision = input("Are you sure you want to do this???  (Y/N) \n")

    """Add in a Password protection here"""
    if user_delete_decision[0].lower() == "y": 
        cur.execute("DELETE FROM MOOD_HISTORY_LOG WHERE ID IN (SELECT ID FROM MOOD_HISTORY_LOG)")
        con.commit()
        
        print("")
        print("Mood History Deleted\n")

    else:
        print("Nevermind.  Back to the Main Menu")


def quit():
    """Quits the program"""
    print("") #Spacing
    print("Thanks!  Have an awesome Day :) \n")
    sys.exit()



if __name__ == "__main__":
    con = lite.connect('mood_history.sqlite')

    cur = con.cursor()
    con.execute('''CREATE TABLE IF NOT EXISTS MOOD_HISTORY_LOG (ID INTEGER PRIMARY KEY AUTOINCREMENT,
        LOG_DATE TEXT NOT NULL,
        MOOD TEXT NOT NULL,
        INTENSITY INT NOT NULL,
        NOTES TEXT NOT NULL);''')
    con.execute('''CREATE TABLE IF NOT EXISTS QUOTES (ID INTEGER PRIMARY KEY AUTOINCREMENT, 
        QUOTE TEXT NOT NULL,
        AUTHOR TEXT NOT NULL);''')

    #This is here for Undo purposes
    #I'll need to find someway of highlighting the differences
    con.execute('''CREATE TABLE IF NOT EXISTS MOOD_HISTORY_LOG_BACKUP (ID INTEGER PRIMARY KEY AUTOINCREMENT,
        LOG_DATE TEXT NOT NULL,
        MOOD TEXT NOT NULL,
        INTENSITY INT NOT NULL,
        NOTES TEXT NOT NULL);''')
    print("\nHi!!  Welcome to the Friendly Mood Tracker :)\n" )
    print("What would you like to do? (Enter as Number)\n")

    run = True
    while run == True:
        menu()