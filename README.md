# Baseball Stats Retrieval Tool

### Purpose:
Using Python and one of its libraries, **sqlite3**, to create an SQL database with data from a 
csv file. In this project, the data is gathered from Baseball Savant and only the first 50 
players were saved to the csv file. *preprocessing.py* file is a Python script that takes
the data from the csv to an SQL database called *baseball.db* and into its table *stats*.
*gui.py* runs the GUI, from the **tkinter** Python library so the user can type SQL queries and
see the results printed under. 

### To compile and run program:
1. Whether you are on command line or in an IDE, <ins>ONLY</ins> run *gui.py*. 
    - on command line, run: python gui.py

##### Using the GUI
1. Enter a valid SQL query into the "Enter your SQL Query" textbox
    - **NOTE**: SQL Keywords like DROP, DELETE, ALTER, UPDATE, SET, ADD, INSERT, RENAME, and
    CREATE are not valid for a SQL query as they will alter the data in the database
2. Click *Submit* button to enter your SQL query and the results should appear in the "Your 
Results" section
3. Continue steps 2-3 if you want to enter more SQL queries
4. Once you are done, you can quit the GUI by either pressing the "Quit Program" button or 
pressing the X icon of the window
