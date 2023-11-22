import tkinter as tk


class ToolTip(object):
    def __init__(self, widget, text):
        self.widget = widget
        self.text = text
        self.tip_window = tk.Toplevel(self.widget)
        self.tip_window.wm_overrideredirect(True)  # remove all Window Manager (wm) decorations
        self.label = tk.Label(self.tip_window, text=self.text, background="#ffffe0", relief="solid", borderwidth=1)
        self.label.pack(ipadx=1)
        self.hide_tip()  # Hide tooltip initially

    def show_tip(self):
        """Display text in tooltip window"""
        x, y, _, _ = self.widget.bbox("insert")  # get size of widget
        x += self.widget.winfo_rootx() + 25      # calculate to display tooltip
        y += self.widget.winfo_rooty() + 20      # below and to the right
        self.tip_window.wm_geometry(f"+{x}+{y}")  # position tooltip
        self.tip_window.deiconify()  # Show tooltip

    def hide_tip(self):
        self.tip_window.withdraw()  # Hide tooltip

    def hover(self, event=None):
        """Show tooltip when hovering over widget"""
        self.show_tip()

    def unhover(self, event=None):
        """Hide tooltip when stop hovering over widget"""
        self.hide_tip()