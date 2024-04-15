import  tkinter as tk
from  tkinter import  ttk
def mtokm():
    x = inputvar.get()
    y = x / 1000
    output.set(y)


window=tk.Tk()
window.title("palak batra")
window.geometry("300x300")
inputvar=tk.IntVar()
output=tk.StringVar()
heading=ttk.Label(master=window,text="m to Km convertor",font="calibri 30 bold")
frame=ttk.Frame(master=window)
inputt=ttk.Entry(master=frame,textvariable=inputvar)
button=ttk.Button(master=frame,text="convertor",command=mtokm)
outputt=ttk.Label(master=window,text="Calculated value",textvariable=output)


heading.pack()
inputt.pack(side="left",padx=10)
button.pack(side="left",padx=10)
frame.pack(pady=20)
outputt.pack()
window.mainloop()