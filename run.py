# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import gspread #import the entire gspread library
from google.oauth2.service_account import Credentials # imports the Credentials class, which is part of the service_account  function from the Google auth library.  

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

#get sales function
def get_sales_data():
    """
    Get sales figures input from the user.
    """
    print("Please enter sales data from the last market.")
    print("Data should be six numbers, separated by commas.")
    print("Example: 10,20,30,40,50,60\n") #"\n" gives spave for next line
    
    #declaring local variable
    data_str = input("Enter your data here: ")
    print(f"The data provided is {data_str}")

#calling the sales function at the end
get_sales_data()