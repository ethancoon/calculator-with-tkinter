from tkinter import *

# Providing basic functionality for the display
root = Tk()
root.title("Calculator")
root.geometry("500x600")
root.configure(bg="black")
root.iconbitmap("calculator.ico")

# Label to display inputs
expression = ""
displayInput = StringVar()
inputField = Label(root, textvariable=displayInput, wraplength=230, anchor="w", background="black", foreground="white", font=", 35", padx=25, pady=5)
inputField.place(x=5, y=5, width=245, height=90)

# Label to display outputs
displayOutput = StringVar()
outputField = Label(root, textvariable=displayOutput, wraplength=230, anchor="e", background="black", foreground="white", font=", 35", padx=25, pady=5)
outputField.place(x=250, y=5, width=245, height=90)

# Function to display the inputs in the inputField
def inputText(symbol):
    global expression
    if len(expression) < 16:
        expression += str(symbol)
        displayInput.set(expression.replace(" ** ", " ^ "))

# Function to the outputs in the outputField
def equal():
    try:
        global expression
        result = str(eval(expression))
        displayOutput.set('%g' % float(result))
    except:
        displayOutput.set("Error")
        expression = "" 

# Function to clear the expression and output
def clear():
    global expression
    expression = ""
    displayInput.set("")
    displayOutput.set("")

# Function to clear calculator screen and display history of expression and result inputs.
# def history():

# Buttons for numbers
button0 = Button(root, text="0", font=", 30", width=4, height=1, command=lambda: inputText("0")).place(x=20, y=500)

button1 = Button(root, text="1", font=", 30", width=4, height=1, command=lambda: inputText("1")).place(x=20, y=400)

button2 = Button(root, text="2", font=", 30", width=4, height=1, command=lambda: inputText("2")).place(x=140, y=400)

button3 = Button(root, text="3", font=", 30", width=4, height=1, command=lambda: inputText("3")).place(x=260, y=400)

button4 = Button(root, text="4", font=", 30", width=4, height=1, command=lambda: inputText("4")).place(x=20, y=300)

button5 = Button(root,  text="5", font=", 30", width=4, height=1, command=lambda: inputText("5")).place(x=140, y=300)

button6 = Button(root, text="6", font=", 30", width=4, height=1, command=lambda: inputText("6")).place(x=260, y=300)

button7 = Button(root, text="7", font=", 30", width=4, height=1, command=lambda: inputText("7")).place(x=20, y=200)

button8 = Button(root, text="8", font=", 30", width=4, height=1, command=lambda: inputText("8")).place(x=140, y=200)

button9 = Button(root, text="9", font=", 30", width=4, height=1, command=lambda: inputText("9")).place(x=260, y=200)

# Buttons for mathematical operations
buttonDecimal = Button(root, background="gray", text=".", font=", 30", width=4, height=1, command=lambda: inputText(".")).place(x=140, y=500)

buttonNegative = Button(root, background="gray", text="(-)", font=", 30", width=4, height=1, command=lambda: inputText("-")).place(x=260, y=500)

buttonEquals = Button(root, background="orange", foreground="white", text="=", font=", 30", width=4, height=1, command=equal).place(x=380, y=460)

buttonAdd = Button(root, background="orange", foreground="white", text="+", font=", 30", width=4, height=1, command=lambda: inputText(" + ")).place(x=380, y=370)

buttonSubtract = Button(root, background="orange", foreground="white", text="-", font=", 30", width=4, height=1, command=lambda: inputText(" - ")).place(x=380, y=280)

buttonMultiply = Button(root, background="orange", foreground="white", text="*", font=", 30", width=4, height=1, command=lambda: inputText(" * ")).place(x=380, y=190)

buttonDivide = Button(root, background="orange", foreground="white", text="/", font=", 30", width=4, height=1, command=lambda: inputText(" / ")).place(x=380, y=100)

buttonClear = Button(root, background="gray", text="CE", font=", 30", width=4, height=1, command=clear).place(x=20, y=100)

buttonMenu = Button(root, background="gray", text="HIST", font=", 30", width=4, height=1).place(x=140, y=100)

buttonPower = Button(root, background="gray", text="^", font=", 30", width=4, height=1, command=lambda: inputText(" ** ")).place(x=260, y=100)

# Mainloop which causes this app to run indefinitely
root.mainloop()