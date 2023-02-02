from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
  letters = [chr(i) for i in range(65,91)] + [chr(i) for i in range(97,123)]
  symbols = ['!','@','#','$','%','^','&','*','(',')']
  numbers = [chr(i) for i in range(10)]

  password_letters = [choice(letters) for _ in range(randint(8,10))]
  password_symbols = [choice(symbols) for _ in range(randint(8,10))]
  password_numbers = [choice(numbers) for _ in range(randint(8,10))]
  password_list = password_letters + password_symbols + password_numbers

  shuffle(password_list)
    
  password = "".join(password_list)
  password_entry.insert(0, password)
  pyperclip.copy(password)
  


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
  website = website_entry.get()
  email = email_entry.get()
  password = password_entry.get()
  new_data = {
    website:{
      "eamil":email,
      "password":password
    }
  }
  
  if len(website) == 0 or len(password) == 0:
    messagebox.showinfo(title="Oops", message="Please make sure you  haven`t left ant fields empty.")
  else:
    try:
      with open("data.json", "r") as data_file:
        data = json.load(data_file)
        data.update(new_data)

    except FileNotFoundError:
      with open("data.json","w") as data_file:
        json.dump(new_data, data_file, indent=4)
    
    else:
      data.update(new_data)
    
      with open("data.json", "w") as fata_file:
        json.dump(data, data_file, indent=4)
    
    finally:
      website_entry.delete(0, END)
      password_entry.delete(0, END)
      
# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
  website = website_entry.get()
  
  try:
    with open("data.json") as data_file:
      data = json.load(data_file)
  except FileNotFoundError:
    messagebox.showinfo(title="Error", message="No data File found")
  else:
    if website in data:
      email = data[website]['email']
      password = data[website]['password']
      messagebox.showinfo(title=website, message=f"Ema il: {email}\nPassword: {password}")
    else:
      messagebox.showinfo(title="Error", message=f"No details for {website} exists.")
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(heigh=200, width=200)
logo_img = PhotoImage(file=r"C:\Users\JDoubleU\Desktop\프로그래밍\dummy\password-manager-start\logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

#Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)

password_label = Label(text="password:")
password_label.grid(row=3, column=0)

# Entries
website_entry = Entry(width=21)
website_entry.grid(row=1, column=1)

email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, string="angel@gmail.com")

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

#  Button
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)


search_button = Button(text="Search", width=13, command=find_password)
search_button.grid(row=1, column=2)

window.mainloop()