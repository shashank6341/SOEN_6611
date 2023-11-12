import tkinter as tk
from statistics import Statistics

# Create a window
window = tk.Tk()
window.title("Statistics Calculator")

# Create a frame to hold the widgets
frame = tk.Frame(window)
frame.pack()

# Create a label to display the instructions
label = tk.Label(frame, text="Enter the data separated by commas:")
label.grid(row=0, column=0, columnspan=2)

# Create an entry to get the data from the user
entry = tk.Entry(frame)
entry.grid(row=1, column=0, columnspan=2)

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
    # Get the data from the entry
    data = entry.get()
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

# Create a button to trigger the calculation
button = tk.Button(frame, text="Calculate", command=calculate)
button.grid(row=10, column=0, columnspan=2)

# Start the main loop
window.mainloop()
