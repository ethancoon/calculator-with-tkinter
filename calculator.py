from tkinter import *

# Providing basic functionality for the display
root = Tk()
root.title("Calculator")
root.geometry("500x600")
root.configure(bg="black")
root.iconbitmap("calculator.ico")

# Frame for history window that is hidden when the program loads
historyFrame = Frame(root, width=500, height=600, bg="black")
historyFrame.place(x=0, y=0)

# The two lists in the history window, inputs on left and outputs on right
historyInputList = []
historyOutputList = []

# Frame for main calculator window
calculatorFrame = Frame(root, width=500, height=600, bg="black")
calculatorFrame.place(x=0, y=0)

# Label to display the calculator expression in the calculator window
expression = ""
displayInput = StringVar()
inputField = Label(calculatorFrame, textvariable=displayInput, wraplength=230, anchor="w", background="black", foreground="white", font=", 35", padx=25, pady=5)
inputField.place(x=5, y=5, width=245, height=90)

# Label to display calculator result in the calculator window
displayOutput = StringVar()
outputField = Label(calculatorFrame, textvariable=displayOutput, wraplength=230, anchor="e", background="black", foreground="white", font=", 35", padx=25, pady=5)
outputField.place(x=250, y=5, width=245, height=90)

# Function called when buttons are pressed to add numbers or operations to the expression
def inputText(symbol):
    global expression
    if len(expression) < 16:
        expression += str(symbol)
        displayInput.set(expression.replace(" ** ", " ^ "))

# Function called when equals button is pressed, used to find the result of the expression. 
def equal():
    try:
        # Displaying the result in the calculator window
        global expression
        result = str(eval(expression))
        displayOutput.set('%g' % float(result))

        # Used to add to the list displayed in the history window, and removes elements past index 7 of the list
        historyInputList.insert(0, expression.replace(" ** ", " ^ "))
        historyOutputList.insert(0, ('%g' % float(result)))
        if len(historyInputList) > 8:
            historyInputList.pop(8)
            historyOutputList.pop(8) 
    except:
        result = "Error"
        displayOutput.set(result)
        expression = "" 

# Function to clear the expression and result from the calculator window
def clear():
    global expression
    expression = ""
    displayInput.set("")
    displayOutput.set("")

# Shows history window, while determining which labels should be filled with a value
def history():
    historyFrame.tkraise()
    for index in range(0, len(historyInputList)):
        if index == 0:
            firstInputField.set(historyInputList[index])
            firstOutputField.set(historyOutputList[index])
        elif index == 1:
            secondInputField.set(historyInputList[index])
            secondOutputField.set(historyOutputList[index])
        elif index == 2:
            thirdInputField.set(historyInputList[index])
            thirdOutputField.set(historyOutputList[index])
        elif index == 3:
            fourthInputField.set(historyInputList[index])
            fourthOutputField.set(historyOutputList[index])
        elif index == 4:
            fifthInputField.set(historyInputList[index])
            fifthOutputField.set(historyOutputList[index])
        elif index == 5:
            sixthInputField.set(historyInputList[index])
            sixthOutputField.set(historyOutputList[index])
        elif index == 6:
            seventhInputField.set(historyInputList[index])
            seventhOutputField.set(historyOutputList[index])
        elif index == 7:
            eighthInputField.set(historyInputList[index])
            eighthOutputField.set(historyOutputList[index])

# When the exit button in the history window is hit, the calculator window will appear
def historyExit():
    calculatorFrame.tkraise()

# Buttons for numbers in calculator window
button0 = Button(calculatorFrame, text="0", font=", 30", width=4, height=1, command=lambda: inputText("0")).place(x=20, y=500)

button1 = Button(calculatorFrame, text="1", font=", 30", width=4, height=1, command=lambda: inputText("1")).place(x=20, y=400)

button2 = Button(calculatorFrame, text="2", font=", 30", width=4, height=1, command=lambda: inputText("2")).place(x=140, y=400)

button3 = Button(calculatorFrame, text="3", font=", 30", width=4, height=1, command=lambda: inputText("3")).place(x=260, y=400)

button4 = Button(calculatorFrame, text="4", font=", 30", width=4, height=1, command=lambda: inputText("4")).place(x=20, y=300)

button5 = Button(calculatorFrame, text="5", font=", 30", width=4, height=1, command=lambda: inputText("5")).place(x=140, y=300)

button6 = Button(calculatorFrame, text="6", font=", 30", width=4, height=1, command=lambda: inputText("6")).place(x=260, y=300)

button7 = Button(calculatorFrame, text="7", font=", 30", width=4, height=1, command=lambda: inputText("7")).place(x=20, y=200)

button8 = Button(calculatorFrame, text="8", font=", 30", width=4, height=1, command=lambda: inputText("8")).place(x=140, y=200)

button9 = Button(calculatorFrame, text="9", font=", 30", width=4, height=1, command=lambda: inputText("9")).place(x=260, y=200)

# Buttons for mathematical operations in calculator window
buttonDecimal = Button(calculatorFrame, background="gray", text=".", font=", 30", width=4, height=1, command=lambda: inputText(".")).place(x=140, y=500)

buttonNegative = Button(calculatorFrame, background="gray", text="(-)", font=", 30", width=4, height=1, command=lambda: inputText("-")).place(x=260, y=500)

buttonEquals = Button(calculatorFrame, background="orange", foreground="white", text="=", font=", 30", width=4, height=1, command=equal).place(x=380, y=460)

buttonAdd = Button(calculatorFrame, background="orange", foreground="white", text="+", font=", 30", width=4, height=1, command=lambda: inputText(" + ")).place(x=380, y=370)

buttonSubtract = Button(calculatorFrame, background="orange", foreground="white", text="-", font=", 30", width=4, height=1, command=lambda: inputText(" - ")).place(x=380, y=280)

buttonMultiply = Button(calculatorFrame, background="orange", foreground="white", text="*", font=", 30", width=4, height=1, command=lambda: inputText(" * ")).place(x=380, y=190)

buttonDivide = Button(calculatorFrame, background="orange", foreground="white", text="/", font=", 30", width=4, height=1, command=lambda: inputText(" / ")).place(x=380, y=100)

buttonClear = Button(calculatorFrame, background="gray", text="CE", font=", 30", width=4, height=1, command=clear).place(x=20, y=100)

buttonHistory = Button(calculatorFrame, background="gray", text="HIST", font=", 30", width=4, height=1, command=history).place(x=140, y=100)

buttonPower = Button(calculatorFrame, background="gray", text="^", font=", 30", width=4, height=1, command=lambda: inputText(" ** ")).place(x=260, y=100)

# Labels to display the previous expressions in history window
firstInputField = StringVar()
secondInputField = StringVar()
thirdInputField = StringVar()
fourthInputField = StringVar()
fifthInputField = StringVar()
sixthInputField = StringVar()
seventhInputField = StringVar()
eighthInputField = StringVar()

historyFirstInputField = Label(historyFrame, textvariable=firstInputField, wraplength=230, anchor="w", background="black", foreground="white", font=", 30", padx=25, pady=5).place(x=5, y=100, width=245, height=90)

historySecondInputField = Label(historyFrame, textvariable=secondInputField, wraplength=230, anchor="w", background="black", foreground="white", font=", 30", padx=25, pady=5).place(x=5, y=160, width=245, height=90)

historyThirdInputField = Label(historyFrame, textvariable=thirdInputField, wraplength=230, anchor="w", background="black", foreground="white", font=", 30", padx=25, pady=5).place(x=5, y=220, width=245, height=90)

historyFourthInputField = Label(historyFrame, textvariable=fourthInputField, wraplength=230, anchor="w", background="black", foreground="white", font=", 30", padx=25, pady=5).place(x=5, y=280, width=245, height=90)

historyFifthInputField = Label(historyFrame, textvariable=fifthInputField, wraplength=230, anchor="w", background="black", foreground="white", font=", 30", padx=25, pady=5).place(x=5, y=340, width=245, height=90)

historySixthInputField = Label(historyFrame, textvariable=sixthInputField, wraplength=230, anchor="w", background="black", foreground="white", font=", 30", padx=25, pady=5).place(x=5, y=400, width=245, height=90)

historySeventhInputField = Label(historyFrame, textvariable=seventhInputField, wraplength=230, anchor="w", background="black", foreground="white", font=", 30", padx=25, pady=5).place(x=5, y=460, width=245, height=90)

historyEighthInputField = Label(historyFrame, textvariable=eighthInputField, wraplength=230, anchor="w", background="black", foreground="white", font=", 30", padx=25, pady=5).place(x=5, y=520, width=245, height=90)

# Labels to display previous results in history frame
firstOutputField = StringVar()
secondOutputField = StringVar()
thirdOutputField = StringVar()
fourthOutputField = StringVar()
fifthOutputField = StringVar()
sixthOutputField = StringVar()
seventhOutputField = StringVar()
eighthOutputField = StringVar()

historyFirstOutputField = Label(historyFrame, textvariable=firstOutputField, wraplength=230, anchor="e", background="black", foreground="white", font=", 30", padx=25, pady=5).place(x=250, y=100, width=245, height=90)

historySecondOutputField = Label(historyFrame, textvariable=secondOutputField, wraplength=230, anchor="e", background="black", foreground="white", font=", 30", padx=25, pady=5).place(x=250, y=160, width=245, height=90)

historyThirdOutputField = Label(historyFrame, textvariable=thirdOutputField, wraplength=230, anchor="e", background="black", foreground="white", font=", 30", padx=25, pady=5).place(x=250, y=220, width=245, height=90)

historyFourthOutputField = Label(historyFrame, textvariable=fourthOutputField, wraplength=230, anchor="e", background="black", foreground="white", font=", 30", padx=25, pady=5).place(x=250, y=280, width=245, height=90)

historyFifthOutputField = Label(historyFrame, textvariable=fifthOutputField, wraplength=230, anchor="e", background="black", foreground="white", font=", 30", padx=25, pady=5).place(x=250, y=340, width=245, height=90)

historySixthOutputField = Label(historyFrame, textvariable=sixthOutputField, wraplength=230, anchor="e", background="black", foreground="white", font=", 30", padx=25, pady=5).place(x=250, y=400, width=245, height=90)

historySeventhOutputField = Label(historyFrame, textvariable=seventhOutputField, wraplength=230, anchor="e", background="black", foreground="white", font=", 30", padx=25, pady=5).place(x=250, y=460, width=245, height=90)

historyEighthOutputField = Label(historyFrame, textvariable=eighthOutputField, wraplength=230, anchor="e", background="black", foreground="white", font=", 30", padx=25, pady=5).place(x=250, y=520, width=245, height=90)

# Title label in history window
historyTitle = Label(historyFrame, text="HISTORY:", wraplength=230, anchor="w", background="black", foreground="white", font=", 35", padx=25, pady=5).place(x=5, y=20, width=245, height=90)

# Button to exit history window
historyExitButton = Button(historyFrame, background="gray", text="EXIT", font=", 30", width=4, height=1, command=historyExit).place(x=380, y=20)

# Mainloop which causes this app to run indefinitely
root.mainloop()