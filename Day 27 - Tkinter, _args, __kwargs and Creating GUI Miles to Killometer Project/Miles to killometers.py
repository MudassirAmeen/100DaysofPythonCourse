# Miles to Kilometer converter

import tkinter as tk

window = tk.Tk()
window.title("Miles to Kilometer")
window.minsize(width=300, height=150)



# Input Miles
miles = tk.Entry()
miles.insert(0, "1")
miles.grid(column=2, row=1)

# Miles Label 
m_label = tk.Label(text="Miles")
m_label.grid(column=3, row=1)

# Global Label
g_label = tk.Label(text="is equal to ")
g_label.grid(column=1, row=2)

# Kilo meter Label
killometers = tk.Label(text="")
killometers.grid(column=2, row=2)

# Kilo meter text Label
k_label = tk.Label(text="Kilometers")
k_label.grid(column=3, row=2)



# main Function
killoMeters = float(miles.get()) * 1.6
killometers.config(text=killoMeters)

# Function to calculate the miles to killometers
def calculate():
    global killoMeters
    killoMeters = float(miles.get()) * 1.6
    killometers.config(text=killoMeters)

# Calculate Button
button = tk.Button(text="Calculate", command=calculate)
button.grid(column=2, row=3)


window.mainloop()