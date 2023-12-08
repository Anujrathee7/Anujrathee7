import tkinter as tk

window = tk.Tk()
window.title("Pocket Calculator") # Name of the application
window.geometry("330x380")# Size 

 
# Entry field for display
entry = tk.Entry(window, width=25, font=('Arial', 18), justify='right')
entry.place(x=0, y=0)

def button_click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + value)

def press_1():
    button_click("1")

def press_2():
    button_click("2")

def press_3():
    button_click("3")

def press_div():
    button_click("/")

def press_4():
    button_click("4")

def press_5():
    button_click("5")

def press_6():
    button_click("6")

def press_prod():
    button_click("*")

def press_7():
    button_click("7")

def press_8():
    button_click("8")

def press_9():
    button_click("9")

def press_plus():
    button_click("+")

def press_0():
    button_click("0")

def press_dot():
    button_click(".")

def press_eq():
    calculate()

def press_minus():
    button_click("-")

# Function to calculate the result
def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")


b1 = tk.Button(window, text="1", height= 1, width=3, font=('Arial', 22),
               command=press_1)

b2 = tk.Button(window, text= "2", height= 1, width=3, font=('Arial', 22),
               command=press_2)

b3 = tk.Button(window, text= "3", height= 1, width=3, font=('Arial', 22),
               command=press_3)

bdiv = tk.Button(window, text = "/", height= 1, width=3, font=('Arial', 22),
               command=press_div)

b1.place(x=20, y=60)
b2.place(x=100, y=60)
b3.place(x=180, y=60)
bdiv.place(x=260, y=60)

b4 = tk.Button(window, text= "4", height= 1, width=3, font=('Arial', 22), command=press_4)
b5 = tk.Button(window, text= "5", height= 1, width=3, font=('Arial', 22), command=press_5)
b6 = tk.Button(window, text= "6", height= 1, width=3, font=('Arial', 22), command=press_6)
bprod = tk.Button(window, text= "*", height= 1, width=3, font=('Arial', 22), command=press_prod)

b4.place(x=20, y=140)
b5.place(x=100, y=140)
b6.place(x=180, y=140)
bprod.place(x=260, y=140)

b7 = tk.Button(window, text= "7", height= 1, width=3, font=('Arial', 22), command=press_7)
b8 = tk.Button(window, text= "8", height= 1, width=3, font=('Arial', 22), command=press_8)
b9 = tk.Button(window, text= "9", height= 1, width=3, font=('Arial', 22), command=press_9)
bplus = tk.Button(window, text= "+", height= 1, width=3, font=('Arial', 22), command=press_plus)

b7.place(x=20, y=220)
b8.place(x=100, y=220)
b9.place(x=180, y=220)
bplus.place(x=260, y=220)

b0 = tk.Button(window, text= "0", height= 1, width=3, font=('Arial', 22),
               command=press_0)

bdot = tk.Button(window, text=" . ", height= 1, width=3, font=('Arial', 22),
               command=press_dot)

beq = tk.Button(window, text=" = ", height= 1, width=3, font=('Arial', 22),
               command=press_eq)

bminus = tk.Button(window, text=" - ", height= 1, width=3, font=('Arial', 22),
               command=press_minus)

b0.place(x=20, y=300)
bdot.place(x=100, y=300)
beq.place(x=180, y=300)
bminus.place(x=260, y=300)

window.mainloop

