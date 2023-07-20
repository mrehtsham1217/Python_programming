from tkinter import Label,Button,Entry,Tk
def miles_to_km():
    miles = float(entry.get()) 
    km = miles*1.609
    result_km_lable.config(text=f"{km}")
    result_km_lable.config(fg='red')


window = Tk()
window.title("Miles to Kilometer converter")
window.config(padx=20,pady=20)
entry = Entry(width=10)
entry.grid(column=1,row=0)
miles_label = Label(text='Miles')
miles_label.grid(column=2,row=0)

is_equal_label  = Label(text="Is equal to ")
is_equal_label.grid(column=0,row=1)
result_km_lable = Label(text=0)
result_km_lable.grid(column=1,row=1)
km_lable = Label(text="Km")
km_lable.grid(column=2,row=1)

caluculate_button = Button(text='calculate',command=miles_to_km)
caluculate_button.grid(column=1,row=2)
# window.minsize(height=200,width=300)
window.mainloop()
