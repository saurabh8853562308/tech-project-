import tkinter as tk
from tkinter import ttk

def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9

def celsius_to_fahrenheit(c):
    return (c * 9 / 5) + 32

def convert_temperature():
    input_temp = float(entry_temperature.get())
    if conversion_choice.get() == "Fahrenheit to Celsius":
        output_temp = fahrenheit_to_celsius(input_temp)
        label_result.config(text=f"{input_temp} °F is {output_temp:.2f} °C")
    else:
        output_temp = celsius_to_fahrenheit(input_temp)
        label_result.config(text=f"{input_temp} °C is {output_temp:.2f} °F")

# Create the main window
root = tk.Tk()
root.title("Temperature Conversion")

# Create and place widgets
label_instruction = tk.Label(root, text="Enter the temperature:")
label_instruction.grid(column=0, row=0, padx=10, pady=10)

entry_temperature = tk.Entry(root)
entry_temperature.grid(column=1, row=0, padx=10, pady=10)

conversion_choice = ttk.Combobox(root, values=["Fahrenheit to Celsius", "Celsius to Fahrenheit"])
conversion_choice.grid(column=0, row=1, padx=10, pady=10)
conversion_choice.current(0)  # Set default selection

button_convert = tk.Button(root, text="Convert", command=convert_temperature)
button_convert.grid(column=1, row=1, padx=10, pady=10)

label_result = tk.Label(root, text="Result will be shown here")
label_result.grid(column=0, row=2, columnspan=2, padx=10, pady=10)

# Run the main event loop
root.mainloop()
