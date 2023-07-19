# def sum(*args):
#     sum = 0
#     print(type(args))

#     for i in args:
#         sum = sum + i
#     return sum
# def dict(**kwargs):
#     print(kwargs)
#     print(type(kwargs))
#     for key,value in kwargs.items():
#         print(key,value)
# print(sum(10,20,30,40,50 ))
# dict(add=30,muliple=50)
from tkinter import *

window = Tk()
window.title("Widget Exampple")
window.minsize(width=500, height=500)
mylabel = Label(text="This is my first label")
mylabel.pack()
#creating an event listener
def button_clicked():
    print("i got clicked")
button = Button(text='Click Me',command=button_clicked)
button.pack()
#creating an input label
entry = Entry(width=30)
entry.insert(END,string="Some text to begin with")
print(entry.get())
entry.pack()
#creating a text
text = Text(height=5,width=30)
#cursor will be in text box
text.focus()
text.insert(END,"Example of multiline text box")
text.pack()
#spinbox--->counter
def spinbox_used():
     print(spinbox.get())
spinbox = Spinbox(from_=0,to=10,width=5,command=spinbox_used)
spinbox.pack()
#creating a scale
#value arguement is necesaary in scale
def scale_used(value):
    print(value)
scale = Scale(from_=0,to=20,command=scale_used)
scale.pack()

#creating a check button
#funcvtion for check
def checkbutton_used():
    print(check_stat.get())
    
check_stat = IntVar()
checkbutton = Checkbutton(text="Check me",variable=check_stat,command=checkbutton_used)
check_stat.get()
checkbutton.pack()

#creating a radio button
def radiobutton_used():
    print(radio_state.get())
    
radio_state = IntVar()
#creating ist radio button
radiobutton1 = Radiobutton(text='Option 1',command=radiobutton_used,value=1,variable=radio_state)
#creating 2nd radio button
radiobutton2 = Radiobutton(text='Option 2',command=radiobutton_used,value=2,variable=radio_state)
radiobutton1.pack()
radiobutton2.pack()
#creating a list box
def listbox_used(event):
    print(listbox.get(listbox.curselection()))

listbox = Listbox(height=4)
fruit = ['Apple','Mango','Orange','Bananas']
for i in fruit:
    listbox.insert(fruit.index(i),i)
listbox.bind("<<ListboxSelect>>",listbox_used)
listbox.pack()
window.mainloop()
