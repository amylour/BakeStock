# Testing for BakeStock  
  
## Validation  
The code was validated using the [Code Institute's](https://pep8ci.herokuapp.com/#) Pep8 Linter through its production. No errors were found in its final testing. The results are displayed below:
  
![Pep8 Linter Validation](documentation/readme/pep8validation.png)  
    
All user input has been validated regularly to ensure no dead ends for the user or acceptance of invalid user input. Opportunity for incorrect input should only be present when the user is prompted to record Sales, Batch or Inventory Data, which requires human precision to enter the new data. Any error in input is out of the control of the application and the clear input prompts which are printed for the user to see. This is discussed further in the [Manual Testing](#manual-testing) section below.

## Browser Testing  
BakeStock was tested through the Heroku app website on the following browsers with no issues arising:  
- Google Chrome (Version 110.0.5481.105)
- Mozilla Firefox (Version 109.0.1)  
- Microsoft Edge (Version Version 110.0.1587.5) 
    
BakeStock was tested on Safari using an iPad but user input was not recognised. I believe this to be a known issue with the Python template, as discovered whilst searching through the Code Institute's Slack archives. I did not have access to Safari on Desktop to check if this was a similar issue.  

Although I tested whether BakeStock would run on Android, which it did, there was no requirement to ensure that the application was responsive on all sizes of devices. As a result there is no Device Testing section to this project.
  
## Manual Testing  

### Testing User Stories  
  
  1. As a User, I want an attractive, engaging application. 
  2. As a User, I want to be provided with clear instructions throughout the application.
  3. As a User, I want to be able to record my Sales neatly, even if my baked items are different everyday.
  4. As a User, I want to be able to view my Sales records.
  5. As a User, I want to be able to clear my Sales data, should I need to.
  6. As a User, I want to be able to navigate back to the Main Menu.
  7. As a User, I want to be able to create and remove Batch records.
  8. As a User, I want to be able to view the Batches that I have left to bake.
  9. As a User, I want to be able to update my Batch records by item when a bake is complete.
  10. As a User, I want to be able to view my Ingredient Inventory.
  11. As a User, I want to be able to delete an Ingredient or Quantity.
  12. As a User, I want to be able to be able to update an Ingredient or Quantity.
  
    
## Bugs
- Colorama not working [Install pip colorama](https://tinyurl.com/msk3uknk)
- Colorama preventing app working in Heroku [requirements.txt](https://tinyurl.com/3bxmr4kj)  