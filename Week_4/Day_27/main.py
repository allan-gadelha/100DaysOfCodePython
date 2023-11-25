from tkinter import *

window = Tk()
window.title("Miles to Kilometer Converter")
window.minsize(width=400, height=200)
#window.config(padx=10, pady=10)

#Entry
input = Entry(width=10)
input.grid(column=2, row=2)

#Label Miles
my_label1 = Label(text=" Miles", font=("Arial", 14, "bold"))
my_label1.grid(column=3, row=2)

#Label is equal to
my_label2 = Label(text="is equal to", font=("Arial", 14, "bold"))
my_label2.grid(column=0, row=3)

#Label Km
my_label3 = Label(text="Km", font=("Arial", 14, "bold"))
my_label3.grid(column=3, row=3)

#Label Result
my_label4 = Label(text="0", font=("Arial", 14, "bold"))
my_label4.grid(column=2, row=3)

def button_clicked():
    km = float(input.get()) * 1.609
    my_label4.config(text=km)

#Button Calculate
button = Button(text="Calculate", command=button_clicked)
button.grid(column=2, row=4)

window.mainloop()