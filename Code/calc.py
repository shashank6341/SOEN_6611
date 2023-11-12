import tkinter as tk
from statistics import Statistics
import csv
import tkinter.filedialog as fd

# Create a window
window = tk.Tk()
window.title("Statistics Calculator")

# Create a frame to hold the widgets
frame = tk.Frame(window)
frame.pack()

# Create a label to display the instructions
label = tk.Label(frame, text="Enter the data separated by commas:")
label.grid(row=0, column=0, columnspan=4)

# Create a text widget to get the data from the user
text = tk.Text(frame, height=5, width=40)
text.grid(row=1, column=0, columnspan=4)

# Create a list of statistics options
options = ["Min", "Max", "Mode", "Median", "Mean", "MAD", "Stdev", "Variance"]

# Create a list of variables to store the checkbox values
vars = []
for i in range(len(options)):
    vars.append(tk.IntVar())

# Create a list of checkboxes to select the statistics
checkboxes = []
for i in range(len(options)):
    checkboxes.append(tk.Checkbutton(frame, text=options[i], variable=vars[i]))
    checkboxes[i].grid(row=2+i, column=0, sticky="w")

# Create a list of labels to display the results
labels = []
for i in range(len(options)):
    labels.append(tk.Label(frame, text=""))
    labels[i].grid(row=2+i, column=1, sticky="w")

# Define a function to calculate and display the statistics
def calculate():
    # Get the data from the text widget
    data = text.get("1.0", "end-1c")
    # Convert the data to a list of numbers
    data = [float(x) for x in data.split(",")]
    # Create a Statistics object
    stats = Statistics()
    # Read the data
    stats.read_data(data)
    # Loop through the options
    for i in range(len(options)):
        # Check if the option is selected
        if vars[i].get() == 1:
            # Get the corresponding method name
            method = options[i].lower()
            # Call the method and get the result
            result = getattr(stats, method)()
            # Display the result
            labels[i].config(text=str(result))
        else:
            # Clear the result
            labels[i].config(text="")

# Define a function to restore the data from the history file
def restore():
    # Open the history file
    with open("history.csv", "r") as file:
        # Read the csv reader
        reader = csv.reader(file)
        # Get the last row
        for row in reader:
            pass
        # Get the data from the last row
        data = row[0]
        # Insert the data into the text widget
        text.delete("1.0", "end")
        text.insert("1.0", data)

# Define a function to clear the data and the results
def clear():
    # Delete the data from the text widget
    text.delete("1.0", "end")
    # Loop through the options
    for i in range(len(options)):
        # Uncheck the option
        vars[i].set(0)
        # Clear the result
        labels[i].config(text="")

# Define a function to save the data and the results to the history file
def save():
    # Get the data from the text widget
    data = text.get("1.0", "end-1c")
    # Get the results from the labels
    results = []
    for i in range(len(options)):
        results.append(labels[i].cget("text"))
    # Open the history file
    with open("history.csv", "a") as file:
        # Create a csv writer
        writer = csv.writer(file)
        # Write the data and the results as a row
        writer.writerow([data] + results)

# Define a function to load the data from a CSV file
def load():
    # Ask the user to select a file
    filename = fd.askopenfilename(filetypes=[("CSV files", "*.csv")])
    # Check if a file is selected
    if filename:
        # Open the file
        with open(filename, "r") as file:
            # Read the csv reader
            reader = csv.reader(file)
            # Get the first row
            data = next(reader)
            # Get the data from the first row
            data = data[0]
            # Insert the data into the text widget
            text.delete("1.0", "end")
            text.insert("1.0", data)

# Create a button to trigger the calculation
button_calculate = tk.Button(frame, text="Calculate", command=calculate)
button_calculate.grid(row=10, column=0)

# Create a button to trigger the restoration
button_restore = tk.Button(frame, text="Restore", command=restore)
button_restore.grid(row=10, column=1)

# Create a button to trigger the clearing
button_clear = tk.Button(frame, text="Clear", command=clear)
button_clear.grid(row=10, column=2)

# Create a button to trigger the saving
button_save = tk.Button(frame, text="Save", command=save)
button_save.grid(row=11, column=0, columnspan=2)

# Create a button to trigger the loading
button_load = tk.Button(frame, text="Load CSV From File", command=load)
button_load.grid(row=11, column=2)

# Start the main loop
window.mainloop()