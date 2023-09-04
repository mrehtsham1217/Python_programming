from tkinter import Tk, Entry, Label, Button
window = Tk()
window.title("Miles To Kilometer")
window.config(padx=20, pady=20)


def miles_to_km():
    miles = float(miles_input.get())
    km = round(miles * 1.609)
    equal_km.config(text=f"{km}")


miles_input = Entry(width=8)
miles_input.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

equal_label = Label(text="Is Equal To")
equal_label.grid(column=0, row=1)

equal_km = Label(text=0)
equal_km.grid(column=1, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

cal_button = Button(text="Calculate", command=miles_to_km)
cal_button.grid(column=1, row=2)

window.mainloop()
