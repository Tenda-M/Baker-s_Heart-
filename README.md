
# **Baker's Heart**

![Baker's Heart ascii art](documentation/readme/main_image.png) 

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
Accurate Sales Tracking:
- Enter and view sales data to monitor product performance and identify trends.
Efficient Inventory Management:
- Add, view, and update stock data to keep track of inventory levels and ensure adequate stock.
Surplus Calculation:
- Calculate and view surplus data to manage waste effectively and optimise production.
Ingredient Management:
- Manage the inventory of ingredients by adding new items, updating quantities, and deleting outdated items.
User-Friendly Interface:
- Interact with the system through an intuitive command line interface enhanced with ASCII art logos and typing effects for a pleasant user experience.

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
