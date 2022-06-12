from tkinter import *
from calculatorfunctions import *

# Providing basic Tkinter functions
root = Tk()
root.title("Calculator")
root.geometry("500x600")
root.configure(bg="black")

# Label to display inputs
inputList = [4, 5, 9]
displayOutput = " ".join([str(item) for item in inputList])
outputfield = Label(root, background="black", foreground="white", text=displayOutput, font=", 50", padx=25, pady=5)
outputfield.place(x=5, y=5, width=490, height=90)

# Buttons for numbers
button0 = Button(root, text="0", font=", 30", width=4, height=1)
button0.place(x=20, y=500)

button1 = Button(root, text="1", font=", 30", width=4, height=1)
button1.place(x=20, y=400)

button2 = Button(root, text="2", font=", 30", width=4, height=1)
button2.place(x=140, y=400)

button3 = Button(root, text="3", font=", 30", width=4, height=1)
button3.place(x=260, y=400)

button4 = Button(root, text="4", font=", 30", width=4, height=1)
button4.place(x=20, y=300)

button5 = Button(root,  text="5", font=", 30", width=4, height=1)
button5.place(x=140, y=300)

button6 = Button(root, text="6", font=", 30", width=4, height=1)
button6.place(x=260, y=300)

button7 = Button(root, text="7", font=", 30", width=4, height=1)
button7.place(x=20, y=200)

button8 = Button(root, text="8", font=", 30", width=4, height=1)
button8.place(x=140, y=200)

button9 = Button(root, text="9", font=", 30", width=4, height=1)
button9.place(x=260, y=200)

# Buttons for mathematical operations
buttonDecimal = Button(root, background="gray", text=".", font=", 30", width=4, height=1)
buttonDecimal.place(x=140, y=500)

buttonNegative = Button(root, background="gray", text="(-)", font=", 30", width=4, height=1)
buttonNegative.place(x=260, y=500)

buttonEquals = Button(root, background="orange", foreground="white", text="=", font=", 30", width=4, height=1)
buttonEquals.place(x=380, y=460)

buttonAdd = Button(root, background="orange", foreground="white", text="+", font=", 30", width=4, height=1)
buttonAdd.place(x=380, y=370)

buttonSubtract = Button(root, background="orange", foreground="white", text="-", font=", 30", width=4, height=1)
buttonSubtract.place(x=380, y=280)

buttonMultiply = Button(root, background="orange", foreground="white", text="*", font=", 30", width=4, height=1)
buttonMultiply.place(x=380, y=190)

buttonDivide = Button(root, background="orange", foreground="white", text="/", font=", 30", width=4, height=1)
buttonDivide.place(x=380, y=100)

buttonClear = Button(root, background="gray", text="CE", font=", 30", width=4, height=1)
buttonClear.place(x=20, y=100)

buttonMenu = Button(root, background="gray", text="HIST", font=", 30", width=4, height=1)
buttonMenu.place(x=140, y=100)

buttonPower = Button(root, background="gray", text="^", font=", 30", width=4, height=1)
buttonPower.place(x=260, y=100)



# Mainloop which causes this app to run indefinitely
root.mainloop()