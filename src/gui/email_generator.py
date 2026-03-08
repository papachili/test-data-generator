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
        self.actions_dict = {"default": "Default", "free": "Free provider",
                             "company": "Company email", "custom": "Custom domain"}
        actions_list = [value for value in self.actions_dict.values()]
        self.add_actions_frame(text="Select email type:",
                                    actions_list=actions_list, command=self.show_hide_custom_domain_entry, row=0, column=0)
        self.add_hidden_custom_domain_entry()
        # Locale selection
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
        count = self.validate_entry_count()
        if not count:
            return

        locale = self.current_locale_key if hasattr(
            self, 'current_locale_key') else "en_GB"

        email_type = self.action_var.get()
        email_type_key = {v: k for k,
                          v in self.actions_dict.items()}.get(email_type)

        if email_type_key == "custom":
            custom_domain = self.custom_entry.get().strip("@")
        else:
            custom_domain = None

        results = []
        for _ in range(count):
            phones = generate_random_email(
                locale, email_type_key, custom_domain)
            results.append(phones)

        self.display_results(results)

    def add_hidden_custom_domain_entry(self):
        self.custom_entry = tk.Entry(self.options_frame, width=15)
        self.custom_entry.insert(0, "@example.com")
        self.custom_entry.grid(row=0, column=2)
        self.custom_entry.grid_forget()

    def show_hide_custom_domain_entry(self, value):
        if value == "Custom domain":
            self.custom_entry.grid(row=0, column=2)
        else:
            self.custom_entry.grid_forget()
