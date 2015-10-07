import sys
from colorama import init, Fore, Back, Style #This will be used to Add in Colors For Visual Clarity.  Refer to: https://pypi.python.org/pypi/colorama
init() #Might want to do this as coloroma.init() instead, just in case anything else in the future uses init()

"""Not committed to any of the Colors I chose"""

date = "10/7/15" #Note: There are Python Modules to pull the Date & Time 
time = "6pm"


def menu():
    """Main Menu"""
    menu_choice = input(Fore.GREEN + "1.  Log Your Mood \n2.  View Your History \n3.  Quote of the Day \n4.  Quit\n\n" + Fore.MAGENTA)

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

    print("") #This is here for Proper Spacing
    mood = input(Fore.GREEN + "What is your Mood?\n" + Fore.MAGENTA)
    intensity = input(Fore.GREEN + "On a Scale of 1-10, How Intense is your Mood?\n" + Fore.MAGENTA)
    notes = input(Fore.GREEN + "Wanna add any Notes about this?\n" + Fore.MAGENTA)

    temp_entry_log = date + "  |  " + time + "  |  " +  mood + "  |  " +  intensity + "  |  " + notes
    #Insert Code to Save Entry Log to a File...
    print("\n")

    entry_log = temp_entry_log 

def view_history(entry_log):
    """Allows the user to view their History in Daily, Weekly, Monthly & Yearly Intervals"""
    print("") #Spacing
    print(Fore.GREEN + "Date      Time    Mood   Intensity  Notes")
    print(Fore.MAGENTA + entry_log, "\n")

def quote_of_the_day(): #Maybe we can Align the Text Center??
    """Pulls quotes from a Giant Text File & Display One at Random"""
    print("") #Spacing
    print(Fore.GREEN + "I find hope in the darkest of days, and focus in the brightest. I do not judge the universe.") 
    print(Fore.MAGENTA + "-Tenzin Gyatsu: Dalai Lama \n")

def quit():
    """Quits the program"""
    print("") #Spacing
    print(Fore.MAGENTA + "Thanks!  Have an awesome Day :) \n")
    sys.exit()

if __name__ == "__main__":

    print(Back.BLACK + Fore.GREEN + "\nHi!!  Welcome to the Friendly Mood Tracker :)\n" )
    print("What would you like to do? (Enter A Number)\n")

    entry_log=""
    run = True
    while run == True:
        menu()



