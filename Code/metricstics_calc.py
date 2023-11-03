import threading
import tkinter as tk
from tkinter import messagebox
import csv


class CustomEntry(tk.Entry):
    def __init__(self, master=None, placeholder="PLACEHOLDER", placeholder_color='grey', **kwargs):
        super().__init__(master, **kwargs)

        self.placeholder = placeholder
        self.placeholder_color = placeholder_color
        self.default_fg_color = self['fg']

        self.bind("<FocusIn>", self._on_focus_in)
        self.bind("<FocusOut>", self._on_focus_out)

        self.put_placeholder()

    def put_placeholder(self):
        self.insert(0, self.placeholder)
        self['fg'] = self.placeholder_color

    def _on_focus_in(self, _):
        if self['fg'] == self.placeholder_color:
            self.delete('0', 'end')
            self['fg'] = self.default_fg_color

    def _on_focus_out(self, _):
        if not self.get().strip():
            self.put_placeholder()


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.calculation_results = {
            'Minimum': '',
            'Maximum': '',
            'Mode': '',
            'Median': '',
            'Arithmetic Mean': '',
            'Mean Absolute Deviation': '',
            'Standard Deviation': ''
        }

        self.title("METRICSTICS System")
        self.geometry("600x600")

        for i in range(3):  # Since you have 3 columns
            self.columnconfigure(i, weight=1)

        self.entry = CustomEntry(self, placeholder="Ex: 1,45,57")
        self.entry.grid(row=0, column=0, columnspan=3, padx=10, pady=5, sticky='ew')

        self.bind("<Button-1>", self.on_window_click)

        # Result Label.
        self.result_label = tk.Label(self, text="Result: ")
        self.result_label.grid(row=1, column=0, columnspan=3, padx=10, pady=5, sticky='w')

        # Calculation Buttons

        # Using "ew" parameter to expand the UI Elements, East - West.

        self.min_button = tk.Button(self, text="Minimum", command=lambda: self.calculate(self.find_minimum))
        self.min_button.grid(row=2, column=0, padx=5, pady=5, sticky='ew')

        self.max_button = tk.Button(self, text="Maximum", command=lambda: self.calculate(self.find_maximum))
        self.max_button.grid(row=2, column=1, padx=5, pady=5, sticky='ew')

        self.mode_button = tk.Button(self, text="Mode", command=lambda: self.calculate(self.find_mode))
        self.mode_button.grid(row=2, column=2, padx=5, pady=5, sticky='ew')

        self.median_btn = tk.Button(self, text="Median", command=lambda: self.calculate(self.find_median))
        self.median_btn.grid(row=3, column=0, padx=5, pady=5, sticky='ew')

        self.mean_btn = tk.Button(self, text="Arithmetic Mean", command=lambda: self.calculate(self.find_mean))
        self.mean_btn.grid(row=3, column=1, padx=5, pady=5, sticky='ew')

        self.mad_button = tk.Button(self, text="Mean Absolute Deviation", command=lambda: self.calculate(self.calculate_mad))
        self.mad_button.grid(row=4, column=0, padx=5, pady=5, sticky='ew')

        self.sd_button = tk.Button(self, text="Standard Deviation", command=lambda: self.calculate(self.calculate_sd))
        self.sd_button.grid(row=4, column=1, padx=5, pady=5, sticky='ew')

        self.csv_button = tk.Button(self, text="Store to CSV", command=self.export_to_csv_threaded)
        self.csv_button.grid(row=5, column=0, columnspan=3, padx=5, pady=5, sticky='ew')

    def on_window_click(self, event):
        widget = self.winfo_containing(event.x_root, event.y_root)
        if widget != self.entry:
            self.focus_set()

    def _get_numbers(self):
        try:
            numbers = [float(num.strip()) for num in self.entry.get().split(',') if num]
            return numbers
        except ValueError:
            tk.messagebox.showerror("Error", "Please enter valid comma-separated numbers!")
            return []

    def calculate(self, func):
        threading.Thread(target=self._calculate, args=(func,)).start()

    def _calculate(self, func):
        numbers = self._get_numbers()
        if numbers:
            result = func(numbers)
            self.result_label.config(text=f"Result: {result}")
        else:
            tk.messagebox.showerror("Error", "Please enter valid comma-separated numbers!")

    def find_minimum(self, numbers):
        result = min(numbers)
        self.calculation_results['Minimum'] = result
        return f"{result} (Minimum)"

    def find_maximum(self, numbers):
        result = {max(numbers)}
        self.calculation_results['Maximum'] = result
        return f"{result} (Maximum)"

    def find_mode(self, numbers):
        from collections import Counter
        count = Counter(numbers)
        mode_data = dict(count)
        mode = [k for k, v in mode_data.items() if v == max(list(count.values()))]

        if len(mode) == len(numbers):
            return "No mode found"
        else:
            # result = f"{', '.join(map(str, mode))} (Mode)"
            result = {', '.join(map(str, mode))}
            self.calculation_results['Mode'] = result
            return f"{result} (Mode)"

    def find_median(self, numbers):
        numbers.sort()
        mid = len(numbers) // 2
        if len(numbers) % 2 == 0:
            median = (numbers[mid - 1] + numbers[mid]) / 2
            self.calculation_results['Median'] = median
        else:
            median = numbers[mid]
            self.calculation_results['Median'] = median
        return f"{median} (Median)"

    def find_mean(self, numbers):
        mean = sum(numbers) / len(numbers)
        self.calculation_results['Arithmetic Mean'] = mean
        return f"{mean} (Arithmetic Mean)"

    def mean_absolute_deviation(self, numbers):
        mean = sum(numbers) / len(numbers)
        return sum(abs(x - mean) for x in numbers) / len(numbers)

    def standard_deviation(self, numbers):
        mean = sum(numbers) / len(numbers)
        variance = sum((x - mean) ** 2 for x in numbers) / len(numbers)
        return variance ** 0.5

    def calculate_mad(self, numbers):
        result = self.mean_absolute_deviation(numbers)
        self.calculation_results['Mean Absolute Deviation'] = result
        return f"{result:.2f} (Mean Absolute Deviation)"

    def calculate_sd(self, numbers):
        result = self.standard_deviation(numbers)
        self.calculation_results['Standard Deviation'] = result
        return f"{result:.2f} (Standard Deviation)"
    
    def export_to_csv(self):
        with open('results.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(self.calculation_results.keys())  # Writing the headers
            writer.writerow(self.calculation_results.values())  # Writing the values

    
    def export_to_csv_threaded(self):
        threading.Thread(target=self.export_to_csv).start()


if __name__ == "__main__":
    app = App()
    app.mainloop()
