import tkinter
#Showing of window
window = tkinter.Tk()
window.title("My first GUI Program")
window.minsize(width=500,height=300)
#creating the label
mylabel = tkinter.Label(text="I am a label",font=("Arial",24,"bold"))
mylabel.pack(side="left")#this code show the lebel on screen
#it will keep the window show untill some disturbance
# mylabel.pack(side="bottom")
mylabel.pack(expand=True)#it will take entire height and width

window.mainloop()
