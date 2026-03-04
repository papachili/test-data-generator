import tkinter as tk
from tkinter import ttk


class MainMenu(tk.Frame):
    """Main menu view"""

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.create_widgets()

    def create_widgets(self):
        """Create all widgets for this view"""
        # Title
        title_label = tk.Label(
            self,
            text="Test Data Generator",
            font=("Arial", 20, "bold")
        )
        title_label.pack(pady=30)

        # Subtitle
        subtitle_label = tk.Label(
            self,
            text="Select a tool to get started",
            font=("Arial", 12)
        )
        subtitle_label.pack(pady=(0, 40))

        # Button container
        button_frame = tk.Frame(self)
        button_frame.pack(expand=True)

        # Phone Generator Button
        phone_btn = ttk.Button(
            button_frame,
            text="📱 Phone Generator",
            command=lambda: self.controller.show_frame('PhoneGenerator'),
            width=25
        )
        phone_btn.pack(pady=10)

        # Name Generator Button
        name_btn = ttk.Button(
            button_frame,
            text="👤 Name Generator",
            command=lambda: self.controller.show_frame('NameGenerator'),
            width=25
        )
        name_btn.pack(pady=10)