import subprocess
import tkinter as tk
from tkinter import messagebox
import mysql.connector
import metricstics

# Function to check if username already exists
def username_exists(username):
    db_connection = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="neharoot",
        database="user_credentials"
    )
    cursor = db_connection.cursor()

    cursor.execute("SELECT * FROM users WHERE username=%s", (username,))
    existing_user = cursor.fetchone()

    db_connection.close()

    return existing_user is not None

# Function to handle the signup button
def signup():
    username = signup_username.get()
    password = signup_password.get()

    if not username or not password:
        messagebox.showwarning("Signup Failed", "Please fill in all fields.")
        return

    if username_exists(username):
        messagebox.showwarning("Signup Failed", "Username or password already exists so please choose a different username/password.")
        return

    # Replace these credentials with your MySQL database details
    db_connection = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="neharoot",
        database="user_credentials"
    )
    cursor = db_connection.cursor()

    cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))

    db_connection.commit()
    db_connection.close()

    messagebox.showinfo("Signup Successful", "Account created successfully.")

    # Clear the signup entry fields
    signup_username.delete(0, tk.END)
    signup_password.delete(0, tk.END)

# Function to handle the login button
def login():
    username = login_username.get()
    password = login_password.get()

    if not username or not password:
        messagebox.showwarning("Login Failed", "Please fill in all fields.")
        return

    # Replace these credentials with your MySQL database details
    db_connection = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="neharoot",
        database="user_credentials"
    )
    cursor = db_connection.cursor()

    cursor.execute("SELECT * FROM users WHERE username=%s AND password=%s", (username, password))
    user = cursor.fetchone()

    db_connection.close()

    if user:
        # messagebox.showinfo("Login Successful", "Welcome, " + username + "!")
        root.destroy()
        metricstics.run_main_ui()
    else:
        messagebox.showerror("Login Failed", "Invalid username or password.")

        # Clear the login entry fields
        login_username.delete(0, tk.END)
        login_password.delete(0, tk.END)

def open_new_window():
    # Replace 'your_another_script.py' with the filename of the Python script you want to run
    subprocess.run(["python", "metricstics.py"])


# Main program
# Create the main window
root = tk.Tk()
root.title("Login and Signup")

# Create and pack frames
login_frame = tk.Frame(root)
signup_frame = tk.Frame(root)

login_frame.pack(padx=10, pady=10)
signup_frame.pack(padx=10, pady=10)

# Login Page
login_label = tk.Label(login_frame, text="Login Page", font=("Helvetica", 16))
login_label.grid(row=0, column=0, columnspan=2, pady=10)

login_username_label = tk.Label(login_frame, text="Username:")
login_username_label.grid(row=1, column=0, sticky=tk.E)

login_password_label = tk.Label(login_frame, text="Password:")
login_password_label.grid(row=2, column=0, sticky=tk.E)

login_username = tk.Entry(login_frame)
login_username.grid(row=1, column=1)

login_password = tk.Entry(login_frame, show="*")
login_password.grid(row=2, column=1)

login_button = tk.Button(login_frame, text="Login", command=login)
login_button.grid(row=3, column=0, columnspan=2, pady=10)

# Signup Page
signup_label = tk.Label(signup_frame, text="Signup Page", font=("Helvetica", 16))
signup_label.grid(row=0, column=0, columnspan=2, pady=10)

signup_username_label = tk.Label(signup_frame, text="Username:")
signup_username_label.grid(row=1, column=0, sticky=tk.E)

signup_password_label = tk.Label(signup_frame, text="Password:")
signup_password_label.grid(row=2, column=0, sticky=tk.E)

signup_username = tk.Entry(signup_frame)
signup_username.grid(row=1, column=1)

signup_password = tk.Entry(signup_frame, show="*")
signup_password.grid(row=2, column=1)

signup_button = tk.Button(signup_frame, text="Signup", command=signup)
signup_button.grid(row=3, column=0, columnspan=2, pady=10)

root.mainloop()
