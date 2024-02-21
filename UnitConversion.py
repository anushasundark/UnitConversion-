import tkinter as tk

def cm_to_feet(cm):
    return cm * 0.0328084
def feet_to_inches(feet):
    return feet * 12
def sqft_to_sqm(sqft):
    return sqft * 0.092903
def sqft_to_hectares(sqft):
    return sqft * 2.2957e-5

def sqft_to_acres(sqft):
    return sqft * 2.2957e-5
def convert_units():
    try:
        value = float(entry.get())
        conversion_option = conversion_var.get()
        if conversion_option == "cm_to_feet":
            result = cm_to_feet(value)
        elif conversion_option == "feet_to_inches":
            result = feet_to_inches(value)
        elif conversion_option == "sqft_to_sqm":
            result = sqft_to_sqm(value)
        elif conversion_option == "sqft_to_hectares":
            result = sqft_to_hectares(value)
        elif conversion_option == "sqft_to_acres":
            result = sqft_to_acres(value)
        else:
            result = "Invalid conversion option"
        
        result_label.config(text=f"Result: {result}")
    except ValueError:
        result_label.config(text="Please enter a valid numeric value.")


root = tk.Tk()
root.title("Unit Conversion")


conversion_var = tk.StringVar()
conversion_var.set("cm_to_feet")

conversion_options = ["cm_to_feet", "feet_to_inches", "sqft_to_sqm", "sqft_to_hectares", "sqft_to_acres"]

conversion_menu_label = tk.Label(root, text="Select Conversion Type:")
conversion_menu_label.pack()

conversion_menu = tk.OptionMenu(root, conversion_var, *conversion_options)
conversion_menu.pack(pady=10)

entry_label = tk.Label(root, text="Enter Value:")
entry_label.pack()

entry = tk.Entry(root, width=10)
entry.pack(pady=10)

convert_button = tk.Button(root, text="Convert", command=convert_units)
convert_button.pack(pady=10)

result_label = tk.Label(root, text="Result: ")
result_label.pack(pady=10)

root.mainloop()
