# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import gspread #import the entire gspread library
from google.oauth2.service_account import Credentials # imports the Credentials class, which is part of the service_account  function from the Google auth library.  
from pprint import pprint

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

#sales = SHEET.worksheet('sales')
#this is to pull all values from the sales worksheet
#data = sales.get_all_values()
# this print statement will print out data to the terminal
#print(data)

####################################
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
        data_str = input("Enter your data here: ")
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
#########################################################################

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
#mains functions, with function calls at the end
def main():
    """
    Run all program functions
    """
    data = get_sales_data()
    sales_data = [int(num) for num in data]
    update_worksheet(sales_data, "sales")
    new_surplus_data = calculate_surplus_data(sales_data)
    update_worksheet(new_surplus_data, "surplus")


print("Welcome to Baker's Heart Data Automation")
"""
this print  statement is the first thing we see,  
before the functions inside the main function are called. 
"""
#main()
sales_columns = get_last_5_entries_sales()
