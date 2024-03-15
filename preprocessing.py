# libraries needed to load data into SQL database file
import sqlite3
import csv

### Function that starts a new SQL database file and table, and takes data from
### csv file and puts it into the new SQL database
def data():
    # creating a sql database and a connection to it
    connection = sqlite3.connect("baseball.db")
    cursor = connection.cursor()

    # creating a SQL table for the baseball data
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS stats (
            name TEXT,
            id INTEGER,
            year INTEGER,
            atBats INTEGER,
            hits INTEGER,
            homeRuns INTEGER,
            strikeouts INTEGER,
            battingAvg REAL,
            obp REAL
        )               
    """)
    
    # adding the data to the newly created stats table from the csv file
    filename = "stats.csv"
    file = open(filename, 'r')

    # array to hold the tuples of each row
    data = []

    # read the names of the columns of the data
    headers = file.readline()
    
    # getting data from csv file
    for each in file:
        row = each[0:-1].split(",")
        data.append(row)

    # closing the file
    file.close()

    # inserting all the data from array into sql table
    cursor.executemany("INSERT INTO stats VALUES(?,?,?,?,?,?,?,?,?)", data)
    connection.commit()
    
    # printing out data 
    all_data = cursor.execute("SELECT * FROM stats")

    # gets the headers from sql table
    headers = all_data.description
    column_names = []
    for col in headers:
        # gets the column name
        column_names.append(col[0])
    print()

    # get all row data
    rows = all_data.fetchall()

    # view columns and data, ensure it looks correct
    print(column_names)
    print(rows)
