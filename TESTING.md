# Testing for Baker's Heart   
  
## Testing Contents  
  
1. [Validation](#validation)
2. [Browser Testing](#browser-testing)
3. [Manual Testing](#manual-testing)
4. [Bugs](#bugs)  
  
-----
## Validation  
The code was validated using the [Code Institute's](https://pep8ci.herokuapp.com/#) during its development. No errors were found in the final testing, as shown below:
![Pep8 Linter Validation](/documentation/readme/pep8validation.png)

## User Input Validation  
In Baker's Heart, robust user input validation ensures data integrity and a seamless user experience. Here are the key validation techniques employed in the application:

    Type Checking:
        Numerical Inputs: For inputs that require numerical values, the program checks if the input is a valid integer or float. If the input is not a valid number, an error message is displayed, and the user is prompted to enter the data again.
        String Inputs: For inputs that should be strings (like ingredient names), the program ensures that the input contains only alphabetic characters and allowed symbols ((), []).

    Format Validation:
        Date Inputs: Dates are checked to ensure they follow the correct format (dd/mm/yyyy). This is crucial for maintaining consistency in date-related operations and ensuring that date comparisons are accurate.

    Range Checking:
        When inputs must fall within a specific range (e.g., quantities must be positive numbers), the program ensures that the input values meet these criteria before proceeding. If the input is outside the allowed range, an error message is displayed.

    Mandatory Fields:
        Certain inputs are mandatory, and the user cannot proceed without providing these. The program prompts the user until valid data is entered.

    Custom Error Messages:
        Clear and specific error messages are provided to guide the user in correcting their inputs. These messages help users understand what went wrong and how to fix it.

| Feature                    | Tested?  | User Feedback Provided                                    |
|----------------------------|----------|-----------------------------------------------------------|
| Main Menu                  | Yes      | Invalid input. Enter number for Menu choice               |
| View Sales Data            | Yes      | Invalid input for dates. Ensure format is dd/mm/yyyy      |
| Add Sales Data             | Yes      | Invalid input for sales figures. Ensure all entries are numbers |
| View Stock Data            | Yes      | Invalid input for dates. Ensure format is dd/mm/yyyy      |
| Add Stock Data             | Yes      | Invalid input for stock figures. Ensure all entries are numbers |
| Update Ingredient          | Yes      | Ingredient not found. Ensure name matches exactly         |
| Delete Ingredient          | Yes      | Ingredient not found. Ensure name matches exactly         |
| Add New Ingredient         | Yes      | Invalid name. Enter only alphabetic characters and allowed symbols ((), []) |
| View Inventory             | Yes      | No specific feedback required                             |
| Check Low Stock            | Yes      | No specific feedback required                             |
| View Sales vs Stock Data   | Yes      | No matching dates found. Ensure dates are correct         |
| Update Surplus Worksheet   | Yes      | Surplus worksheet updated successfully                    |
| Validate Sales Data        | Yes      | Invalid data. Enter five numbers followed by a date       |
| Validate Stock Data        | Yes      | Invalid data. Enter five numbers followed by a date       |
| Clear Screen               | Yes      | Screen cleared successfully                               |
| Exit Program               | Yes      | Program exited successfully                               |

----- 

## Browser Testing 
BakeStock was tested on the Heroku app website across multiple browsers, including Google Chrome, Mozilla Firefox, and Safari, without encountering any issues.

## Manual Testing  

### Testing User Stories 
This table summarises the manual testing of the Baker's Heart application against its key user stories. Each feature was tested thoroughly to ensure it meets the user's needs, with feedback provided based on the testing outcomes.

| User Story                                                                                                                                  | Feature                              | Tested? | User Feedback Provided                                 |
|---------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------|---------|--------------------------------------------------------|
| 1. As a bakery manager, I want to view the current inventory levels, so that I can check the availability of ingredients.                       | View Inventory Levels                | Yes     | Clear display of inventory data.                       |
| 2. As a bakery manager, I want to add new ingredients to the inventory, so that I can keep track of all the ingredients we have in stock.       | Add New Ingredients                  | Yes     | Prompt feedback on successful addition.                |
| 3. As a bakery manager, I want to update the quantity of existing ingredients, so that the inventory reflects the actual stock levels.         | Update Ingredient Quantity           | Yes     | Accurate reflection of updated quantities.             |
| 4. As a bakery manager, I want to delete ingredients from the inventory, so that obsolete or unused items do not clutter the inventory list.    | Delete Ingredients                   | Yes     | Confirmation of deletion with updated inventory view.  |
| 5. As a bakery manager, I want to view sales data, so that I can analyse the sales performance of different products.                           | View Sales Data                      | Yes     | Comprehensive sales data display.                      |
| 6. As a bakery manager, I want to add new sales data, so that I can keep the records up to date with the latest sales figures.                  | Add New Sales Data                   | Yes     | Easy addition with immediate confirmation.             |
| 7. As a bakery manager, I want to compare sales data with stock levels, so that I can identify surplus or shortage of ingredients.              | Compare Sales Data with Stock Levels | Yes     | Clear comparison with surplus/shortage identification. |
| 8. As a bakery manager, I want to update ingredient names and quantities, so that any changes or corrections can be made accurately.            | Update Ingredient Names and Quantities| Yes    | Smooth updating process with confirmation messages.    |
| 9. As a bakery manager, I want the system to validate the data I enter, so that errors are minimised, and the data integrity is maintained.     | Data Validation                      | Yes     | Effective error handling and feedback.                 |
| 10. As a bakery manager, I want a clear and simple user interface, so that I can easily navigate through different menus and perform tasks efficiently. | User Interface Navigation            | Yes     | Intuitive and user-friendly navigation.                |


<br>

## Bugs 
Here are some bugs we found and fixed during the development of Baker's Heart:
1. Bug: Deleting Non-existent Ingredients
Issue: The program did not handle cases where users tried to delete ingredients that didn't exist in the inventory.
Fix: Added checks to confirm the ingredient's existence before attempting to delete it and provided appropriate feedback if it wasn't found.

2. Bug: Displaying Sales Data
Issue: Sales data display was misaligned, making it difficult to read.
Fix: Adjusted the formatting using the tabulate library to ensure clear and readable output.

3. Bug: Synchronisation between Sales and Stock Data
Issue: Inconsistent data synchronisation between sales and stock data could lead to inaccurate surplus calculations.
Fix: Implemented functions to ensure both datasets are accurately matched by date before calculations.

4. Bug: Inconsistent Updates to Inventory
 Issue: Updates to ingredient names or quantities were not consistently reflected in the inventory.
 Fix: Ensured that updates are properly saved to the Google Sheets and confirmed with the user.


<br>  

## Known Bugs  
After rigorous testing, there are no known bugs in the code.

