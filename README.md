
# **Baker's Heart**

![Baker's Heart ascii art](/documentation/readme/main_image.png) 

Baker's Heart is a Python command line interface (CLI) application designed for efficient sales and inventory management in a bakery setting. It allows users to view, add, and update sales and stock data, ensuring accurate tracking of inventory levels. The application provides detailed tabulated views of sales and stock, calculates surplus data for better waste management, and checks for low stock to prevent shortages. With features to manage ingredients, the program enhances operational efficiency. The ASCII art logos and typing effect enhance user interaction, making the application user-friendly and visually appealing.


View the live application here: [Baker's Heart](https://bakers-heart-b9b8b5bfd9a7.herokuapp.com/)  

Google Sheets Sales, surplus, stock and Inventory Data (view only) [here.](https://docs.google.com/spreadsheets/d/17wg0BMZQo8cI_MWcDCm8S6tk35mrxapXJOLnCT-UnFo/edit#gid=1071172766)

## Contents
* [**User Experience/User Interface (UX/UI)**](#user-experienceuser-interface-uxui)
  * [User Goals](#user-goals)
  * [User Stories](#user-stories)
* [**Creation process**](#creation-process)
  * [Project Planning](#project-planning)
  * [Flowchart](#flowchart)
  * [Google API SetUp](#google-api-setup)
  * [Python Logic](#python-logic)
  * [Data Model - Google Sheets](#data-model---google-sheets)
  * [Design Choices](#design-choices)
* [**Features**](#features)
  * [How to Use BakeStock](#how-to-use-bakestock)
  * [Future Features](#future-features)
* [**Technologies Used**](#technologies-used)
* [**Libraries & Packages**](#libraries--packages)
* [**Testing**](#testing)
* [**Creation & Deployment**](#creation--deployment)
* [**Credits**](#credits) 

# User Experience/User Interface (UX/UI)  
  
## User Goals
1. Accurate Sales Tracking:
   Enter and view sales data to monitor product performance and identify trends.
2. Efficient Inventory Management:
   Add, view, and update stock data to keep track of inventory levels and ensure adequate stock.
3. Surplus Calculation:
   Calculate and view surplus data to manage waste effectively and optimise production.
4. Ingredient Management:
   Manage the inventory of ingredients by adding new items, updating quantities, and deleting outdated items.
5. User-Friendly Interface:
   Interact with the system through an intuitive command line interface enhanced with ASCII art logos and typing effects for a pleasant user experience.

## User Stories 
These user stories aim to cover the essential functionalities required for managing the inventory and sales data of Baker's Heart effectively.

1. As a bakery manager, I want to view the current inventory levels, so that I can check the availability of ingredients.

2. As a bakery manager, I want to add new ingredients to the inventory, so that I can keep track of all the ingredients we have in stock.

3. As a bakery manager, I want to update the quantity of existing ingredients, so that the inventory reflects the actual stock levels after purchases or usage.

4. As a bakery manager, I want to delete ingredients from the inventory, so that obsolete or unused items do not clutter the inventory list.

5. As a bakery manager, I want to view sales data, so that I can analyse the sales performance of different products.

6. As a bakery manager, I want to add new sales data, so that I can keep the records up to date with the latest sales figures.

7. As a bakery manager, I want to compare sales data with stock levels, so that I can identify surplus or shortage of ingredients.

8. As a bakery manager, I want to update ingredient names and quantities, so that any changes or corrections can be made accurately.

9. As a bakery manager, I want the system to validate the data I enter, so that errors are minimised, and the data integrity is maintained.

10. As a bakery manager, I want a clear and simple user interface, so that I can easily navigate through different menus and perform tasks efficiently. 

# Creation Process    
  
## Project Planning  
 As a home baker, I often relied on my notebook to keep track of ingredient inventory, sales, and customer orders. While this worked for small-scale operations, it became increasingly cumbersome as my business grew. I imagined how a digital system could streamline these processes, making it easier to manage stock, record sales, and fulfil customer orders efficiently. Many other bakers likely face similar challenges, struggling with the manual recording of essential business information. This project aims to develop a comprehensive digital tool that addresses these issues, offering a practical solution for bakers to maintain accurate records, ensure smooth operations, and ultimately, grow their businesses. 

  Project Planning and Use of Lucidchart

To effectively plan and visualise the Baker's Heart project, I utilised [Lucidchart](https://www.lucidchart.com/) to create detailed flowcharts. Lucidchart is a powerful tool that allows for the easy creation of diagrams and flowcharts, making it ideal for mapping out the structure and functionality of the application. Here’s how Lucidchart was instrumental in the planning process:

1. Identifying Key Features:
The first step was to identify the key features the application needed, such as inventory management, sales tracking, and customer order management. Lucidchart allowed me to create a high-level overview of these features, ensuring all essential components were included.

2. Flowchart Creation:
I created flowcharts to detail the process flows within the application. For example, the flowchart for inventory management illustrated how users could add, update, or delete ingredients, and how the system would check for low stock levels.
Another flowchart mapped out the sales process, from recording sales data to comparing sales with stock levels and calculating surplus or deficit.

3. User Interaction Mapping:
Lucidchart helped in visualising user interactions with the system. This included how users would navigate through different menus, input data, and receive feedback from the system.
The flowcharts depicted user paths, making it easier to design a user-friendly interface.

4. Data Flow Diagrams:
Data flow diagrams were created to show how information would move between different parts of the system. This ensured that data integrity was maintained and that all parts of the application were well-integrated.

5. Iterative Design and Feedback:
Using Lucidchart made it easy to update and refine the flowcharts based on feedback and new ideas. This iterative process ensured that the final design was robust and met all the requirements.

By using Lucidchart for planning, I was able to create a clear and organised visual representation of the Baker's Heart project. This not only facilitated better understanding and communication of the project’s scope and functionality but also helped in identifying potential issues early in the design phase, leading to a more efficient development process. 


## Flowchart   
ADD IMAGE

<br>  

## Google API SetUp  
Before writing any function code, it was essential to set up the relevant credentials and API connections. This process is outlined in the Creation & Deployment section. Ensuring security was crucial, especially when connecting a Google Account—created specifically for this project—to access the Google Sheets worksheet. Careful steps were taken to prevent sensitive files, such as CREDS.json, from being exposed publicly. The setup of these authorisations and credentials was guided by the Code Institute's Full Stack Software Development course.

Google Sheets was used to store user data, which was accessed, manipulated, and updated as needed. It functioned as a simulated database, ensuring that users would not directly interact with the actual worksheets. Instead, all data entry and manipulation occurred within the terminal. 

Clear instructions are provided in the terminal to guide the user on how to enter data correctly. These instructions ensure that the data is displayed accurately in the output, adhering to the scope and requirements of the project. The terminal prompts are designed to be user-friendly, making the data entry process straightforward and minimising the chances of errors. This approach ensures that the user can interact with the system efficiently, and that the data entered is properly formatted and processed within the project's framework. 

## Python Logic 
For Baker's Heart, I adopted a similar approach to ensure a seamless and functional application. The primary objective was to create a system that accessed, displayed, and edited data from Google Sheets, effectively simulating a database. Recognising the limits of my knowledge with the gspread library, I continually adjusted the scope.

I started by developing simple functions to guide user input through the application. Using if/elif statements, I constructed menus and employed while loops and try/except blocks to validate user input, ensuring robust error handling and user guidance.

From these basic menus, I built smaller functions to manage the flow and manipulation of data. The enumerate() function was particularly useful in pulling data from specific matched locations in the worksheets, ensuring that user input was validated and accurately reflected in the data. Regular testing of these validation functions was critical to maintaining the integrity of the application.

Once a section of the application was confirmed to function correctly, I explored the potential for code reuse in other sections with similar requirements. This approach helped streamline development and maintain consistency. However, some sections required personalised code, especially concerning data display. For instance, I used the Python zip() function for parallel iteration when displaying Inventory data.

By employing these strategies, I ensured that Baker's Heart remained a functional, user-friendly application, effectively simulating a real-world database interaction through Google Sheets.


<br>  

## Data Model - Google Sheets
The user data is inputted into the respective Google Sheets worksheets. Each worksheet is accessible only by me as the Editor, but a View-only link will be provided to demonstrate the data distribution for the project. [Google Worksheets](https://docs.google.com/spreadsheets/d/17wg0BMZQo8cI_MWcDCm8S6tk35mrxapXJOLnCT-UnFo/edit#gid=1071172766)


- Sales Worksheet: Stores detailed records of all sales data entered by the user, ensuring accurate tracking and analysis of sales performance.
[Sales data](/documentation/readme/sales_data.png) 

- Stock Worksheet: Maintains current stock levels, allowing for real-time monitoring and management of inventory.
[Stock data](/documentation/readme/stock_data.png)

- Surplus Worksheet: Records surplus data, indicating the difference between stock and sales to help manage waste and production needs.
[Surplus data](/documentation/readme/surplus_data.png)

- Inventory Worksheet: Lists all ingredients along with their quantities, facilitating efficient inventory management and restocking. 
[Inventory data](/documentation/readme/inventory_data.png)

Design Choices
*****EDIT*******


# Features

## How to Use Baker's Heart
Navigating to the Main Menu and Using Baker's Heart

Navigating to the Main Menu:
- Start the Application:
    Launch the Baker's Heart application in your terminal. The program will begin with a welcome screen displaying the Baker's Heart logo and a brief introduction.

    Proceed to the Main Menu:
    After the welcome screen, you will be directed to the Main Menu. This menu serves as the central hub for navigating the application's features.

### Main Menu 

Using the Main Menu:

The Main Menu presents three primary options, each corresponding to a specific aspect of the Baker's Heart application:

    Sales Menu:
        Select this option by entering '1' and pressing Enter.
        This menu allows you to view sales data, add new sales records, and compare sales data with stock levels.

    Ingredients Inventory:
        Select this option by entering '2' and pressing Enter.
        Here, you can view the current inventory, manage ingredients (add, delete, or update), and check for low stock alerts.

    Exit:
        Select this option by entering '3' and pressing Enter.
        This will terminate the application, displaying a goodbye message before exiting.

    ![Main Menu screenshot](/documentation/readme/main_menu.png) 

### Sales Menu 

Sales Menu:

1. View Sales Data: Displays and edit sales data in a tabulated format.
2. Add Stock Data: Displays and edit sales data in a tabulated format.
3. View Sales vs Stock: Compares sales data with stock levels, calculating and displaying any surplus.
4. Return to main menu:

![Sales menu screenshot](/documentation/readme/sales_menu.png)

### Using the sales menu
        
At the Main Menu, type '1' and press Enter to navigate to the Sales Menu.
The Sales Menu provides several options for managing and viewing your sales data:

   #### View Sales Data Menu
        Select this option by entering '1' and pressing Enter.
        This menu provides sub-options menu view, add, and return to sales data menu.
        ![View Sales Data Menu screenshot](/documentation/readme/sales_data_menu.png)

    1. View sales data:
        This will display the current sales data in a tabulated format, showing details such as item names, quantities sold, and dates.
        ![View sales data screenshot](/documentation/readme/sales_cake_data.png)

        After viewing the sales data, you will have the option to add new sales data.
            If you choose to add new sales data, you will be prompted to enter sales figures for five items followed by a date (e.g., 10,20,30,40,50,01/01/2024).
            The new sales data will be added to the sales worksheet, and you will return to the Sales Data Menu.
            Press Enter to return to the Sales Data Menu after viewing the sales data.
            ![Add Sales Data screenshot](/documentation/readme/add_cake_data.png)

    2. Add Sales Data:
        Select this option by entering '2' and pressing Enter.
        You will be prompted to enter sales figures for five items followed by a date (e.g., 10,20,30,40,50,01/01/2024).
        The new sales data will be validated and added to the sales worksheet.
        After successfully adding the sales data, you will return to the Sales Data Menu.
        ![Add Sales Data screenshot](/documentation/readme/add_cake_data.png)
    
    3. Return to sales data menu:
       Select this option by entering '3' and pressing Enter.
        This will take you back to the sales data Menu.

   #### View Stock Data Menu
    In the Sales Menu, type '2' and press Enter to view the stock data.
    This menu provides sub-options menu view, add, and return to stock data menu.
    ![View Stock Data Menu screenshot](/documentation/readme/stock_data_menu.png)

    1. Viewing Current Stock Data:
    Once you select to view the stock data, the application will display the current stock data in a neatly formatted table. The table will show details such as item names and quantities in stock.
    ![Viewing Current Stock screenshot](/documentation/readme/stock_cake_data.png)
 
    After viewing the stock data, you will be prompted with an option to add new stock data.
    If you wish to add new stock data, type 'y' and press Enter. If you do not wish to add new stock data, type 'n' and press Enter to return to the Stock Data Menu.
    ![Adding New Stock Data screenshot](/documentation/readme/add_stock_data.png)

    2. Adding New Stock Data:

    If you choose to add new stock data, you will be prompted to enter stock figures for five items followed by a date.
    Enter the data in the following format: quantity1,quantity2,quantity3,quantity4,quantity5,date (e.g., 100,200,300,400,500,01/01/2024).
    ![Adding New Stock Data screenshot](/documentation/readme/add_stock_data.png)

   3. Returning to the Stock Data Menu:

    After successfully adding the new stock data, you will be returned to the Stock Data Menu.
    Press Enter to return to the Stock Data Menu after viewing or adding stock data.

  #### View Sales vs Stock Menu
    View Sales vs Stock:
        Select this option by entering '3' and pressing Enter.
        This option compares sales data with stock data to calculate surplus for matching dates.
        The surplus data will be displayed in a tabulated format, showing the difference between stock and sales for each item on matching dates.
        If no matching dates are found, an appropriate message will be displayed.
        Press Enter to return to the Sales Menu after viewing the sales vs stock data.
    ![View Sales vs Stock screenshot](/documentation/readme/sales_vs_stock.png)

    Return to Main Menu:
        Select this option by entering '4' and pressing Enter.
        This will take you back to the Main Menu.

### Ingredients Inventory Menu

Ingredients Inventory:

View Inventory: Shows the current inventory list with ingredient names and quantities.
Manage Inventory: Provides sub-options to add, delete, or update ingredients.
1. View Inventory: Inventory is displayed.
2. Manage Inventory : Modify the inventory.
3. Return to main menu:
![Ingredients Inventory menu screenshot](/documentation/readme/inventory_menu.png)

### Using Ingredients Inventory menu

#### View Inventory:
Select this option by entering '1' and pressing Enter.
This will display the current inventory list, showing ingredient names and quantities in a tabulated format.
Press Enter to return to the Inventory Menu after viewing the inventory.
![Inventory display screenshot](/documentation/readme/inventory_data.png)

#### Manage Inventory:
Select this option by entering '2' and pressing Enter.
This menu provides sub-options menu to add, delete, or update ingredients in your inventory.
![Manage Inventory manu screenshot](/documentation/readme/manage_inventory.png)

    1. Add New Ingredient:
            Enter '1' to add a new ingredient.
            You will be prompted to enter the name of the new ingredient. Ensure the name contains only alphabetic characters and allowed symbols ((), []).
            Next, enter the quantity of the new ingredient as a number.
            The new ingredient will be added to the inventory, and the updated inventory list will be displayed.
            You can choose to add another ingredient or return to the Manage Inventory menu.
            [Add New Ingredient screenshot](/documentation/readme/add_ingredient.png)

    2. Delete Ingredient:
            Enter '2' to delete an ingredient.
            You will be prompted to enter the name of the ingredient you wish to delete.
            If the ingredient is found, it will be removed from the inventory, and the updated inventory list will be displayed.
            If the ingredient is not found, an alert will be displayed, and you will be prompted to try again.
            You can choose to delete another ingredient or return to the Manage Inventory menu.
            [Delete Ingredient screenshot](/documentation/readme/delete_ingredient.png)

    3. Update Ingredient Name or Quantity:
            Enter '3' to update an ingredient.
            You will be prompted to enter the name of the ingredient you wish to update.
            If the ingredient is found, you can enter a new name (or leave blank to keep the current name) and a new quantity (or leave blank to keep the current quantity).
            The ingredient details will be updated, and the updated inventory list will be displayed.
            If the ingredient is not found, an alert will be displayed, and you will be prompted to try again.
            You can choose to update another ingredient or return to the Manage Inventory menu.
            [Update Ingredient screenshot](/documentation/readme/update_ingredient.png)

#### Return to Main Menu:
    Select this option by entering '3' and pressing Enter.
    This will take you back to the Main Menu.

### Using Exit:
        Selecting this option will end the application. Ensure you have saved any changes before exiting.

By following these steps, you can effectively navigate and utilize the Baker's Heart application to manage sales and inventory efficiently.

### Error Handling and Clear 

    Input Validation:
        The program extensively validates user input to ensure it meets the required format and criteria.
        For instance, when entering sales data, the program checks if the input contains five numbers followed by a date in the correct format. If the input is invalid, an error message is displayed, and the user is prompted to try again.
        [Invalid data screenshot](/documentation/readme/invalid_data.png)

    Try/Except Blocks:
        The program uses try/except blocks to handle potential errors gracefully. For example, when converting input values to integers, if the conversion fails, the program catches the error and provides a clear error message to the user.

    Clear Error Messages:
        Whenever an error occurs, the program provides clear and specific error messages. This helps users understand what went wrong and how to correct their input.
        [Invalid option screenshot](/documentation/readme/invalid_option.png)

   Clear Screen Function:
    The clearScreen() function is used to clear the terminal screen before displaying new content. This helps maintain a clean and organized display, making it easier for users to focus on the current task.
    The function is called at the beginning of each menu or sub-menu to ensure that previous outputs and inputs are cleared.

-----  

<br>

## Future Features  

Batch Management and Tracking:
Introduce batch management features to track production batches, expiry dates, and batch-specific sales.

Inventory Alerts and Notifications:
 Add automated alerts and notifications for low stock levels, upcoming expiration dates, or reorder points. Allow users to set custom thresholds for notifications, ensuring timely restocking and reducing waste.

Enhanced Reporting and Analytics:
Introduce detailed reporting features that generate visual charts and graphs for sales, stock levels, and inventory trends.














¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨
![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome,

This is the Code Institute student template for deploying your third portfolio project, the Python command-line project. The last update to this file was: **March 14, 2023**

## Reminders

- Your code must be placed in the `run.py` file
- Your dependencies must be placed in the `requirements.txt` file
- Do not edit any of the other files or your code may not deploy properly

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

---

Happy coding!
