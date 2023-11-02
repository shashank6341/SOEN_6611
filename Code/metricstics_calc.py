import tkinter as tk


class CustomEntry(tk.Entry):
    def __init__(self, master=None, placeholder="PLACEHOLDER", color='grey'):
        super().__init__(master)

        self.placeholder = placeholder
        self.placeholder_color = color
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

        self.title("METRICSTICS System")
        self.geometry("600x600")

        self.entry = CustomEntry(self, placeholder="Ex: 1,45,57")
        self.entry.grid(row=0, column=0, columnspan=2, padx=10, pady=5, sticky='ew')
        
        self.bind("<Button-1>", self.on_window_click)

        # Result Label.
        self.result_label = tk.Label(self, text="Result: ")
        self.result_label.grid(row=1, column=0, columnspan=2, padx=10, pady=5)


        # Calculation Buttons.

        # Using "ew" parameter to expand the UI Elements, East - West.

        self.min_button = tk.Button(self, text="Minimum", command=self.find_minimum)
        self.min_button.grid(row=2, column=0, padx=5, pady=5, sticky='ew')

        self.max_button = tk.Button(self, text="Maximum", command=self.find_maximum)
        self.max_button.grid(row=2, column=1, padx=5, pady=5, sticky='ew')

        self.mode_button = tk.Button(self, text="Mode", command=self.find_mode)
        self.mode_button.grid(row=2, column=2, padx=5, pady=5, sticky='ew')

        self.median_btn = tk.Button(self, text="Median", command=self.find_median)
        self.median_btn.grid(row=3, column=0, padx=5, pady=5, sticky='ew')

        self.mean_btn = tk.Button(self, text="Arithmetic Mean", command=self.find_mean)
        self.mean_btn.grid(row=3, column=1, padx=5, pady=5, sticky='ew')

        self.mad_button = tk.Button(self, text="Mean Absolute Deviation", command=self.calculate_mad)
        self.mad_button.grid(row=4, column=0, sticky='ew', padx=5, pady=5)

        self.sd_button = tk.Button(self, text="Standard Deviation", command=self.calculate_sd)
        self.sd_button.grid(row=4, column=1, sticky='ew', padx=5, pady=5)




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

    def find_minimum(self):
        numbers = self._get_numbers()
        if numbers:
            min_val = min(numbers)
            self.result_label.config(text=f"Result: Minimum value is {min_val}")

    def find_maximum(self):
        numbers = self._get_numbers()
        if numbers:
            max_val = max(numbers)
            self.result_label.config(text=f"Result: Maximum value is {max_val}")

    def find_mode(self):
        numbers = self._get_numbers()
        if numbers:
            from collections import Counter
            count = Counter(numbers)
            mode_data = dict(count)
            mode = [k for k, v in mode_data.items() if v == max(list(count.values()))]

            if len(mode) == len(numbers):
                self.result_label.config(text=f"Result: No mode found")
            else:
                self.result_label.config(text=f"Result: Mode is {', '.join(map(str, mode))}")

    def find_median(self):
        values = self._get_numbers()
        if not values:
            return
        values.sort()
        mid = len(values) // 2
        if len(values) % 2 == 0:
            median = (values[mid - 1] + values[mid]) / 2
        else:
            median = values[mid]
        self.result_label.config(text=f"Result: Median is {median}")

    def find_mean(self):
        values = self._get_numbers()
        if not values:
            return
        mean = sum(values) / len(values)
        self.result_label.config(text=f"Result: Arithmetic Mean is {mean}")



    def mean_absolute_deviation(self, numbers):
        mean = sum(numbers) / len(numbers)
        return sum(abs(x - mean) for x in numbers) / len(numbers)

    def standard_deviation(self, numbers):
        mean = sum(numbers) / len(numbers)
        variance = sum((x - mean) ** 2 for x in numbers) / len(numbers)
        return variance ** 0.5
    
    def calculate_mad(self):
        numbers = self._get_numbers()
        if numbers:
            result = self.mean_absolute_deviation(numbers)
            self.result_label.config(text=f"Result: Mean Absolute Deviation is {result:.2f}")
        else:
            tk.messagebox.showerror("Error", "Please enter valid comma-separated numbers!")

    def calculate_sd(self):
        numbers = self._get_numbers()
        if numbers:
            result = self.standard_deviation(numbers)
            self.result_label.config(text=f"Result: Standard Deviation is {result:.2f}")
        else:
            tk.messagebox.showerror("Error", "Please enter valid comma-separated numbers!")




if __name__ == "__main__":
    app = App()
    app.mainloop()
