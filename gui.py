# GUI Libraries
import tkinter as tk
from tkinter import *

# SQL Library
import sqlite3

# python program that did the SQL setup
from preprocessing import *

### Setting up the window for the GUI
frame = tk.Tk() # creating a starter window/frame for the GUI
frame.geometry("900x675") # setting the size
frame.title("Baseball Stats Retrieval Tool") # TITLE of the window
frame.maxsize(900, 675)  # max width x height
frame.minsize(900, 675)  # min width x height
frame.config(bg="#075aad")  # set background color of root window

# When you hover over a button, it will glow yellow
def on_enter(e):
    e.widget['background'] = 'yellow'

# when you don't hover over the button, it will return back to original button color
def on_leave(e):
    e.widget['background'] = '#edf1f7'

# prints the result of the SQL query onto one of the Labels in the GUI
def printResult(): 
    # clearing previous result
    lbl.delete("1.0", "end")
    
    # connecting to baseball.db and creating a cursor to it
    connection = sqlite3.connect("baseball.db")
    cursor = connection.cursor()

    # gets all of the query that the user inputted in the inputtxt section
    query = inputtxt.get(1.0, "end-1c")
    
    # the bad words that could change the database
    bad_words = ["DROP", "DELETE", "ALTER", "UPDATE", "SET", "ADD",
                 "INSERT", "RENAME", "CREATE"]
    
    # checks to see if the user typed in any bad SQL words from the list above
    if any(word in query for word in bad_words):
        lbl.config(text = "INVALID QUERY: Please enter a valid query")

    # if not, continue
    else:
        # sees if the user typed in a valid SQL query
        try:
            all_data = cursor.execute(query).fetchall() # gets all the data

            return_string = ""  # the starting blank string that will be printed
            
            for row in all_data:
                for datum in row:
                    return_string += str(datum) + "  " # adds result to the string
                return_string += "\n"
            
            # inserts the result from the return string to the lbl section of GUI
            lbl.insert(tk.END, return_string)
        
        # if SQL query is invalid, print out the error message and put it into 
        # lbl section of the GUI
        except:
            invalid_msg = "INVALID QUERY: Please check to see if you mistyped and enter a valid query"
            lbl.insert(tk.END, invalid_msg)

data()  # calls the data function from preprocessing.py to see if database is loaded

# creating a header for the GUI, with a background color of white and some padding
title = Label(frame, text = "Welcome to the Baseball Stats Retrieval Tool!", bg="#075aad", fg="white")
title.pack(ipady=5, pady=5)
title.config(font=("Font", 30))  # change font and size of label

# A subtitle to let the user know where to enter the SQL query
subtitle = Label(frame, text = "Enter your SQL Query:", bg="#075aad", fg="white", anchor='w')
subtitle.pack(fill="both", ipady=5, pady=2, padx=45) # add some more padding
subtitle.config(font=("Font", 14))  # change font and size of label

# creating a user input frame 
input_frame = Frame(frame, bg="#075aad")
input_frame.pack()

# creating a text input box for user to type in SQL query inside the input frame
inputtxt = tk.Text(input_frame, 
                height = 5, 
                width = 100) 
inputtxt.pack() 

### Button Creations inside the input frame
# submit button for the user to submit their query
submit = tk.Button(input_frame, 
                    text = "Submit",
                    command = printResult) 
submit.pack(padx=(50,5), pady=10, side="left", ipadx=5, ipady=5) 

submit.bind("<Enter>", on_enter)    # calling the function to whenever the button is hovered
submit.bind("<Leave>", on_leave)    # calling the function to whenever the button is not hovered

# quit program button so the user can leave the GUI window
quit = tk.Button(input_frame,
                    text="Quit Program", command=frame.destroy)
quit.pack(padx=5, side="left", ipadx=5, ipady=5)

quit.bind("<Enter>", on_enter)  # calling the function to whenever the button is hovered
quit.bind("<Leave>", on_leave)  # calling the function to whenever the button is not hovered


# title for the sql frame
sqlTitle = Label(frame, text = "Your results:", bg="#075aad", fg="white", anchor='w')
sqlTitle.pack(fill="both", ipady=5, pady=(20, 2), padx=45)
sqlTitle.config(font=("Font", 14))  # change font and size of label

# output SQL info frame
sql_frame = Frame(frame, bg="#ffffff")
sql_frame.pack()

# put resutls into sql frame
lbl = Text(sql_frame, height = 20, width=100, bg="#ffffff") 
lbl.pack() 

# to keep the window open, through a constant loop
frame.mainloop()
