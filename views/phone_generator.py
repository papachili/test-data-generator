import tkinter as tk
from tkinter import ttk


class PhoneGenerator(tk.Frame):
    """Phone generator view"""

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.create_widgets()

    def create_widgets(self):
        """Create all widgets for phone generator"""
        # Header
        header_frame = tk.Frame(self)
        header_frame.pack(fill="x", padx=20, pady=10)

        # Back button
        back_btn = ttk.Button(
            header_frame,
            text="← Back",
            command=lambda: self.controller.show_frame('MainMenu')
        )
        back_btn.pack(side="left")

        # Title
        title_label = tk.Label(
            header_frame,
            text="Phone Generator",
            font=("Arial", 16, "bold")
        )
        title_label.pack(side="left", padx=20)

    def on_show(self):
        """Called when this frame is shown"""
        pass
