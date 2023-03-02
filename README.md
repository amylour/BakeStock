# **BakeStock**
  

![bakestock ascii art](documentation/readme/main_image.png)  


BakeStock is a Python command line interface (CLI) application designed to be used by hobby or 'small-batch' bakers. The application will allow the user to keep track of daily bakes and sales, batch numbers, and keep track of ingredient types and inventory levels. It is fully customisable and editable to allow the user to change their bakes and inventory items through multiple menus.

View the live application here: [BakeStock](https://bakestock.herokuapp.com/)  

Google Sheets Sales, Batch, Inventory Data (view only) [here.](https://docs.google.com/spreadsheets/d/1ny_lvzMpPjMDCl1ET9uSyVTzBcJko1QDY6DXggS_y5s/edit?usp=sharing)


## Contents
* [**User Experience - UX**](#user-experience-ux)
  * [User Goals](#user-goals)
  * [User Stories](#user-stories)
* [**Creation process**](#creation-process)
  * [Planning](#planning)
  * [Flowcharts](#flowcharts)
  * [Google API SetUp](#google-api-setup)
  * [Google Sheets Data](#google-sheets-data)
  * [Python Logic](#python-logic)
  * [Design Choices](#design-choices)
* [**Features**](#features)
  * [How to Use](#how-to-use)
  * [Future Features](#future-features)
* [**Technologies Used**](#technologies-used)
* [**Python Libraries**](#python-libraries)
* [**Testing**](#testing)
  * [Bugs](#bugs)
  * [Validator](#validator)
* [**Deployment**](#deployment)
* [**Credits**](#credits)  

  
# User Experience (UX)  
  
## User Goals
BakeStock has been designed like a 'digital notebook', a clear, interactive, safe way for a hobby baker to keep track of important data. Some key user goals that I have kept in mind during this project have been:  

  - It must be easy to navigate, with clear Menu options.
  - An attractive, bright UI to engage the user.
  - Clear instructions are made available for correct data input.
  - Data must be completely editable for different baked items to be recorded.
  - The option to clear data if needed.
  - No dead ends to trap the user at the end of a function.

## User Stories  
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
  

# Creation Process  

  
## Flowcharts  
## Google API SetUp
## Python Logic
## Design Choices   
   - [ASCII banner maker](https://manytools.org/hacker-tools/ascii-banner/) : The BakeStock banner was created using the 'Colossal' font.  
     
![bakestock banner image](assets/readme_images/bakestock_ascii.png)
  
# Features

## How to Use
## Future Features
  
# Technologies Used  
  
# Python Libraries  
  
# Testing  
  
## Bugs
- Colorama not working [Install pip colorama](https://tinyurl.com/msk3uknk)
- Colorama preventing app working in Heroku [requirements.txt](https://tinyurl.com/3bxmr4kj)
## Validator  
  
# Deployment  

### Forking the GitHub Repositiory

A copy of the original repository can be made through GitHub. Please follow the below steps to fork this repository:  

1. Navigate to GitHub and log in.  
2. Once logged in, navigate to this repository using this link [BakeStock Repository](https://github.com/amylour/BakeStock).
3. Above the repository file section and to the top, right of the page is the 'Fork' button, click on this to make a fork of this repository.
4. You should now have access to a forked copy of this repository in your Github account.

### Clone this GitHub Repository

A local clone of this repository can be made on GitHub. Please follow the below steps:

1. Navigate to GitHub and log in.
2. The [BakeStock Repositiory](https://github.com/amylour/BakeStock) can be found at this location.
3. Above the repository file section, locate the 'Code' button.
4. Click on this button and choose your clone method from HTTPS, SSH or GitHub CLI, copy the URL to your clipboard by clicking the 'Copy' button.
5. Open your Git Bash Terminal.
6. Change the current working directory to the location you want the cloned directory to be made.
7. Type `git clone` and paste in the copied URL from step 4.
8. Press 'Enter' for the local clone to be created.

[GitHub Repository Clone Steps]()


###


  
# Credits

## Content References
   - gspread Documentation is used as reference material and guidance throughout the project for the manipulation of data between Python and Google Sheets: [gspread Docs](https://docs.gspread.org/en/latest/index.html)
   - Code Institute's 'Love Sandwiches' project for Google Sheets API and Creds Set-Up: [Code Institute](https://codeinstitute.net/ie/)
   - 101 Computing for the type-text effect, 'screen sleep', and 'clear screen' effects used throughout the project: [Python typing text effect](https://www.101computing.net/python-typing-text-effect/)
   - StackOverflow for providing a solution to display my Sales Data: [Adding tab for data formatting and display](https://stackoverflow.com/questions/4488570/how-do-i-write-a-tab-in-python)
   - Python enumerate tutorial by Tech with Tim for searching through Google Sheet data: [Tech with Tim Youtube](https://www.youtube.com/watch?v=-MZiQaNI0QA)
   - Python enumerate tutorial via Real Python for looping through data items: [Real Python](https://realpython.com/python-enumerate/)
   - Python zip() Function for Parallel Iteration for display of Batch and Inventory items: [Real Python](https://realpython.com/python-zip-function/)
   - Linuxhint for their Colorama tutorial and materials: [Linuxhint Colorama & Python](https://linuxhint.com/colorama-python/)

## Literature
I used the below book as extra learning material and reference material during the project:  

- [Python Crash Course](https://www.oreilly.com/library/view/python-crash-course/9781492071266/), Author: Eric Matthes, Publisher: No Starch Press, Year: 2019 Edition.

## Media
ASCII art was used twice in the project and were generated by:
- [ManyTools.org](https://manytools.org/hacker-tools/ascii-banner/), for the opening banner.
- [ASCII Art](https://www.asciiart.eu/), for the hidden easter egg.

## Acknowledgements  
- Many thanks to my family for their continued support when I need to talk through ideas and bugs, and for testing my work.
- Thank you to my mentor Rahul Lakhanpal for his support and guidance.
- Thanks and appreciation to my fellow Code Institute students who have offered great support.


[Back to Top](#bakestock)