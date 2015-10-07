import sys
import colorama #This will be used to Add in Colors For Visual Clarity.  Refer to: https://pypi.python.org/pypi/colorama

date = "10/7/15" #Note: There are Python Modules to pull the Date & Time 
time = "6pm"


def menu():
    """Main Menu"""
    menu_choice = input("1.  Log Your Mood \n2.  View Your History \n3.  Quote of the Day \n4.  Quit\n\n")

    if menu_choice == "1":
        log_mood(date, time)
    elif menu_choice == "2":
        view_history(entry_log)
    elif menu_choice == "3":
        quote_of_the_day()
    elif menu_choice == "4":
        quit()

def log_mood(date, time):
    """Logs the User's Mood & Saves to a Global"""
    global entry_log
    mood = input("What is your Mood?\n")
    intensity = input("On a Scale of 1-10, How Intense is your Mood?\n")
    notes = input("Wanna add any Notes about this?\n")

    temp_entry_log = date + "  |  " + time + "  |  " +  mood + "  |  " +  intensity + "  |  " + notes
    #Insert Code to Save Entry Log to a File...
    print("\n")

    entry_log = temp_entry_log 

def view_history(entry_log):
    """Allows the user to view their History in Daily, Weekly, Monthly & Yearly Intervals"""
    print("Date      Time    Mood   Intensity  Notes")
    print(entry_log, "\n")

def quote_of_the_day():
    """Pulls quotes from a Giant Text File & Display One at Random"""
    print("I find hope in the darkest of days, and focus in the brightest. I do not judge the universe. \n-Tenzin Gyatsu: Dalai Lama \n")

def quit():
    """Quits the program"""
    print("Thanks!  Have an awesome Day :) \n")
    sys.exit()

if __name__ == "__main__":

    print("Hi!!  Welcome to the Friendly Mood Tracker :)\n" )
    print("What would you like to do? (Enter A Number)\n")

    entry_log=""
    run = True
    while run == True:
        menu()



