import tkinter as tk

class Calculator:
    def __init__(self):
        self.user_input = ""
        self.calculator = ""
        
    def show(self):
        user_input_entry.delete(0, tk.END)
        user_input_entry.insert(0, self.user_input)
        
    def operators(self, operator: str):
        if operator == "x":
            self.calculator = self.calculator + "*"
        elif operator == "÷":
            self.calculator = self.calculator + "/"
        else:
            self.calculator = self.calculator + operator
    
    def input_entry(self, text: str):
        self.user_input = self.user_input + text
        self.operators(text)
        self.show()
        
    def calculate(self):
        try:
            answer = eval(self.calculator)
            self.calculator = str(answer)
            self.user_input = str(answer)
            self.show()
        except:
            self.user_input = "Invalid Input"
            self.show()
            
    def delete(self):
        self.user_input = self.user_input[: -1]
        self.calculator = self.calculator[: -1]
        self.show()
    
    def delete_all(self):
        self.user_input = ""
        self.calculator = ""
        self.show()
  
root = tk.Tk()
process = Calculator()
root.title("Calculator")
root.geometry("420x420")
root.resizable(height=False, width=False)

user_input_entry = tk.Entry(root, font=("Arial", 40), bd=10)
user_input_entry.pack()

button_frame = tk.Frame(root)
button_frame.columnconfigure("0", weight=2)
button_frame.columnconfigure("1", weight=2)
button_frame.columnconfigure("2", weight=2)

button1 = tk.Button(button_frame, text="1", font=("Arial", 20), command=lambda:process.input_entry(str(1))).grid(column=0, row=0, sticky=tk.W+tk.E)
button2 = tk.Button(button_frame, text="2", font=("Arial", 20), command=lambda:process.input_entry(str(2))).grid(column=1, row=0, sticky=tk.W+tk.E)
button3 = tk.Button(button_frame, text="3", font=("Arial", 20), command=lambda:process.input_entry(str(3))).grid(column=2, row=0, sticky=tk.W+tk.E)
button4 = tk.Button(button_frame, text="4", font=("Arial", 20), command=lambda:process.input_entry(str(4))).grid(column=0, row=1, sticky=tk.W+tk.E)
button5 = tk.Button(button_frame, text="5", font=("Arial", 20), command=lambda:process.input_entry(str(5))).grid(column=1, row=1, sticky=tk.W+tk.E)
button6 = tk.Button(button_frame, text="6", font=("Arial", 20), command=lambda:process.input_entry(str(6))).grid(column=2, row=1, sticky=tk.W+tk.E)
button7 = tk.Button(button_frame, text="7", font=("Arial", 20), command=lambda:process.input_entry(str(7))).grid(column=0, row=2, sticky=tk.W+tk.E)
button8 = tk.Button(button_frame, text="8", font=("Arial", 20), command=lambda:process.input_entry(str(8))).grid(column=1, row=2, sticky=tk.W+tk.E)
button9 = tk.Button(button_frame, text="9", font=("Arial", 20), command=lambda:process.input_entry(str(9))).grid(column=2, row=2, sticky=tk.W+tk.E)
buttonC = tk.Button(button_frame, text="C", font=("Arial", 20), command=lambda:process.delete_all()).grid(column=0, row=3, sticky=tk.W+tk.E)
button0 = tk.Button(button_frame, text="0", font=("Arial", 20), command=lambda:process.input_entry(str(0))).grid(column=1, row=3, sticky=tk.W+tk.E)
buttonEqual = tk.Button(button_frame, text="=", font=("Arial", 20), command=lambda:process.calculate()).grid(column=2, row=3, sticky=tk.W+tk.E)
buttonAddition = tk.Button(button_frame, text="+", font=("Arial", 20), command=lambda:process.input_entry("+")).grid(column=0, row=4, sticky=tk.W+tk.E)
buttonSubtraction = tk.Button(button_frame, text="-", font=("Arial", 20), command=lambda:process.input_entry("-")).grid(column=1, row=4, sticky=tk.W+tk.E)
buttonMultiplication = tk.Button(button_frame, text="x", font=("Arial", 20), command=lambda:process.input_entry("x")).grid(column=2, row=4, sticky=tk.W+tk.E)
buttonDivision = tk.Button(button_frame, text="÷", font=("Arial", 20), command=lambda:process.input_entry("÷")).grid(column=1, row=5, sticky=tk.W+tk.E)
buttonDelete = tk.Button(button_frame, text="<", font=("Arial", 20), command=lambda:process.delete()).grid(column=2, row=5, sticky=tk.W+tk.E)
button_frame.pack(fill="x")
root.mainloop()
