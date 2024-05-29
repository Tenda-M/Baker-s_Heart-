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

# Import the pandas library
import pandas as pd  

# Import the tabulate library
from tabulate import tabulate  
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
    #print("Welcome to Baker's Heart Data Automation")

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
        clearScreen()
        print("\nSales Menu\n")
        print("1. View Sales Data")
        print("2. View Stock Data")
        print("3. View Sales vs Stock")
        print("4. Back to Main Menu\n")

        sales_choice = input("Enter your choice (1, 2, 3, or 4):\n")
        clearScreen()  # Clear the screen when a choice is made
        if sales_choice == '1':
            view_sales()
        elif sales_choice == '2':
            view_stock_data()
        elif sales_choice == '3':
            view_sales_vs_stock()
        elif sales_choice == '4':
            break
        else:
            print("\033[91mInvalid choice. Please enter 1, 2, 3, or 4.\033[0m")
            input("Press Enter to continue...")

# Function to view sales and edit
def view_sales():
    """
    View and manage sales data .
    """
    while True:
        clearScreen()
        print("\nSales Data Menu\n")
        print("1. View Sales Data")
        print("2. Add Sales Data")
        print("3. Return to Sales Menu\n")

        sales_choice = input("Enter your choice (1, 2, or 3):\n")
        clearScreen()  # Clear the screen when a choice is made

        if sales_choice == '1':
            print("Viewing sales data...\n")
            # Centering "CAKES" with a fixed width
            cakes_string = "CAKES"
            centered_cakes = cakes_string.center(40)
            print(centered_cakes)
            sales = SHEET.worksheet("sales").get_all_values()

            # Convert the sales data to a DataFrame for better display
            sales_df = pd.DataFrame(sales[1:], columns=sales[0])
            
            # Adjust the width of columns for better display
            pd.set_option('display.max_columns', None)  # Show all columns
            pd.set_option('display.max_colwidth', 20)   # Set column width

            print(tabulate(sales_df, headers='keys', tablefmt='grid', showindex=False))

            choice = input("\nWould you like to add sales data? Type 'y' for YES and 'n' to return to the Sales Data Menu:\n")
            if choice.lower() == 'y':
                clearScreen()
                print("Adding new sales data...\n")
                data = get_sales_data()
                update_worksheet(data, "sales")
                input("Sales data added successfully. Press Enter to return to the Sales Data Menu...")
                clearScreen()  # Clear the screen when a choice is made
                break
            elif choice.lower() == 'n':
                    clearScreen()
                    break
            else:
                    print("\033[91mInvalid choice. Please enter 'y' or 'n'.\033[0m")
                    input("Press Enter to continue to return to Sales Data Menu\n")

        elif sales_choice == '2':
            print("Adding new sales data...\n")
            data = get_sales_data()
            update_worksheet(data, "sales")
            input("Sales data added successfully. Press Enter to return to the Sales Data Menu...")
            clearScreen()  # Clear the screen when a choice is made

        elif sales_choice == '3':
            break

        else:
            print("\033[91mInvalid choice. Please enter 1, 2, or 3.\033[0m")
            input("Press Enter to continue...")
            clearScreen()  # Clear the screen when a choice is made


#Function to get sales data
def get_sales_data():
    """
    Get sales figures input from the user.

    Run a while loop to collect a valid string of data from the user
    via the terminal, which must be a string of 5 numbers followed by a date
    separated by commas. The loop will repeatedly request data, until it is valid.
    """
    while True:  # loop to request valid data
        print("Please enter sales data from the last market.")
        print("Data should be five numbers followed by a date (dd/mm/yyyy), separated by commas.")
        print("Example: 10,20,30,40,50,01/01/2024\n")  # "\n" gives space for next line

        # declaring local variable
        data_str = input("Enter your data here:\n")
        sales_data = data_str.split(",")  # this variable will split the string above to list

        if validate_sales_data(sales_data):
            print("Data is valid!")
            break  # break to end the while loop

    return sales_data

#Function
def validate_sales_data(values):
    """
    Inside the try,
    check if the first 5 values are integers and the last value is a valid date.
    Raises ValueError if strings cannot be converted into int,
    if there aren't exactly 6 values, or if the last value is not a valid date.
    """
    import datetime

    try:
        [int(value) for value in values[:-1]]  # Validate the first 5 values as integers
        if len(values) != 6:
            raise ValueError(
                f"Exactly 5 numbers and 1 date required, you provided {len(values)} values."
            )
        # Validate the last value as a date
        datetime.datetime.strptime(values[-1], '%d/%m/%Y')
    except ValueError as e:
        print(f"\033[91mInvalid data: {e}, please try again.\n\033[0m")
        return False  # return to end the while loop
    return True


#Function to view stock 
def view_stock_data():
    """
    View and manage stock data.
    """
    while True:
        clearScreen()
        print("\nStock Data Menu\n")
        print("1. View Stock Data")
        print("2. Add Stock Data")
        print("3. Return to Sales Menu\n")

        stock_choice = input("Enter your choice (1, 2, or 3):\n")
        clearScreen()  # Clear the screen when a choice is made

        if stock_choice == '1':
            print("Viewing stock data...\n")
            # Centering "CAKES" with a fixed width
            cakes_string = "CAKES"
            centered_cakes = cakes_string.center(40)
            print(centered_cakes)
            stock = SHEET.worksheet("stock").get_all_values()

            # Convert the stock data to a DataFrame for better display
            stock_df = pd.DataFrame(stock[1:], columns=stock[0])
            
            # Adjust the width of columns for better display
            pd.set_option('display.max_columns', None)  # Show all columns
            pd.set_option('display.max_colwidth', 20)   # Set column width

            print(tabulate(stock_df, headers='keys', tablefmt='grid', showindex=False))

            while True:
                choice = input("\nWould you like to add stock data? Type 'y' for YES and 'n' to return to the Stock Data Menu:\n")
                if choice.lower() == 'y':
                    clearScreen()
                    print("Adding new stock data...\n")
                    data = get_stock_data()
                    update_worksheet(data, "stock")
                    input("Stock data added successfully. Press Enter to return to the Stock Data Menu...")
                    clearScreen()  # Clear the screen when a choice is made
                    break
                elif choice.lower() == 'n':
                    clearScreen()
                    break
                else:
                    print("\033[91mInvalid choice. Please enter 'y' or 'n'.\033[0m")
                    input("Press Enter to continue...")

        elif stock_choice == '2':
            while True:
                print("Adding new stock data...\n")
                data = get_stock_data()
                if data is not None:
                    update_worksheet(data, "stock")
                    input("Stock data added successfully. Press Enter to return to the Stock Data Menu...")
                    clearScreen()  # Clear the screen when a choice is made
                    break
                else:
                    retry_choice = input("\033[91mInvalid stock data. Type 'r' to retry or 'n' to return to the Stock Data Menu:\033[0m\n")
                    if retry_choice.lower() == 'n':
                        clearScreen()
                        break

        elif stock_choice == '3':
            break

        else:
            print("\033[91mInvalid choice. Please enter 1, 2, or 3.\033[0m")
            input("Press Enter to continue...")
            clearScreen()  # Clear the screen when a choice is made

#Function to get stock data
def get_stock_data():
    """
    Get stock figures input from the user.

    Run a while loop to collect a valid string of data from the user
    via the terminal, which must be a string of 5 numbers followed by a date
    separated by commas. The loop will repeatedly request data, until it is valid.
    """
    while True:  # loop to request valid data
        print("Please enter stock data.")
        print("Data should be five numbers followed by a date (dd/mm/yyyy), separated by commas.")
        print("Example: 100,200,300,400,500,01/01/2024\n")  # "\n" gives space for next line

        # declaring local variable
        data_str = input("Enter your data here:\n")
        stock_data = data_str.split(",")  # this variable will split the string above to list

        if validate_stock_data(stock_data):
            print("Data is valid!")
            return stock_data  # return the valid data
        else:
            print("\033[91mInvalid data entered.\033[0m")
            return None  # return None if the data is invalid

    return stock_data


#Function to validate data
def validate_stock_data(values):
    """
    Inside the try,
    check if the first 5 values are integers and the last value is a valid date.
    Raises ValueError if strings cannot be converted into int,
    if there aren't exactly 6 values, or if the last value is not a valid date.
    """
    import datetime
    try:
        [int(value) for value in values[:-1]]  # Validate the first 5 values as integers
        if len(values) != 6:
            raise ValueError(
                f"Exactly 5 numbers and 1 date required, you provided {len(values)} values."
            )
        # Validate the last value as a date
        datetime.datetime.strptime(values[-1], '%d/%m/%Y')
    except ValueError as e:
        print(f"\033[91mInvalid data: {e}, please try again.\033[0m\n")
        return False

    return True


def view_sales_vs_stock():
    """
    View sales vs stock data.
    """
    clearScreen()  # Clear the terminal screen
    print("Viewing sales vs stock data...\n")
    # Centering "CAKES" with a fixed width
    cakes_string = "CAKES"
    centered_cakes = cakes_string.center(70)
    print(centered_cakes)
    sales = SHEET.worksheet("sales").get_all_values()  # Get all sales data from the worksheet
    stock = SHEET.worksheet("stock").get_all_values()  # Get all stock data from the worksheet

    # Calculate surplus data only for matching dates
    surplus_data = []
    headers = ["Date"] + sales[0][:-1]  # Create headers, excluding 'Date' from sales and adding 'Surplus'

    # Create dictionaries with date as key for both sales and stock data
    sales_dict = {row[-1]: row for row in sales[1:]}  # Use the last column (date) as the key for sales data
    stock_dict = {row[-1]: row for row in stock[1:]}  # Use the last column (date) as the key for stock data

    # Iterate through sales data to find matching dates in stock data
    for date, sales_row in sales_dict.items():
        if date in stock_dict:
            stock_row = stock_dict[date]
            surplus = []
            # Calculate the surplus for each item, excluding the date column
            for stock_value, sales_value in zip(stock_row[:-1], sales_row[:-1]):
                try:
                    surplus_value = int(stock_value) - int(sales_value)
                    surplus.append(str(surplus_value))
                except ValueError:
                    surplus.append("N/A")  # Handle non-integer values
            surplus_data.append([date] + surplus)  # Include the date in the surplus data

    if surplus_data:
        # Convert the surplus data to a DataFrame for better display
        surplus_df = pd.DataFrame(surplus_data, columns=headers)
        
        # Adjust the width of columns for better display
        pd.set_option('display.max_columns', None)  # Show all columns
        pd.set_option('display.max_colwidth', 20)   # Set column width

        # Print the surplus data in a tabulated format
        print(tabulate(surplus_df, headers='keys', tablefmt='grid', showindex=False))

        # Update surplus worksheet with the calculated data
        update_surplus_worksheet(surplus_data)
    else:
        print("No matching dates found between sales and stock data.")

    input("Press Enter to return to the Sales Menu...")
    clearScreen()  # Clear the screen when a choice is made

def update_surplus_worksheet(surplus_data):
    """
    Update the surplus worksheet with the calculated surplus data.
    """
    print("Updating surplus worksheet...\n")
    surplus_worksheet = SHEET.worksheet("surplus")

    # Clear the surplus worksheet before updating
    surplus_worksheet.clear()

    # Update the headers in the surplus worksheet
    headers = ["Date"] + ["Van", "Choc", "Berry", "Lemo", "Red"]
    surplus_worksheet.append_row(headers)

    # Append each surplus row to the surplus worksheet
    for row in surplus_data:
        surplus_worksheet.append_row(row)

    print("Surplus worksheet updated successfully.\n")

def calculate_surplus_data(sales_row):
    """
    Compare sales with stock and calculate the surplus for each item type.
    The surplus is defined as the sales figure subtracted from the stock:
    - Positive surplus indicates waste
    - Negative surplus indicates extra made when stock was sold out.
    """
    print("Calculating surplus data...\n")
    stock = SHEET.worksheet("stock").get_all_values()
    stock_row = stock[-1]  # Get the last row of stock data

    surplus_data = []
    for stock, sales in zip(stock_row, sales_row):
        try:
            surplus = int(stock) - int(sales)
        except ValueError:
            surplus = "N/A"  # Handle non-integer values
        surplus_data.append(surplus)

    return surplus_data

    """
    Compare sales with stock and calculate the surplus for each item type.
    The surplus is defined as the sales figure subtracted from the stock:
    - Positive surplus indicates waste
    - Negative surplus indicates extra made when stock was sold out.
    """
    print("Calculating surplus data...\n")
    stock = SHEET.worksheet("stock").get_all_values()
    stock_row = stock[-1]  # Get the last row of stock data

    surplus_data = []
    for stock, sales in zip(stock_row, sales_row):
        try:
            surplus = int(stock) - int(sales)
        except ValueError:
            surplus = "N/A"  # Handle non-integer values
        surplus_data.append(surplus)

    return surplus_data


###################################

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
        print("2. Manage Inventory")
        print("3. Back to Main Menu\n")

        inventory_choice = input("Enter your choice (1, 2, or 3):\n")
        clearScreen()# Clear the screen when a choice is made
        if inventory_choice == '1':
            view_inventory()
        elif inventory_choice == '2':
            manage_inventory()
        elif inventory_choice == '3':
            break
        else:
            print("\033[91mInvalid choice. Please enter 1, 2, or 3.\033[0m")


#Function for inventory list
def view_inventory():
    """
    Display current inventory List
    """
    clearScreen()
    print("Viewing inventory data...\n")
    inventory = SHEET.worksheet("inventory").get_all_values()
    # Print the inventory data in a table format
    # Credit: https://stackoverflow.com/questions/71389140/python-tablulate-headers-and-grid-lines
    print(tabulate(inventory, headers="firstrow", tablefmt="grid"))
    #for row in inventory:
    #    print(row)
    input("Press Enter to return to the Inventory Menu...")
    clearScreen()  # Clear the screen when a choice is made

#Function to manage inventory
def manage_inventory():
    """
    Display options to manage inventory: Add, Delete, Update, or Return to Inventory Menu.
    """
    while True:
        clearScreen()
        print("\nManage Inventory\n")
        print("1. Add New Ingredient")
        print("2. Delete Ingredient")
        print("3. Update Ingredient Name or Quantity")
        print("4. Return to Inventory Menu\n")

        manage_choice = input("Enter your choice (1, 2, 3, or 4):\n")
        clearScreen()  # Clear the screen when a choice is made
        if manage_choice == '1':
            add_new_ingredient()
        elif manage_choice == '2':
            delete_ingredient()
        elif manage_choice == '3':
            update_ingredient()
        elif manage_choice == '4':
             break  # Return to Inventory Menu
        else:
            print("\033[91mInvalid choice. Please enter 1, 2, 3, or 4.\033[0m")
            input("Press Enter to continue...")


#Function to add ingredients
def add_new_ingredient():
    """
    Add a new ingredient to the inventory.
    """
    while True:
        clearScreen()  # Clear the screen when a choice is made
        print("Please add a new ingredient\n")
        
        while True:
            name = input("Enter the name of the new ingredient (e.g., coco(g)):\n")
            if all(char.isalpha() or char.isspace() or char in "()[]" for char in name.replace(' ', '')):
                break
            else:
                print("\033[91mInvalid name. Please enter a valid ingredient name containing only alphabetic characters and allowed symbols ((), []).\033[0m")
                input("Press Enter to try again...")

        while True:
            quantity = input("Enter the quantity of the new ingredient:\n")
            if quantity.isdigit():
                break
            else:
                print("\033[91mInvalid quantity. Please enter a number.\033[0m")
                input("Press Enter to try again...")

        # Append the new ingredient to the inventory sheet
        inventory_sheet = SHEET.worksheet("inventory")
        inventory_sheet.append_row([name, quantity])

        print(f"Ingredient '{name}' with quantity '{quantity}' added successfully.\n")
        print("\nUpdated Inventory List:")
        view_inventory()
        
        while True:
            choice = input("Would you like to add another ingredient? Type 'y' for YES and 'n' for NO:\n")
            if choice.lower() == 'y':
                break
            elif choice.lower() == 'n':
                clearScreen()
                input("Press Enter to return to Manage Inventory...")
                clearScreen()  # Clear the screen when a choice is made
                return
            else:
                print("\033[91mInvalid choice. Please enter 'y' for YES or 'n' for NO.\033[0m")
                input("Press Enter to try again...")

    clearScreen()  # Clear the screen when a choice is made

    input("Press Enter to return to Manage Inventory...")
    clearScreen()  # Clear the screen when a choice is made

     


#function to delete ingredient
def delete_ingredient():
    """
    Delete an ingredient from the inventory list.
    """
    while True:
        clearScreen()
        print("Delete Ingredient\n")
        ingredient_name = input("Enter the name of the ingredient to delete:\n")

        # Find the ingredient in the inventory sheet and delete the row
        inventory_sheet = SHEET.worksheet("inventory")
        ingredients = inventory_sheet.get_all_values()

        found = False  # Flag to track if ingredient is found

        for idx, ingredient in enumerate(ingredients):
            # Convert to str to ensure the code handles both numbers and words properly
            if str(ingredient[0]).strip().lower() == ingredient_name.strip().lower():
                inventory_sheet.delete_rows(idx + 1)
                print(f"Ingredient '{ingredient_name}' deleted successfully.")
                found = True
                break

        if not found:
            print(f"\033[91mIngredient '{ingredient_name}' not found.\033[0m")
            input("Press Enter to try again...")

        print("\nUpdated Inventory List:")
        view_inventory()

        while True:
            choice = input("Would you like to delete another ingredient? Type 'y' for YES and 'n' for NO:\n")
            if choice.lower() == 'y':
                break
            elif choice.lower() == 'n':
                clearScreen()
                return
            else:
                print("\033[91mInvalid choice. Please enter 'y' for YES or 'n' for NO.\033[0m")
                input("Press Enter to try again...")

    clearScreen()  # Clear the screen when a choice is made
    


#Function to update ingredient list
 # Function to update ingredient list
def update_ingredient():
    """
    Update an ingredient's name or quantity.
    """
    while True:
        clearScreen()
        print("Update Ingredient\n")
        ingredient_name = input("Enter the name of the ingredient to update:\n")

        # Find the ingredient in the inventory sheet
        inventory_sheet = SHEET.worksheet("inventory")
        ingredients = inventory_sheet.get_all_values()

        for idx, ingredient in enumerate(ingredients):
            if str(ingredient[0]).strip().lower() == str(ingredient_name).strip().lower():
                print(f"Current name: {ingredient[0]}, Current quantity: {ingredient[1]}")
                new_name = input("Enter new name (leave blank to keep current name):\n")
                new_quantity = input("Enter new quantity (leave blank to keep current quantity):\n")

                if new_name:
                    ingredient[0] = new_name
                if new_quantity:
                    ingredient[1] = new_quantity

                inventory_sheet.update(range_name=f'A{idx + 1}:B{idx + 1}', values=[ingredient])
                print(f"Ingredient '{ingredient_name}' updated successfully.")
                break
        else:
            print(f"\033[91mIngredient '{ingredient_name}' not found.\033[0m")
            input("Press Enter to continue...")

        print("\nUpdated Inventory List:")
        view_inventory()

        while True:
            choice = input("Would you like to update another ingredient? Type 'y' for YES and 'n' for NO:\n")
            if choice.lower() == 'y':
                break
            elif choice.lower() == 'n':
                clearScreen()
                input("Press Enter to return to Manage Inventory...")
                clearScreen()  # Clear the screen when a choice is made
                return
            else:
                print("\033[91mInvalid choice. Please enter 'y' for YES or 'n' for NO.\033[0m")
                input("Press Enter to try again...")

    clearScreen()  # Clear the screen when a choice is made



#######################################################
    ##########. EXIT SCREEN .############
#######################################################
def print_goodbye_logo():
    """
    Prints a goodbye ASCII art logo and terminates the program.
    """
    print("\n")
    # List of lines that make up the ASCII art logo
    # Credit: https://ascii.today/
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
    sys.exit()  # Terminate the program

#######################################################
    ##########. MAIN MENU .#################
#######################################################
  
def main():
    """
    This is the main Menu that will display after the ASCII disappears and gives users
    options to select.
    """
    while True:
        print("Welcome Baker's Heart bakery. \n")
        time.sleep(1)
        typingPrint("Please choose from the Menu below.\n")
        time.sleep(1)
        print("\n")
        print("1. Sales Menu\n")
        print("2. Ingredients Inventory\n")
        print("3. Exit\n")

        choice = input("Enter your choice (1, 2, or 3):\n")
        clearScreen()  # Clear the screen when a choice is made
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
            print("\033[91mInvalid choice. Please enter 1, 2, or 3.\033[0m")

# Main execution
print_bakers_heart_logo()
main()
