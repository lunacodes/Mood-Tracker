import sys

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
        view_history(entry_log)
    elif menu_choice == "3":
        quote_of_the_day()
    elif menu_choice =="4":
        delete_log_entry()
    elif menu_choice =="5":
        delete_history()
    elif menu_choice == "6":
        quit()

def log_mood(date, time):
    """Logs the User's Mood & Saves to a Global"""
    global log_number
    global entry_log

    log_number += 1

    print("") #This is here for Proper Spacing

    mood = input("What is your Mood?\n")
    intensity = input("On a Scale of 1-10, How Intense is your Mood?\n")
    notes = input("Wanna add any Notes about this?\n")

    temp_entry_log = date + "  |  " + time + "  |  " +  mood + "  |  " +  intensity + "  |  " + notes + "\n"
    # temp_entry_log = str(log_number) + ".  " + date + "  |  " + time + "  |  " +  mood + "  |  " +  intensity + "  |  " + notes + "\n"

    with open('mood_history.txt', 'a') as f: #Consider Hopping Back to JSON For Data Dump
        f.write(temp_entry_log)
        f.close()

    print("\n")


def view_history(entry_log):
    """Allows the user to view their History in Daily, Weekly, Monthly & Yearly Intervals"""
    global log_number
    print("") #Spacing
    print("Date      Time    Mood   Intensity  Notes")
    with open('mood_history.txt', 'r') as f:
        output = f.read()
    print(output)


def quote_of_the_day(): #Maybe we can Align the Text to Center??
    """Pulls quotes from a Giant Text File & Display One at Random"""
    """Does it make sense to write this in JSON?  Is it reasonable to pull a dictionary or list from JSON for this???"""

    quote_str = "I find hope in the darkest of days, and focus in the brightest. I do not judge the universe."
    author_str = "-Tenzin Gyatsu: Dalai Lama"
    print("") #Spacing
    print(quote_str.center(len(quote_str))) 
    print(author_str.center(len(author_str)) + "\n")

    # print("I find hope in the darkest of days, and focus in the brightest. I do not judge the universe.") 
    # print("-Tenzin Gyatso: Dalai Lama \n")


def delete_log_entry():
    print("This Feature is in Revision & will become available next version")
    # user_log_to_delete = input("Enter the number of the line you wish to delete: \n")
    # with open('mood_history.txt', 'r') as log_deletetion_input:
    #     with open('mood_history.txt', 'w') as log_deletion_output:
    #         for line in log_deletetion_input:
    #             if line.startswith(user_log_to_delete) == False:
    #                 output.write("This Is A Test") ## The problem here is that it's overwriting from the beginning of the file
    #                 I will need to consult ppl about this


    # input('Enter the Number of the log you wish to delete.  You may type "main" instead to return to the Main Menu')
    """This will have to list all the logs & be able to modify them via their list position"""


def delete_history():
    user_delete_decision = input("Are you sure you want to do this???  (Y/N) \n")

    """Add in a Password protection here"""
    if user_delete_decision[0].lower() == "y": 
        with open('mood_history.txt', "w") as f:
            f.write("")
            f.close()
        print("\nDeleted\n")
        log_number = 0
    else:
        print("Nevermind.  Back to the Main Menu")


def quit():
    """Quits the program"""
    print("") #Spacing
    print("Thanks!  Have an awesome Day :) \n")
    sys.exit()



if __name__ == "__main__":
    #Add In A Check To see if mood_history.txt exists.  
    #If not - Create it
    
    entry_log = ""
    with open('mood_history.txt', 'r') as f:
        log_number = sum(1 for line in f) 
    print(log_number)

    print("\nHi!!  Welcome to the Friendly Mood Tracker :)\n" )
    print("What would you like to do? (Enter as Number)\n")

    run = True
    while run == True:
        menu()