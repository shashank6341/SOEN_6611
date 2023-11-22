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
    try:
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
    except ValueError:
        # Display an error message if the data is not valid
        tk.messagebox.showerror("Error", "Invalid data. Please enter comma-separated numbers.")
    except AttributeError:
        # Display an error message if the method is not found
        tk.messagebox.showerror("Error", "Invalid method. Please select a valid option.")
    except Exception as e:
        # Display a generic error message for any other exception
        tk.messagebox.showerror("Error", "An error occurred.")

# Define a function to restore the data from the history file
def restore():
    try:
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
    except FileNotFoundError:
        tk.messagebox.showerror("Error", "No previous history found.")
    except Exception as e:
        tk.messagebox.showerror("Error", "An error occurred while restoring the last session")

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
    select()

def checkOptions(advanced=False):
    # Loop through the basic options
    for i in range(len(options)-3):
        # Check the option
        vars[i].set(1)
    # Loop through the basic options
    for i in range(5,len(options)):
        # Check the option
        if advanced: vars[i].set(1)
        else: vars[i].set(0)

# Define a function to save the data and the results to the history file
def save():
    try:
        # Get the data from the text widget
        data = text.get("1.0", "end-1c")
        # Open the history file
        with open("history.csv", "a") as file:
            # Create a csv writer
            writer = csv.writer(file)
            # Write the data and the results as a row
            writer.writerow([data])
    except Exception as e:
        tk.messagebox.showerror("Error", "An error occurred storing the session.")

# Define a function to load the data from a CSV file
def load():
    try:
        # Ask the user to select a file
        filename = fd.askopenfilename(filetypes=[("CSV files", "*.csv")])
        # Check if a file is selected
        if filename:
            # Open the file
            with open(filename, "r") as file:
                # Read the entire file content and replace non-breaking spaces with standard spaces
                file_content = file.read().replace(u'\u00A0', ' ')
                # Use StringIO to mimic a file object for csv.reader
                from io import StringIO
                file_like_object = StringIO(file_content)

                # Read the csv reader
                reader = csv.reader(file_like_object)
                # Get the first row
                data = next(reader)
                # Join the data items from the first row separated by commas
                data_str = ','.join(data)
                # Insert the data into the text widget
                text.delete("1.0", "end")
                text.insert("1.0", data_str)
    except FileNotFoundError:
        tk.messagebox.showerror("Error", "File not found.")
    except csv.Error:
        tk.messagebox.showerror("Error", "Error reading the input file.")
    except Exception as e:
        tk.messagebox.showerror("Error", "An error occurred while uploading data.")

# Define a function to handle the radio button selection
def select():
    # Get the radio button value
    value = radio_var.get()
    # Check if the value is 1 (basic)
    if value == 1:
        # Call the checkOptions function with False
        checkOptions(False)
    # Check if the value is 2 (advanced)
    elif value == 2:
        # Call the checkOptions function with True
        checkOptions(True)

# Create a variable to store the radio button value
radio_var = tk.IntVar()

# Create two radio buttons "basic" and "advanced"
radio_label = tk.Label(frame, text="Profile:")
radio_label.grid(row=10, column=0, sticky="w")
radio_basic = tk.Radiobutton(frame, text="Basic", variable=radio_var, value=1, command=select)
radio_basic.grid(row=10, column=1, sticky="w")
radio_advanced = tk.Radiobutton(frame, text="Advanced", variable=radio_var, value=2, command=select)
radio_advanced.grid(row=10, column=2, sticky="w")

# Set the default radio button value to 1 (basic)
radio_var.set(1)
select()


# Create a button to trigger the calculation
button_calculate = tk.Button(frame, text="Calculate", command=calculate)
button_calculate.grid(row=11, column=0, columnspan=1)

# Create a button to trigger the restoration
button_restore = tk.Button(frame, text="Restore", command=restore)
button_restore.grid(row=12, column=0, columnspan=1)

# Create a button to trigger the clearing
button_clear = tk.Button(frame, text="Clear", command=clear, fg="red")
button_clear.grid(row=11, column=2, columnspan=1)

# Create a button to trigger the saving
button_save = tk.Button(frame, text="Save", command=save)
button_save.grid(row=11, column=1, columnspan=1)

# Create a button to trigger the loading
button_load = tk.Button(frame, text="Load CSV From File", command=load)
button_load.grid(row=12, column=1, columnspan=2)

# Start the main loop#
window.mainloop()