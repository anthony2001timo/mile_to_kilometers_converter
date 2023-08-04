from tkinter import *

def miles_to_km():
    miles = float(miles_entry.get())
    km = round(miles * 1.609)
    km_result.config(text=f"{km}")

#Window
window = Tk()
window.title("Mile to Kilometers converter")
window.config(padx=20,pady=20)

#Entry
miles_entry = Entry(width=7)
miles_entry.grid(column=1,row=0)

#Label
miles_label = Label(text="Miles")
miles_label.grid(column=2,row=0)

equal_to = Label(text="is equal to")
equal_to.grid(column=0,row=1)

km_result = Label(text="0")
km_result.grid(column=1,row=1)


km_label = Label(text="Km")
km_label.grid(column=2,row=1)


#Button
button = Button(text="Calculate",command=miles_to_km)
button.grid(column=1,row=2)


window.mainloop()
