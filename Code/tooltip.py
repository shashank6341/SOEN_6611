import tkinter as tk


class ToolTip(object):
    def __init__(self, widget, text):
        self.widget = widget
        self.text = text
        self.tip_window = None

    def show_tip(self):
        """Display text in tooltip window"""
        x, y, _, _ = self.widget.bbox("insert")  # get size of widget
        x += self.widget.winfo_rootx() + 25      # calculate to display tooltip
        y += self.widget.winfo_rooty() + 20      # below and to the right
        self.tip_window = tw = tk.Toplevel(self.widget)  # create new tooltip window
        tw.wm_overrideredirect(True)  # remove all Window Manager (wm) decorations
        tw.wm_geometry(f"+{x}+{y}")  # position tooltip

        label = tk.Label(tw, text=self.text, background="#ffffe0", relief="solid", borderwidth=1)
        label.pack(ipadx=1)

    def hide_tip(self):
        if self.tip_window:
            self.tip_window.destroy()  # destroy tooltip window
            self.tip_window = None

    def hover(self, event=None):
        """Show tooltip when hovering over widget"""
        self.show_tip()

    def unhover(self, event=None):
        """Hide tooltip when stop hovering over widget"""
        self.hide_tip()