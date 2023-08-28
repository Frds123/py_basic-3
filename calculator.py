import tkinter as tk
from tkinter import ttk


class SmartWatchPopup:
    def __init__(self, parent):
        self.parent = parent
        self.popup = tk.Toplevel(parent)
        self.popup.title("Colorful Smartwatch")

        self.style = ttk.Style()
        self.style.configure("TButton", font=("Helvetica", 12))

        self.screen = tk.Label(self.popup, text="", font=("Helvetica", 20))
        self.screen.pack(padx=20, pady=20)

        self.next_button = ttk.Button(self.popup, text="Next Screen", command=self.next_screen)
        self.next_button.pack(pady=10)

        self.current_screen = 0
        self.screens = [
            ("Red", "red"),
            ("Green", "green"),
            ("Blue", "blue"),
            ("Yellow", "yellow"),
            ("Purple", "purple"),
        ]

        self.update_screen()

    def update_screen(self):
        name, color = self.screens[self.current_screen]
        self.screen.config(text=name, fg=color)

    def next_screen(self):
        self.current_screen = (self.current_screen + 1) % len(self.screens)
        self.update_screen()


root = tk.Tk()
root.title("Smartwatch Simulator")

popup_button = ttk.Button(root, text="Open Smartwatch", command=lambda: SmartWatchPopup(root))
popup_button.pack(pady=20)

root.mainloop()
