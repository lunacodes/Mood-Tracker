import sys
import json
from colorama import init, Fore, Back, Style #This will be used to Add in Colors For Visual Clarity.  Refer to: https://pypi.python.org/pypi/colorama
init() #Might want to do this as coloroma.init() instead, just in case anything else in the future uses init()

"""Consider writing this without the JSON dump"""
"""Add User Profiles???"""
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
    global mood_history
    global mood_list #Is there a way to not use Globals???

    print("") #This is here for Proper Spacing

    mood = input(Fore.GREEN + "What is your Mood?\n" + Fore.MAGENTA)
    intensity = input(Fore.GREEN + "On a Scale of 1-10, How Intense is your Mood?\n" + Fore.MAGENTA)
    notes = input(Fore.GREEN + "Wanna add any Notes about this?\n" + Fore.MAGENTA)

    temp_entry_log = date + "  |  " + time + "  |  " +  mood + "  |  " +  intensity + "  |  " + notes 
    mood_list.append(temp_entry_log)

    """For some reason, this is overwriting the previous contents of the json file ... Why?!?!"""
    """it needs to save State between uses of the app in order to be useful"""
    """This may be a JSON issue, though it may also be a Python Issue"""
    with open('mood_history.json', 'w+') as f:
        json.dump(mood_list, f) #Does this cause the overwrite?

    print("\n")


def view_history(entry_log):
    """Allows the user to view their History in Daily, Weekly, Monthly & Yearly Intervals"""
    print("") #Spacing
    print(Fore.GREEN + "Date      Time    Mood   Intensity  Notes")
    with open('mood_history.json', 'r') as f:
        output = json.load(f)

    """How do we get this to format nicely???"""
    print(output)


def quote_of_the_day(): #Maybe we can Align the Text to Center??
    """Pulls quotes from a Giant Text File & Display One at Random"""
    """Does it make sense to write this in JSON?  Is it reasonable to pull a dictionary or list from JSON for this???"""

    quote_str = "I find hope in the darkest of days, and focus in the brightest. I do not judge the universe."
    autohr_str = "-Tenzin Gyatsu: Dalai Lama"
    print("") #Spacing
    print(Fore.GREEN + quote_str.center(len(quote_str))) 
    print(Fore.MAGENTA + autohr_str.center(len(autohr_str)) + "\n")

    # print(Fore.GREEN + "I find hope in the darkest of days, and focus in the brightest. I do not judge the universe.") 
    # print(Fore.MAGENTA + "-Tenzin Gyatsu: Dalai Lama \n")

def quit():
    """Quits the program"""
    print("") #Spacing
    print(Fore.MAGENTA + "Thanks!  Have an awesome Day :) \n")
    sys.exit()



if __name__ == "__main__":

    print(Back.BLACK + Fore.GREEN + "\nHi!!  Welcome to the Friendly Mood Tracker :)\n" )
    print("What would you like to do? (Enter as Number)\n")

    entry_log = ""
    mood_history = ""
    mood_list = []
    run = True
    while run == True:
        menu()