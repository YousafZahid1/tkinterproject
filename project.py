import tkinter as tk
import random as r

#Sign up page

# Create the Sign-Up window
sign = tk.Tk()
sign.geometry("500x500")
sign.title("Sign UP")

# Title Label
label2 = tk.Label(sign, text="SIGN UP", font=('Bold', 30))
label2.pack(padx=50, pady=30)

# Function to get the values and save them in a text file
def get_values():
    name = text1.get()
    username = text2.get()
    password = text3.get()
    file = open("info.txt", "a")
    file.write(" Username: " + username + " Password: " + password + "\n")
    file.close()

# Function to generate a random password
def generatepassword():
    all_values = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
        'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
        'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
        '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
        '`', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-',
        '_', '=', '+', '[', ']', '{', '}', '|', ';', ':', '"',
        ',', '.', '/', '<', '>', '?', ''
    ]
    random_password = ""
    for i in range(12):
        random_password += r.choice(all_values)
    print("Random password")
    text3.insert(0, random_password)


# Labels and Entry fields for user input
name = tk.Label(sign, text="Enter your Name", font=('Bold', 15))
name.pack(padx=0, pady=10)
text1 = tk.Entry(sign)
text1.pack()

enter_username = tk.Label(sign, text="Enter your username", font=('Bold', 15))
enter_username.pack(padx=0, pady=10)
text2 = tk.Entry(sign)
text2.pack()

enter_password = tk.Label(sign, text="Enter your password", font=('Bold', 15))
enter_password.pack(padx=0, pady=10)
text3 = tk.Entry(sign)
text3.pack()

# Buttons for generating password and signing up
gbutton = tk.Button(sign, text="Generate Password", font=('Arial', 15), command=generatepassword)
gbutton.pack(padx=2, pady=10)

button = tk.Button(sign, text="Sign UP", font=("Bold", 14), command=get_values)
button.pack(pady=40)

# Run the Sign-Up window
sign.mainloop()


##### LOGIN PAGE #####

# Create the Login window
first = tk.Tk()
first.geometry("500x500")
first.title("Login")

# Title Label
label = tk.Label(first, text="LOGIN", font=('Bold', 30))
label.pack(padx=50, pady=40)

# Labels and Entry fields for username and password
username = tk.Label(first, text="USERNAME", font=('Bold', 19))
username.pack(padx=25, pady=40)
get_user = tk.Entry(first, text="USERNAME")
get_user.pack()

password = tk.Label(first, text="PASSWORD", font=('Bold', 19))
password.pack(padx=25, pady=40)
get_password = tk.Entry(first, text="PASSWORD")
get_password.pack()


# Function to handle login
def login():
    username = get_user.get()
    password = get_password.get()
    file = open("info.txt", "r")
    for i in file:
        if i != " Username: " + username + " Password: " + password + "\n":
            pass
        elif i == " Username: " + username + " Password: " + password + "\n":
            print("logged in Successfully")
            break
        else:
            print("NOT Logged In")


# Button for login
button = tk.Button(first, text="Log in", font=('Bold', 15), command=login)
button.pack(pady=20)

# Run the Login window
first.mainloop()
import tkinter as tk
import random as r

##### SIGN UP PAGE #####

# Create the Sign-Up window
sign = tk.Tk()
sign.geometry("500x500")
sign.title("Sign UP")

# Title Label
label2 = tk.Label(sign, text="SIGN UP", font=('Bold', 30))
label2.pack(padx=50, pady=30)


# Function to get the values and save them in a text file
def get_values():
    name = text1.get()
    username = text2.get()
    password = text3.get()
    file = open("info.txt", "a")
    file.write(" Username: " + username + " Password: " + password + "\n")
    file.close()


# Function to generate a random password
def generatepassword():
    all_values = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
        'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
        'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
        '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
        '`', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-',
        '_', '=', '+', '[', ']', '{', '}', '|', ';', ':', '"',
        ',', '.', '/', '<', '>', '?', ''
    ]
    random_password = ""
    for i in range(12):
        random_password += r.choice(all_values)
    print("Random password")
    text3.insert(0, random_password)


# Labels and Entry fields for user input
name = tk.Label(sign, text="Enter your Name", font=('Bold', 15))
name.pack(padx=0, pady=10)
text1 = tk.Entry(sign)
text1.pack()

enter_username = tk.Label(sign, text="Enter your username", font=('Bold', 15))
enter_username.pack(padx=0, pady=10)
text2 = tk.Entry(sign)
text2.pack()

enter_password = tk.Label(sign, text="Enter your password", font=('Bold', 15))
enter_password.pack(padx=0, pady=10)
text3 = tk.Entry(sign)
text3.pack()

# Buttons for generating password and signing up
gbutton = tk.Button(sign, text="Generate Password", font=('Arial', 15), command=generatepassword)
gbutton.pack(padx=2, pady=10)

button = tk.Button(sign, text="Sign UP", font=("Bold", 14), command=get_values)
button.pack(pady=40)

# Run the Sign-Up window
sign.mainloop()


##### LOGIN PAGE #####

# Create the Login window
first = tk.Tk()
first.geometry("500x500")
first.title("Login")

# Title Label
label = tk.Label(first, text="LOGIN", font=('Bold', 30))
label.pack(padx=50, pady=40)

# Labels and Entry fields for username and password
username = tk.Label(first, text="USERNAME", font=('Bold', 19))
username.pack(padx=25, pady=40)
get_user = tk.Entry(first, text="USERNAME")
get_user.pack()

password = tk.Label(first, text="PASSWORD", font=('Bold', 19))
password.pack(padx=25, pady=40)
get_password = tk.Entry(first, text="PASSWORD")
get_password.pack()


# Function to handle login
def login():
    username = get_user.get()
    password = get_password.get()
    file = open("info.txt", "r")
    for i in file:
        if i != " Username: " + username + " Password: " + password + "\n":
            pass
        elif i == " Username: " + username + " Password: " + password + "\n":
            print("logged in Successfully")
            break
        else:
            print("NOT Logged In")


# Button for login
button = tk.Button(first, text="Log in", font=('Bold', 15), command=login)
button.pack(pady=20)

# Run the Login window
first.mainloop()
