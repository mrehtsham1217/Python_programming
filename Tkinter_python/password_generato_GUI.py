from random import randint, choice, shuffle
from tkinter import Tk, Label, Button, mainloop, Canvas, PhotoImage, Entry, END, messagebox
# ------------------- PASSWORD GENERATOR--------------------- #


def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
               'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', "-", "+"]

    password_letter = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letter + password_symbols + password_numbers
    shuffle(password_list)
    password = "".join(password_list)
    # print(f"Your password is {password}")
    password_entry.insert(0, password)

# --------------------SAVE PASSWORD ---------------------- #


def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(
            title="OOPS--!", message="Please Make sure all the input should fill")
    else:
        is_okay = messagebox.askokcancel(
            title=website, message=f"These details are enetered: \n Email {email}\n password {password}\n Is is okay to save in file ")
        if is_okay:
            with open("save_password.txt", "a") as data:
                data.write(f"{website}\t {email}\t{password} \n")
                # this will remove the data after submiting into file
                website_entry.delete(0, END)
                # email_entry.delete(0, END)
                password_entry.delete(0, END)


# --------------------- UI SETUP -------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
canvas = Canvas(height=200, width=200)
# create photo image
logo_img = PhotoImage(file="images/logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)
# create website label
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

# creating webiste entry
website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2)
# creating username/email label
email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

# creating username/email Entry
email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "ehtsham@gmail.com")  # 0-->starts at 0 index-->END

# creating password label
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)
# creating passsword entry
password_entry = Entry(width=23, show="*")
password_entry.grid(column=1, row=3)

# creating password geneator button
gen_password_button = Button(text="Gen Password", command=password_generator)
gen_password_button.grid(column=2, row=3)

# creating add button
add_password_button = Button(text="Add Password", width=34, command=save)
add_password_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
