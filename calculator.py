import tkinter as tk
import math

# Create the main window
root = tk.Tk()
root.title("iPhone-Style Calculator")
root.geometry("400x600")
root.configure(bg="black")

expression = ""

# Display screen
display = tk.Entry(root, font=("Helvetica", 30), bd=10, relief=tk.FLAT, bg="black", fg="white", justify='right')
display.pack(expand=True, fill="both")

# Function to update expression
def press(key):
    global expression
    expression += str(key)
    display.delete(0, tk.END)
    display.insert(tk.END, expression)

# Function to evaluate expression
def equal():
    global expression
    try:
        result = str(eval(expression))
        display.delete(0, tk.END)
        display.insert(tk.END, result)
        expression = result  # Let user continue from result
    except:
        display.delete(0, tk.END)
        display.insert(tk.END, "Error")
        expression = ""

# Function to clear
def clear():
    global expression
    expression = ""
    display.delete(0, tk.END)

# Function to delete one character
def delete():
    global expression
    expression = expression[:-1]
    display.delete(0, tk.END)
    display.insert(tk.END, expression)

# Function for scientific operations
def sci_func(func):
    global expression
    try:
        value = eval(expression)
        if func == 'sqrt':
            value = math.sqrt(value)
        elif func == 'log':
            value = math.log10(value)
        elif func == 'ln':
            value = math.log(value)
        elif func == 'sin':
            value = math.sin(math.radians(value))
        elif func == 'cos':
            value = math.cos(math.radians(value))
        elif func == 'tan':
            value = math.tan(math.radians(value))
        elif func == '1/x':
            value = 1 / value
        display.delete(0, tk.END)
        display.insert(tk.END, str(value))
        expression = str(value)
    except:
        display.delete(0, tk.END)
        display.insert(tk.END, "Error")
        expression = ""

# Button layout
buttons = [
    ['C', 'DEL', '%', '/'],
    ['7', '8', '9', '*'],
    ['4', '5', '6', '-'],
    ['1', '2', '3', '+'],
    ['0', '.', '=', '√'],
    ['sin', 'cos', 'tan', 'log']
]

for row in buttons:
    frame = tk.Frame(root, bg="black")
    frame.pack(expand=True, fill="both")
    for btn in row:
        def make_cmd(x=btn):
            if x == "=":
                return equal
            elif x == "C":
                return clear
            elif x == "DEL":
                return delete
            elif x in ['√', 'log', 'sin', 'cos', 'tan']:
                return lambda: sci_func('sqrt' if x == '√' else x)
            else:
                return lambda: press(x)
        tk.Button(frame, text=btn, font=("Helvetica", 20), bg="#333", fg="white", bd=0, command=make_cmd()).pack(side="left", expand=True, fill="both")

root.mainloop()
