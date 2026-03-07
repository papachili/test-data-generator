import tkinter as tk
from tkinter import ttk


class MainMenu(tk.Frame):
    """Main menu view"""

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.create_widgets()

    def create_widgets(self):
        """Create all widgets for Main Menu view"""
        # Title
        title_label = tk.Label(
            self,
            text="Test Data Generator",
            font=("Arial", 20, "bold")
        )
        title_label.pack(pady=30)

        # Container for subtitle and buttons
        sub_btn_frame = tk.Frame(self)
        sub_btn_frame.pack(pady=10)  # Less space overall

        # Subtitle
        subtitle_label = tk.Label(
            sub_btn_frame,
            text="Select a tool to get started:",
            font=("Arial", 12, "bold")
        )
        subtitle_label.pack(pady=(0, 10))  # Small space below subtitle

        # Button container inside the same frame
        button_frame = tk.Frame(sub_btn_frame)
        button_frame.pack()

        # Name Generator Button
        name_btn = ttk.Button(
            button_frame,
            text="👤 Name Generator",
            command=lambda: self.controller.show_frame('NameGenerator'),
            width=25
        )
        name_btn.pack(pady=10)

        # Phone Generator Button
        phone_btn = ttk.Button(
            button_frame,
            text="📱 Phone Generator",
            command=lambda: self.controller.show_frame('PhoneGenerator'),
            width=25
        )
        phone_btn.pack(pady=10)
        self.add_version_footer()

    def add_version_footer(self):
        from app import __version__
        """Add a footer label to display the application version."""
        # Footer with version number
        footer_frame = tk.Frame(self)
        footer_label = tk.Label(
            self, text=f"Version {__version__}", font=("Arial", 10))
        footer_label.place(relx=1.0, rely=1.0, anchor="se", height=20)

        version_label = tk.Label(
            footer_frame,
            text=f"Version {__version__}",
            font=("Arial", 10),
        )
        version_label.pack(side=tk.RIGHT, padx=5)
