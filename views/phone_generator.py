import tkinter as tk
from tkinter import ttk
from views.base_generator import BaseView
from utils import generate_random_phone_number, MAX_AMOUNT, LOCALE_MAPPING_PHONE


class PhoneGenerator(BaseView):
    """Phone generator view"""

    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        self.title_label['text'] = "Phone Generator"
        self.create_additional_widgets()

    def create_additional_widgets(self):
        """Create additional widgets for phone generator"""
        # Locale selection
        default_locale_key = LOCALE_MAPPING_PHONE["en_GB"]
        self.add_locale_option(default_locale_key, LOCALE_MAPPING_PHONE)

        # Amount of names to generate
        tk.Label(self.options_frame, text="Amount:").grid(
            row=3, column=0, sticky="w", padx=5, pady=5)
        self.entry_count = tk.IntVar(value=5)
        num_spinbox = ttk.Spinbox(
            self.options_frame, from_=1, to=MAX_AMOUNT, textvariable=self.entry_count, width=10)
        num_spinbox.grid(row=3, column=1, columnspan=3, sticky="w", padx=5)