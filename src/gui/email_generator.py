import tkinter as tk
from tkinter import ttk
from gui.base_generator import BaseView
from data_generator import generate_random_email, MAX_AMOUNT, LOCALE_MAPPING_INTERNET


class EmailGenerator(BaseView):
    """Email generator view"""

    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        self.title_label['text'] = "Email Generator"
        self.create_additional_widgets()

    def create_additional_widgets(self):
        """Create additional widgets for email generator"""
        actions_list = ["Default", "Free provider",
                        "Company email", "Custom domain"]
        self.add_actions_frame(text="Select email type:",
                               actions_list=actions_list, row=0, column=0)
        self.option_menu.config(state="disabled")
        # Locale selection
        # Set default locale key for email generator
        self.default_locale_key = LOCALE_MAPPING_INTERNET["en_GB"]
        self.add_locale_option(
            default_locale_key=self.default_locale_key, locale_mapping_dict=LOCALE_MAPPING_INTERNET, row=1, column=0)
        # Amount selection spinbox
        self.add_amount_option_spinbox(row=2, column=0)
        # Set default amount for email generator
        # self.entry_count.set(5)
        # Update generate button command
        self.generate_button.config(command=self.generate_emails)

    def generate_emails(self):
        """Generate email addresses based on user input."""
        try:
            count = int(self.entry_count.get())
            if count > MAX_AMOUNT:
                message = f"Number exceeds the maximum allowed ({MAX_AMOUNT}). Setting to maximum."
                self.show_entry_count_message(message)
                self.entry_count.set(MAX_AMOUNT)
                return
            elif count <= 0:
                message = f"Please enter a positive number between 1 and {MAX_AMOUNT}"
                self.show_entry_count_message(message)
                self.entry_count.set(5)
                return
        except Exception as e:
            message = f"Please enter a positive number between 1 and {MAX_AMOUNT}"
            self.show_entry_count_message(message)
            self.entry_count.set(5)
            return

        locale = self.current_locale_key if hasattr(
            self, 'current_locale_key') else "en_GB"

        results = []
        for _ in range(count):
            phones = generate_random_email(locale)
            results.append(phones)

        self.display_results(results)
