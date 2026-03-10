import tkinter as tk
from tkinter import ttk
from gui.base_generator import BaseView
from data_generator import generate_random_name, MAX_AMOUNT, LOCALE_MAPPING_NAME


class NameGenerator(BaseView):
    """Name generator view"""

    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        self.title_label['text'] = "Name Generator"
        self.create_additional_widgets()

    def create_additional_widgets(self):
        """Create additional widgets for name generator"""
        actions_list = ["Full Name", "First Name", "Last Name"]
        self.add_actions_frame(text="Select action:",
                                    actions_list=actions_list, row=0, column=0)

        # Gender selection
        tk.Label(self.options_frame, text="Gender:").grid(
            row=1, column=0, sticky="w", padx=5, pady=5)
        self.gender_var = tk.StringVar(value="any")

        # Create a sub-frame for radio buttons
        gender_frame = tk.Frame(self.options_frame)
        gender_frame.grid(row=1, column=1, sticky="w", padx=5)

        # Use pack in the sub-frame
        ttk.Radiobutton(gender_frame, text="Any", variable=self.gender_var,
                        value="any").pack(side="left", padx=(0, 10))
        ttk.Radiobutton(gender_frame, text="Male", variable=self.gender_var,
                        value="male").pack(side="left", padx=(0, 10))
        ttk.Radiobutton(gender_frame, text="Female", variable=self.gender_var,
                        value="female").pack(side="left", padx=(0, 10))
        ttk.Radiobutton(gender_frame, text="Non-binary",
                        variable=self.gender_var, value="non-binary").pack(side="left", padx=(0, 10))

        # Locale selection
        # Set default locale key for phone generator
        self.default_locale_key = LOCALE_MAPPING_NAME["en"]
        self.add_locale_option(
            default_locale_key=self.default_locale_key, locale_mapping_dict=LOCALE_MAPPING_NAME, row=2, column=0)
        # Amount selection spinbox
        self.add_amount_option_spinbox(row=3, column=0)
        # Set default amount for phone generator
        self.entry_count.set(5)
        # Update generate button command
        self.generate_button.config(command=self.generate_names)

    def generate_names(self):
        """Generate names based on selected options and display in text box"""
        count = self.validate_entry_count()
        if not count:
            return

        action = self.action_var.get()
        gender = self.gender_var.get()
        locale = self.current_locale_key if hasattr(
            self, 'current_locale_key') else "en"

        results = []
        for _ in range(count):
            if action == "Full Name":
                name = generate_random_name(sex=gender, locale=locale)
            elif action == "First Name":
                name = generate_random_name(
                    sex=gender, locale=locale).split()[0]
            elif action == "Last Name":
                name = generate_random_name(
                    sex=gender, locale=locale).split()[-1]
            else:
                name = ""
            results.append(name)

        # Show results in the text box
        self.display_results(results)

    def reset_state(self):
        """Reset all UI elements to default values"""
        self.copy_reset_message_label.config(text="Options reset!", fg="red")
        self.copy_reset_message_label.after(
            2000, self.hide_copy_reset_message)  # hide after 2 seconds

        self.action_var.set("Full Name")
        self.gender_var.set("any")
        self.entry_count.set(5)
        self.results_text.config(state="normal")
        self.results_text.delete("1.0", tk.END)
        self.results_text.insert(
            tk.END, "Generated data will appear here...\n")
        self.results_text.config(state="disabled")
        self.copy_button.config(state="disabled")
