import tkinter as tk
from tkinter import ttk
from gui.base_generator import BaseView
from data_generator import generate_random_phone_number, MAX_AMOUNT, LOCALE_MAPPING_PHONE


class PhoneGenerator(BaseView):
    """Phone generator view"""

    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        self.title_label['text'] = "Phone Generator"
        self.create_additional_widgets()

    def create_additional_widgets(self):
        """Create additional widgets for phone generator"""
        # Locale selection
        # Set default locale key for phone generator
        self.default_locale_key = LOCALE_MAPPING_PHONE["en_GB"]
        self.add_locale_option(
            default_locale_key=self.default_locale_key, locale_mapping_dict=LOCALE_MAPPING_PHONE)
        # Amount selection spinbox
        self.add_amount_option_spinbox(row=1, column=0)
        # Set default amount for phone generator
        self.entry_count.set(5)
        # Update generate button command
        self.generate_button.config(command=self.generate_phones)
        # Update Reset button command
        self.reset_button.config(command=self.reset_state)

    def generate_phones(self):
        """Generate phone numbers based on user input."""
        count = self.validate_entry_count()
        if not count:
            return

        locale = self.current_locale_key if hasattr(
            self, 'current_locale_key') else "en_GB"

        results = []
        for _ in range(count):
            phones = generate_random_phone_number(locale)
            results.append(phones)

        self.display_results(results)

    def reset_state(self):
        """Reset all UI elements to default values"""
        self.locale_var.set(self.default_locale_key)
        super().reset_options()
