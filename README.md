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

#### Using the GUI
1. Enter a valid SQL query into the "Enter your SQL Query" textbox
    - **NOTE**: SQL Keywords like DROP, DELETE, ALTER, UPDATE, SET, ADD, INSERT, RENAME, and
    CREATE are not valid for a SQL query as they will alter the data in the database
2. Click *Submit* button to enter your SQL query and the results should appear in the "Your 
Results" section
3. Continue steps 2-3 if you want to enter more SQL queries
4. Once you are done, you can quit the GUI by either pressing the "Quit Program" button or 
pressing the X icon of the window

### Notes on the SQL Headers and Data
- *name* is a TEXT data type, with the baseball player's first name and last name
    - ex.) "Pete Alonso"
- *id* is an INTEGER data type, contributing to the baseball player's id number
    - Min: 502671, Max: 683011
- *year* is an INTEGER data type, the year of the stats (all of them are in 2023)
- *atBats* is an INTEGER data type, the number of at bats the player had in 2023 (>0)
- *hits* is an INTEGER data type, the number of hits the player had in 2023 (>0)
- *homeRuns* is an INTEGER data type, the number of home runs the player had in 2023 (>0)
- *strikeouts* is an INTEGER data type, the number of strikeouts the player had in 2023 (>0)
- *battingAvg* is a REAL data type, the formula for batting average is (hits / atBats)
    - 0 <= battingAvg <= 1
- *obp* is a REAL data type, the formula for on-base percentage is ((hits + walks or base on balls + hit by pitches) / (at bats + walks or base on balls + hit by pitches + sacrifice flies))
    - 0 <= obp <= 1
