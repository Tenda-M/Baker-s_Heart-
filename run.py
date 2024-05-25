# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import gspread #import the entire gspread library
from google.oauth2.service_account import Credentials # imports the Credentials class, which is part of the service_account  function from the Google auth library.  

#import two libraries: time and sys, to improve the display of text on the screen by adding a typing effect/delay.
import time

# Import sys for sys.stdout.write
import sys 

# import the os library, that will clear screen
import os

#"SCOPE" constant variable , in pathon they are in capital
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ] #The scope lists the APIs that the  program should access in order to run.

#constant variables
CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('Baker’s_Heart')
#######################################################
    ###########. WELCOME SCREEN .############
#######################################################

#Function to improve the display of text on the screen by adding a typing effect/delay.
"""
Credit: https://www.101computing.net/python-typing-text-effect/
"""
def typingPrint(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.05)
  

def typingInput(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.05)
  value = input()  
  return value


# Function used to clear the screen from previous outputs and inputs.
# Credit: https://www.101computing.net/python-typing-text-effect/
def clearScreen():
    """
    This function will be use to clear the ASCII 
    """
    os.system("clear")


# Function the print logo ASCII
def print_bakers_heart_logo():
    """
    Run opening screen for user and gives brief explanation of its use.
     Prints the specified logo for Baker's Heart.
    ASCII creation redit: patorjk.com
    """
    print("Welcome to Baker's Heart Data Automation")

    print("\n")
    # List of lines that make up the ASCII art logo
    #Credit: https://ascii.today/
    logo_lines = [
    
        "888888b.            888                       d8b         ",
        "888  88b            888                       88P         ",
        "888  .88P           888                       8P          ",
        "8888888K.   8888b.  888  888  .d88b.  888d888  .d8888b  ",
        "888  Y88b       88b 888 .88P d8P  Y8b 888P     88K      ",
        "888    888 .d888888 888888K  88888888 888       Y8888b. ",
        "888   d88P 888  888 888  88b Y8b.     888           X88 ",
        "8888888P   Y888888  888  888  Y8888   888       88888P' ",
        "                                                          ",
        "                                                          ",
        "                                                          ",
        "888    888                           888                  ",
        "888    888                           888                  ",
        "888    888                           888                  ",
        "8888888888  .d88b.   8888b.  888d888 888888               ",
        "888    888 d8P  Y8b      88b 888P    888                  ",
        "888    888 88888888 .d888888 888     888                  ",
        "888    888 Y8b.     888  888 888     Y88b.                ",
        "888    888  Y8888   Y888888  888      Y888"
      ]

    # Loop through each line in the logo_lines list and print it
    for line in logo_lines:
        print(line)

    print("\n")
    print(" Sales & Inventory Management " "for Baker's Heart.\n")
 
    print("(Created for Educational Purposes -" " Copyright: Tatenda Mudehwe 'May 2024)")
    time.sleep(5)
    clearScreen()
    #print (logo_lines)


#sales = SHEET.worksheet('sales')
#this is to pull all values from the sales worksheet
#data = sales.get_all_values()
# this print statement will print out data to the terminal
#print(data)
##########################################################
    ###########.  SALES MENU .##############
##########################################################
# Function for sales menu
def sales_menu():
    """
    Display the Sales Menu and handle user choices.
    """
    while True:
        print("\nSales Menu\n")
        print("1. View Sales")
        print("2. Add Sales")
        print("3. Back to Main Menu\n")

        sales_choice = input("Enter your choice (1, 2, or 3):\n")
        clearScreen()# Clear the screen when a choice is made
        if sales_choice == '1':
            view_sales()
        elif sales_choice == '2':
            data = get_sales_data()
            update_worksheet(data, "sales")
        elif sales_choice == '3':
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


#get sales function
def get_sales_data():
    """
    Get sales figures input from the user.

    Run a while loop to collect a valid string of data from the user
    via the terminal, which must be a string of 6 numbers separated
    by commas. The loop will repeatedly request data, until it is valid.
    """
    while True: # loop to request valid data
        print("Please enter sales data from the last market.")
        print("Data should be six numbers, separated by commas.")
        print("Example: 10,20,30,40,50,60\n") #"\n" gives spave for next line
    
        #declaring local variable
        data_str = input("Enter your data here:\n")
        sales_data = data_str.split(",") # this varible will split the string above to list
    #calling the validate function inside sales data fuction
    #validate_data(sales_data)

        if validate_data(sales_data):
            print("Data is valid!")
            break #break to end the while loop

    return sales_data

###################################
#get validate data function, to ensure collected data is valid
def validate_data(values):
    """
    Inside the try, 
    check if values are equal to exactly 6 inputs
    check if it converts all string values into integers.
    Raises ValueError if strings cannot be converted into int,
    or if there aren't exactly 6 values.
    """
    #print(values)
    try:
        [int(value) for value in values]
        if len(values) != 6:
            raise ValueError(
                f"Exactly 6 values required, you provided {len(values)}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False #return to end the while loop

    return True # 
    """
    adding this return true at the end of the validate_data function, 
    ensures that the function correctly informs the calling code (get_sales_data) 
    when the data is valid. This allows the get_sales_data function to print "Data is valid!" 
    and exit the loop.
    """

##########################################################################
#comment out repeated code
################################
#update sales function,  inserts data into our spreadsheet.  
#def update_sales_worksheet(data):
    """
    Update sales worksheet, add new row with the list data provided
    """
    """print("Updating sales worksheet...\n")
    sales_worksheet = SHEET.worksheet("sales")
    sales_worksheet.append_row(data)
    print("Sales worksheet updated successfully.\n")
    """


################################
# function to update the surplus worksheet
#def update_surplus_worksheet(data):
    """
    Update surplus worksheet, add new row with the list data provided
    """
    """
    print("Updating surplus worksheet...\n")
    surplus_worksheet = SHEET.worksheet("surplus")
    surplus_worksheet.append_row(data)
    print("Surplus worksheet updated successfully.\n")
    """


#mains functions, with function calls at the end
def main():
    """
    Run all program functions
    
    data = get_sales_data()
    sales_data = [int(num) for num in data]
    update_worksheet(sales_data, "sales")
    new_surplus_data = calculate_surplus_data(sales_data)
    update_worksheet(new_surplus_data, "surplus")
    sales_columns = get_last_5_entries_sales()
    stock_data = calculate_stock_data(sales_columns)
    update_worksheet(stock_data, "stock")

#print("Welcome to Baker's Heart Data Automation")
#this print  statement is the first thing we see, before the functions inside the main function are called. 



# Call main two functions
print_bakers_heart_logo()
main()"""
    
#########################################################################
#end of repeated code
########################################################################

###############################
def update_worksheet(data, worksheet):
    """
    Receives a list of integers to be inserted into a worksheet
    Update the relevant worksheet with the data provided
    """
    print(f"Updating {worksheet} worksheet...\n")
    worksheet_to_update = SHEET.worksheet(worksheet)
    worksheet_to_update.append_row(data)
    print(f"{worksheet} worksheet updated successfully\n")

    
###############################
# function to calculate the surplus data,  
def calculate_surplus_data(sales_row):
    """
    Compare sales with stock and calculate the surplus for each item type.
    The surplus is defined as the sales figure subtracted from the stock:
    - Positive surplus indicates waste
    - Negative surplus indicates extra made when stock was sold out.
    """
    print("Calculating surplus data...\n")
    stock = SHEET.worksheet("stock").get_all_values()
    """
    defined variable,to get the last line of  numbers from our stock worksheet here.
    """
    #pprint(stock)
    stock_row = stock[-1]
    print(stock_row)

    surplus_data = []
    for stock, sales in zip(stock_row, sales_row):
        """
        use the zip method to iterate  
        through two lists at the same time
        """
        surplus = int(stock) - sales
        """
        to convert the stock to integer, wrap this stock variable in the int() method
        it will return the converted integer,  and then we can subtract our sales value from it. 
        """
        surplus_data.append(surplus)
        #print(surplus_data)

    return surplus_data

############################
#function to   get the last 5 records for each sandwich.  
def get_last_5_entries_sales():
    """
    Collects columns of data from sales worksheet, collecting
    the last 5 entries for each sandwich and returns the data
    as a list of lists.
    """
    sales = SHEET.worksheet("sales")

    columns = []
    for ind in range(1, 7):
        column = sales.col_values(ind)
        columns.append(column[-5:])

    return columns
##############################

# function we’ll pass it the stock_data that our get_last_5_entries_sales function returned.

def calculate_stock_data(data):
    """
    Calculate the average stock for each item type, adding 10%
    """
    print("Calculating stock data...\n")
    new_stock_data = []

    for column in data:
        int_column = [int(num) for num in column] # converst the valuses into integers
        average = sum(int_column) / len(int_column)
        stock_num = average * 1.1
        new_stock_data.append(round(stock_num))

    return new_stock_data

#######################################################
    ##########. INVENTORY MENU SCREEN .############
#######################################################
# FUnction for sales menu
def inventory_menu():
    """
    Display the Inventory Menu and handle user choices.
    """
    while True:
        print("\nInventory Menu\n")
        print("1. View Inventory")
        print("2. Add Inventory")
        print("3. Back to Main Menu\n")

        inventory_choice = input("Enter your choice (1, 2, or 3):\n")
        clearScreen()# Clear the screen when a choice is made
        if inventory_choice == '1':
            view_inventory()
        elif inventory_choice == '2':
            data = get_inventory_data()
            update_worksheet(data, "sales")
        elif inventory_choice == '3':
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


#######################################################
    ##########. EXIT SCREEN .############
#######################################################

def print_goodbye_logo():
    """
    Prints a goodbye ASCII art logo.
    """
    print("\n")
    # List of lines that make up the ASCII art logo
    #Credit: https://ascii.today/
    goodbye_logo = """
     .d8888b.                         888 888                        
    d88P  Y88b                        888 888                        
    888    888                        888 888                        
    888         .d88b.   .d88b.   .d88888 88888b.  888  888  .d88b.  
    888  88888 d88""88b d88""88b d88" 888 888 "88b 888  888 d8P  Y8b 
    888    888 888  888 888  888 888  888 888  888 888  888 88888888 
    Y88b  d88P Y88..88P Y88..88P Y88b 888 888 d88P Y88b 888 Y8b.     
     "Y8888P88  "Y88P"   "Y88P"   "Y88888 88888P"   "Y88888  "Y8888  
                                                    888          
                                               Y8b d88P          
                                                "Y88P"          
    """

    print(goodbye_logo)
    print("\n")

#######################################################
    ##########. Main MANU .#################
#######################################################
  
#Mains functions, with function calls at the end
def main():
    """
    This the main Menu that will display after the ASCCI disappears and give user
    options to select
    """
    while True:
        print("This is Baker's Heart Data Automation. \n")
        time.sleep(1)
        typingPrint("Please choose from the Menu below.\n")
        time.sleep(1)
        print("\n")
        print("1. Sales Menu\n")
        print("2. Ingredients Inventory\n")
        print("3. Exit\n")

        choice = input("Enter your choice (1, 2, or 3):\n")
        clearScreen()# Clear the screen when a choice is made
        if choice == '1':
            # Call the sales menu or related functions
            print("Sales Menu selected.")
            sales_menu()
        elif choice == '2':
            # Call the ingredients inventory menu or related functions
            print("Ingredients Inventory selected.")
            inventory_menu()
        elif choice == '3':
            print("Exiting program. Goodbye!")
            print_goodbye_logo()
            time.sleep(5)  # Wait for 5 seconds
            clearScreen()
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

# Main loop to restart the program
while True:
    # Call main two functions
    print_bakers_heart_logo()
    main()


