import tkinter as tk

# Function to update the display
def update_display(value):
    display.insert(tk.END, value)

# Function to clear the display
def clear_display():
    display.delete(1.0, tk.END)

# Function to perform the calculation
def calculate():
    expression = display.get(1.0, tk.END)
    try:
        result = eval(expression)
        clear_display()
        update_display(result)
    except:
        clear_display()
        update_display("Error")

# Create the main window
window = tk.Tk()
window.title("Calculator")

# Styling the calculator
window.configure(bg='#193b1e')
window.geometry('300x400')
window.resizable(False, False)

# Create the display
display = tk.Text(window, height=2, width=25, font=('Arial', 14))
display.pack(pady=(10, 0))

# Create the number buttons
button_frame = tk.Frame(window, pady=20)
button_frame.pack()

for i in range(9):
    button = tk.Button(button_frame, text=str(i+1), width=5, height=2, font=('Arial', 14),
                       command=lambda num=i+1: update_display(num))
    button.grid(row=i//3, column=i%3, padx=5, pady=7)

# Create the 0 button
zero_button = tk.Button(button_frame, text="0", width=5, height=2, font=('Arial', 14),
                        command=lambda: update_display(0))
zero_button.grid(row=3, column=1, padx=5, pady=7)

# Create the operator buttons
operators = ['+', '-', '*', '/']
for i, operator in enumerate(operators):
    button = tk.Button(button_frame, text=operator, width=5, height=2, font=('Arial', 14),
                       command=lambda op=operator: update_display(op))
    button.grid(row=i, column=3, padx=5, pady=7)

# Create the equal button
equal_button = tk.Button(button_frame, text="=", width=5, height=2, font=('Arial', 14), command=calculate)
equal_button.grid(row=3, column=2, padx=5, pady=7)

# Create the clear button
clear_button = tk.Button(button_frame, text="C", width=5, height=2, font=('Arial', 14), command=clear_display)
clear_button.grid(row=3, column=0, padx=5, pady=7)

# Change button colors
button_frame.configure(bg='#193b1e')
buttons = button_frame.winfo_children()
for button in buttons:
    button.configure(bg='#e4f0df', activebackground='#193b1e')

# Start the main event loop
window.mainloop()



