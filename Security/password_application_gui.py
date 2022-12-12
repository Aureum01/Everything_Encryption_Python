import tkinter as tk
from tkinter import messagebox

# Define the password
PASSWORD = "secret"

# Create the main window
root = tk.Tk()

# Define a function to check the password
def check_password():
    # Get the password from the input field
    entered_password = password_entry.get()

    # Check if the entered password is correct
    if entered_password == PASSWORD:
        # If the password is correct, show a success message
        messagebox.showinfo("Success", "The password is correct!")
    else:
        # If the password is incorrect, show an error message
        messagebox.showerror("Error", "The password is incorrect!")

# Create a label for the password prompt
password_label = tk.Label(root, text="Enter the password:")
password_label.pack()

# Create an input field for the password
password_entry = tk.Entry(root, show="*")
password_entry.pack()

# Create a button to submit the password
password_button = tk.Button(root, text="Submit", command=check_password)
password_button.pack()

# Start the main event loop
root.mainloop()

