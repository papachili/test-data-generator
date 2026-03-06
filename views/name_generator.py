import tkinter as tk
from tkinter import ttk, messagebox
from utils import generate_random_name, MAX_AMOUNT, LOCALE_MAPPING_NAME


class NameGenerator(tk.Frame):
    """Name generator view"""

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.create_widgets()

    def create_widgets(self):
        """Create all widgets for name generator"""
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
            text="Name Generator",
            font=("Arial", 16, "bold")
        )
        title_label.pack(side="left", padx=20)

        # Main content
        self.content_frame = tk.Frame(self)
        self.content_frame.pack(expand=True, fill="both", padx=40, pady=20)

        # Options frame
        self.options_frame = tk.LabelFrame(
            self.content_frame, text="Options", padx=10, pady=10)
        self.options_frame.pack(fill="x", pady=(0, 20))

        # Action selection
        tk.Label(self.options_frame, text="Select action:").grid(
            row=0, column=0, padx=5, pady=5, sticky="w")
        self.action_var = tk.StringVar(value="Full Name")
        actions = ["Full Name", "First Name", "Last Name"]
        ttk.OptionMenu(self.options_frame, self.action_var,
                       actions[0], *actions).grid(row=0, column=1, padx=5, sticky="w")

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
        tk.Label(self.options_frame, text="Region/Language").grid(
            row=2, column=0, padx=5, pady=5, sticky="w")

        self.locale_var = tk.StringVar(value=LOCALE_MAPPING_NAME["en"])

        locale_combo = ttk.Combobox(
            self.options_frame,
            textvariable=self.locale_var,
            # All locale display values
            values=list(LOCALE_MAPPING_NAME.values()),
            state="readonly",  # Prevent typing, only selection
            width=25  # Adjust width as needed
        )
        locale_combo.grid(row=2, column=1, padx=5, sticky="w")

        # Bind selection event (similar to OptionMenu's command)
        locale_combo.bind("<<ComboboxSelected>>", self.on_locale_select)

        # Number of names
        tk.Label(self.options_frame, text="Number of names:").grid(
            row=3, column=0, sticky="w", padx=5, pady=5)
        self.entry_count = tk.IntVar(value=5)
        num_spinbox = ttk.Spinbox(
            self.options_frame, from_=1, to=MAX_AMOUNT, textvariable=self.entry_count, width=10)
        num_spinbox.grid(row=3, column=1, columnspan=3, sticky="w", padx=5)

        # Label for entry_count status messages
        self.entry_count_label = tk.Label(
            self.content_frame, text="")
        self.entry_count_label.pack()

        # Generate button
        generate_btn = ttk.Button(
            self.content_frame,
            text="Generate Names",
            command=self.generate_names,
            width=20
        )
        generate_btn.pack(pady=(0, 20))

        # Results area
        results_frame = tk.LabelFrame(
            self.content_frame, text="Generated Names", padx=10, pady=10)
        results_frame.pack(expand=True, fill="both")

        # Text widget for displaying names
        self.results_text = tk.Text(results_frame, height=10, width=40)
        self.results_text.pack(side="left", expand=True, fill="both")
        self.results_text.insert(
            tk.END, "Generated data will appear here...\n")
        self.results_text.config(state="disabled")
        self.scrollbar = tk.Scrollbar(results_frame)
        self.scrollbar.pack(side="right", fill="y")
        self.results_text.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.results_text.yview)

        # Create a frame to hold the copy button below results_frame
        copy_button_frame = tk.Frame(self)
        copy_button_frame.pack(fill="x")

        # Copy button
        copy_button = ttk.Button(
            copy_button_frame,
            text="Copy to Clipboard",
            command=self.copy_to_clipboard
        )
        self.copy_button = copy_button
        self.copy_button.config(state="disabled")
        copy_button.pack(pady=10)

        # Label for copy and reset status messages
        self.copy_reset_message_label = tk.Label(
            copy_button_frame, text="")
        self.copy_reset_message_label.pack()

        # Reset button
        reset_button = ttk.Button(
            copy_button_frame,
            text="Reset",
            command=self.reset_state
        )
        self.reset_button = reset_button
        reset_button.pack(pady=10)

    def generate_names(self):
        """Generate names based on selected options and display in text box"""
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
        self.results_text.config(state="normal")
        self.results_text.delete("1.0", tk.END)
        self.results_text.insert(tk.END, "\n".join(results))
        self.results_text.config(state="disabled")
        self.update_copy_button()

    def on_locale_select(self, event=None):
        """Handle locale selection from dropdown"""
        # Get the selected display value
        selected_display = self.locale_var.get()

        for key, value in LOCALE_MAPPING_NAME.items():
            if value == selected_display:
                self.current_locale_key = key
                break

    def copy_to_clipboard(self):
        """Copy generated names to clipboard"""
        names = self.results_text.get(1.0, tk.END).strip()
        if names:
            self.clipboard_clear()
            self.clipboard_append(names)

            # Count lines in the text
            line_count = self.results_text.index('end-1c').split('.')[0]
            message = f"{line_count} name(s) copied to clipboard!"
            self.show_copy_reset_message(message)

    def show_entry_count_message(self, message, color="red"):
        """Display a temporary entry count message with automatic fade-out"""
        self.entry_count_label.config(text=message, fg=color)
        self.entry_count_label.after(
            2000, self.hide_entry_count_message)

    def hide_entry_count_message(self):
        """Clear the entry count message from the UI"""
        self.entry_count_label.config(text="")

    def show_copy_reset_message(self, message, color="green"):
        """Display a temporary message about copy/reset actions with automatic fade-out"""
        self.copy_reset_message_label.config(text=message, fg=color)
        self.copy_reset_message_label.after(
            2000, self.hide_copy_reset_message)

    def hide_copy_reset_message(self):
        """Clear the reset confirmation message from the UI"""
        self.copy_reset_message_label.config(text="")

    def update_copy_button(self):
        """Enable or disable copy button based on results text"""
        results_text = self.results_text.get("1.0", tk.END)
        if results_text.strip() == "":
            # Disable copy button if results text is empty
            self.copy_button.config(state="disabled")
        else:
            # Enable copy button if results text is not empty
            self.copy_button.config(state="normal")

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
