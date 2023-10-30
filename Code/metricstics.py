import tkinter as tk
import csv
import statistics

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("METRICSTICS")

        self.result = 0
        self.current_num = 0
        self.operation = None
        self.values = []

        # create display
        self.display = tk.Entry(master, width=20, font=('Arial', 16))
        self.display.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

        # create buttons
        self.create_button('7', 1, 0)
        self.create_button('8', 1, 1)
        self.create_button('9', 1, 2)
        self.create_button('/', 1, 3)
        self.create_button('4', 2, 0)
        self.create_button('5', 2, 1)
        self.create_button('6', 2, 2)
        self.create_button('*', 2, 3)
        self.create_button('1', 3, 0)
        self.create_button('2', 3, 1)
        self.create_button('3', 3, 2)
        self.create_button('-', 3, 3)
        self.create_button('0', 4, 0)
        self.create_button('C', 4, 1)
        self.create_button('=', 4, 2)
        self.create_button('+', 4, 3)

        # create statistics buttons
        self.create_button('Minimum', 5, 0)
        self.create_button('Maximum', 5, 1)
        self.create_button('Mode', 5, 2)
        self.create_button('Median', 5, 3)
        self.create_button('Mean', 6, 0)
        self.create_button('MAD', 6, 1)
        self.create_button('Std Dev', 6, 2)

        # create file buttons
        self.create_button('Save', 7, 0)
        self.create_button('Load', 7, 1)

    def create_button(self, text, row, col):
        button = tk.Button(self.master, text=text, width=8, height=2, font=('Arial', 16), command=lambda: self.button_click(text))
        button.grid(row=row, column=col, padx=5, pady=5)

    def button_click(self, text):
        if text.isdigit():
            self.current_num = self.current_num * 10 + int(text)
            self.display.delete(0, tk.END)
            self.display.insert(0, str(self.current_num))
        elif text == 'C':
            self.current_num = 0
            self.result = 0
            self.operation = None
            self.display.delete(0, tk.END)
        elif text in ['+', '-', '*', '/']:
            self.calculate()
            self.operation = text
            self.current_num = 0
        elif text == '=':
            self.calculate()
            self.operation = None
            self.current_num = 0
        elif text == 'Minimum' and self.values:
            self.result = min(self.values)
            self.display_result()
        elif text == 'Maximum' and self.values:
            self.result = max(self.values)
            self.display_result()
        elif text == 'Mode' and self.values:
            self.result = statistics.mode(self.values)
            self.display_result()
        elif text == 'Median' and self.values:
            self.result = statistics.median(self.values)
            self.display_result()
        elif text == 'Mean' and self.values:
            self.result = statistics.mean(self.values)
            self.display_result()
        elif text == 'MAD' and self.values:
            self.result = statistics.mean([abs(x - statistics.mean(self.values)) for x in self.values])
            self.display_result()
        elif text == 'Std Dev' and self.values:
            self.result = statistics.stdev(self.values)
            self.display_result()
        elif text == 'Save':
            self.save_to_csv()
        elif text == 'Load':
            self.load_from_csv()

    def calculate(self):
        if self.operation == '+':
            self.result += self.current_num
        elif self.operation == '-':
            self.result -= self.current_num
        elif self.operation == '*':
            self.result *= self.current_num
        elif self.operation == '/':
            if self.current_num == 0:
                raise ValueError("Cannot divide by zero")
            self.result /= self.current_num
        else:
            self.result = self.current_num

        self.display_result()

    def display_result(self):
        self.display.delete(0, tk.END)
        self.display.insert(0, str(self.result))
        self.values.append(self.result)

    def save_to_csv(self):
        with open('calculations.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(self.values)

    def load_from_csv(self):
        with open('calculations.csv', mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                self.values = [int(x) for x in row]
                self.result = self.values[-1]
                self.display_result()

root = tk.Tk()
calculator = Calculator(root)
root.mainloop()
