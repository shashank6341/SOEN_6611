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

        self.title("METRICSTICS System.")
        self.geometry("300x100")

        self.entry = CustomEntry(self, placeholder="Ex: 1,45,57")
        self.entry.pack(fill=tk.BOTH, padx=10, pady=10)
        
        self.bind("<Button-1>", self.on_window_click)

        # Result Label.
        self.result_label = tk.Label(self, text="Result: ")
        self.result_label.pack(padx=10, pady=5)


        # Calculation Buttons.
        self.min_button = tk.Button(self, text="Minimum", command=self.find_minimum)
        self.min_button.pack(padx=10, pady=5, side=tk.LEFT)

        self.max_button = tk.Button(self, text="Maximum", command=self.find_maximum)
        self.max_button.pack(padx=10, pady=5, side=tk.LEFT)

        self.mode_button = tk.Button(self, text="Mode", command=self.find_mode)
        self.mode_button.pack(padx=10, pady=5, side=tk.LEFT)


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



if __name__ == "__main__":
    app = App()
    app.mainloop()
