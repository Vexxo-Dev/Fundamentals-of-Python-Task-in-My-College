from tkinter import Tk, Label, Button, Entry

root = Tk()
root.title("Simple GUI")
root.geometry("400x300")

# Function to show success message

def show_success():
    success_label = Label(root, text="Submission Successful!", fg="green", font=("Arial", 12))
    success_label.pack(pady=10)
 

# Save Username and Password
def save_credentials():
    if not entry_name.get() or not entry_password.get():
        error_window = Tk()
        error_window.title("Error")
        error_window.geometry("300x150")
        error_label = Label(error_window, text="Both fields are required!", fg="red", font=("Arial", 12))
        error_label.pack(pady=20)
        button_close = Button(error_window, text="Close", command=error_window.destroy)
        button_close.pack(pady=10)
        error_window.mainloop()
        return

    username = entry_name.get()
    password = entry_password.get()
    show_success()

# Sign in window after submission

def sign_in_window():
    sign_in_window = Tk()
    sign_in_window.title("Sign In")
    sign_in_window.geometry("300x200")
    
    label_sign_in = Label(sign_in_window, text="Sign In Successful!", font=("Arial", 12))
    label_sign_in.pack(pady=20)
    
    label_info = Label(sign_in_window, text="You can now close this window.", font=("Arial", 10))
    label_info.pack(pady=10)

    button_close = Button(sign_in_window, text="Close", command=sign_in_window.destroy)
    button_close.pack(pady=10)
    
    sign_in_window.mainloop()


# Enter Name and Password
label = Label(root, text="Welcome to the Simple GUI Application", font=("Arial", 14))
label.pack(pady=20)
label_name = Label(root, text="Username:")
label_name.pack(pady=5)
entry_name = Entry(root)
entry_name.pack(pady=5)
label_password = Label(root, text="Password:")
label_password.pack(pady=5)
entry_password = Entry(root, show='*')
entry_password.pack(pady=5)
ton_submit = Button(root, text="Submit", command=save_credentials) # add window sign in open
ton_submit.config(command=lambda: [save_credentials(), sign_in_window()])

ton_submit.pack(pady=20)


root.mainloop()