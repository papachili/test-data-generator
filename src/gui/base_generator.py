import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from data_generator import MAX_AMOUNT
import json
import os


class BaseView(tk.Frame):
    """Base view class with common functionality."""

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.create_widgets()

    def create_widgets(self):
        """Override this method in child classes to create specific widgets"""
        # Header
        self.add_header_frame()
        # Back button
        self.add_back_button()
        # Title
        self.add_title_label("Base View")
        # Main content
        self.add_main_content()
        # Options frame
        self.add_options_frame()
        # Status message label
        self.add_status_message()
        # Create frame for Generate buttons
        self.button_frame = tk.Frame(self.content_frame)
        self.button_frame.pack(fill="x")
        # Generate button
        self.add_generate_button(
            frame=self.button_frame, command=None, row=0, column=1)
        # Results area
        self.add_results_area("Results")
        # Create frame for bottom buttons
        self.button_frame = tk.Frame(self.content_frame)
        self.button_frame.pack(fill="x")
        # Save as JSON button
        self.add_save_json_button(frame=self.button_frame, row=0, column=0)
        # Save as CSV button
        self.add_save_csv_button(frame=self.button_frame, row=0, column=1)
        # Copy to clipboar button
        self.add_copy_button(frame=self.button_frame, row=0, column=2)
        # Reset button
        self.add_reset_button(frame=self.button_frame, row=1, column=1)

        # Configure the bottom buttons frame to expand
        self.button_frame.grid_columnconfigure(0, weight=2)
        self.button_frame.grid_columnconfigure(1, weight=1)
        self.button_frame.grid_columnconfigure(2, weight=1)
        self.button_frame.grid_columnconfigure(3, weight=0)

    def add_header_frame(self):
        """Add header frame to the view."""
        self.header_frame = tk.Frame(self)
        self.header_frame.pack(fill="x", padx=20, pady=10)

    def add_back_button(self):
        """Add a back button to the header frame."""
        self.back_button = ttk.Button(
            self.header_frame,
            text="← Back",
            command=lambda: self.controller.show_frame('MainMenu')
        )
        self.back_button.pack(side="left")

    def add_title_label(self, text):
        """Add a title label to the header frame."""
        self.title_label = tk.Label(
            self.header_frame,
            text=text,
            font=("Arial", 16, "bold")
        )
        self.title_label.pack(side="left", padx=20)

    def add_main_content(self):
        """Add main content frame to the view."""
        self.content_frame = tk.Frame(self)
        self.content_frame.pack(expand=True, fill="both", padx=40, pady=20)

    def add_options_frame(self):
        """Add options frame to the view."""
        self.options_frame = tk.LabelFrame(
            self.content_frame, text="Options", padx=10, pady=10)
        self.options_frame.pack(fill="x", pady=0)

    def add_actions_frame(self, text="Select action:", actions_list=None, command=None, row=0, column=0):
        """Add actions frame to the view."""
        self.actions_frame = tk.Frame(self.content_frame)
        self.actions_frame.pack(fill="x", pady=(0, 20))

        # Action selection
        tk.Label(self.options_frame, text=text).grid(
            row=row, column=column, padx=5, pady=5, sticky="w")
        self.action_var = tk.StringVar(
            value=actions_list[0] if actions_list else "")
        self.option_menu = ttk.OptionMenu(self.options_frame, self.action_var,
                                          actions_list[0], *actions_list, command=command)
        self.option_menu.grid(row=row, column=column+1, padx=5, sticky="w")

    def add_locale_option(self, default_locale_key=None, locale_mapping_dict=None, label_text="Region/Language", row=0, column=0):
        """Add a locale selection option to the options frame."""
        tk.Label(self.options_frame, text=label_text).grid(
            row=row, column=column, padx=5, pady=5, sticky="w")

        self.locale_var = tk.StringVar(value=default_locale_key)
        self.locale_mapping_dict = locale_mapping_dict or {}

        self.locale_combo = ttk.Combobox(
            self.options_frame,
            textvariable=self.locale_var,
            values=list(locale_mapping_dict.values()
                        ) if locale_mapping_dict else [],
            state="readonly",
            width=25
        )
        self.locale_combo.grid(row=row, column=column+1, padx=5, sticky="w")
        self.locale_combo.bind("<<ComboboxSelected>>", self.on_locale_select)

    def on_locale_select(self, event=None):
        """Handle locale selection from dropdown"""
        # Get the selected display value
        selected_display = self.locale_var.get()

        for key, value in self.locale_mapping_dict.items():
            if value == selected_display:
                self.current_locale_key = key
                break

    def add_amount_option_spinbox(self, default_value=5, label_text="Amount:", row=0, column=0):
        """Add an amount selection spinbox to the options frame."""
        tk.Label(self.options_frame, text=label_text).grid(
            row=row, column=column, padx=5, pady=5, sticky="w")
        self.entry_count = tk.IntVar(value=default_value)
        num_spinbox = ttk.Spinbox(
            self.options_frame,
            from_=1,
            to=MAX_AMOUNT,
            textvariable=self.entry_count,
            width=10
        )
        num_spinbox.grid(row=row, column=column+1, padx=5, sticky="w")

    def add_status_message(self):
        # Label for entry_count status messages
        self.status_message_label = tk.Label(
            self.content_frame, text="")
        self.status_message_label.pack()

    def add_generate_button(self, frame=None, text="Generate", command=None, row=0, column=0):
        """Add a generate button to the content frame."""
        if frame is None:
            frame = self.content_frame
        self.generate_button = ttk.Button(
            frame,
            text=text,
            command=command,
        )
        # self.generate_button.pack(pady=(0, 20))
        self.generate_button.grid(
            row=row, column=column, pady=(0, 10), padx=130, sticky="ew")
        self.button_frame.grid_columnconfigure(0, weight=1)
        self.button_frame.grid_columnconfigure(1, weight=2)
        self.button_frame.grid_columnconfigure(2, weight=1)
        self.button_frame.grid_columnconfigure(3, weight=0)

    def validate_entry_count(self):
        try:
            count = int(self.entry_count.get())
            if count > MAX_AMOUNT:
                message = f"Number exceeds the maximum allowed ({MAX_AMOUNT}). Setting to maximum."
                self.show_fading_message(
                    self.status_message_label, message, "red")
                self.entry_count.set(MAX_AMOUNT)
            elif count <= 0:
                message = f"Please enter a positive number between 1 and {MAX_AMOUNT}"
                self.show_fading_message(
                    self.status_message_label, message, "red")
                self.entry_count.set(5)
            else:
                return count
        except Exception as e:
            message = "Please enter a valid integer."
            self.show_fading_message(self.status_message_label, message, "red")
            self.entry_count.set(5)

    def add_results_area(self, title="Results", pady=0):
        """Add a results area to the content frame."""
        # Results area
        self.results_frame = tk.LabelFrame(
            self.content_frame, text=title, padx=10, pady=10)
        self.results_frame.pack(expand=True, fill="both", pady=pady)

        # Text widget for displaying results
        self.results_text = tk.Text(self.results_frame, height=15, width=40)
        self.results_text.pack(side="left", expand=True, fill="both")
        self.results_text.insert(
            tk.END, "Generated data will appear here...\n")
        self.results_text.config(state="disabled")
        self.scrollbar = tk.Scrollbar(self.results_frame)
        self.scrollbar.pack(side="right", fill="y")
        self.results_text.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.results_text.yview)

    def add_copy_button(self, frame=None, row=0, column=0):
        """Add a copy to clipboard button below the results area."""
        if frame is None:
            frame = self.content_frame
        self.copy_button = ttk.Button(
            frame,
            text="Copy to Clipboard",
            command=self.copy_to_clipboard
        )
        self.copy_button.config(state="disabled")
        self.copy_button.grid(row=row, column=column, pady=10, sticky="ew")

    def add_save_json_button(self, frame=None, row=0, column=0):
        """Add a Save as JSON button below the results area."""
        if frame is None:
            frame = self.content_frame
        self.save_json_button = ttk.Button(
            frame,
            text="Save as JSON",
            command=self.save_to_json
        )
        self.save_json_button.config(state="disabled")
        self.save_json_button.grid(
            row=row, column=column, pady=10, sticky="ew")

    def add_save_csv_button(self, frame=None, row=0, column=0):
        """Add a Save as CSV button below the results area."""
        if frame is None:
            frame = self.content_frame
        self.save_csv_button = ttk.Button(
            frame,
            text="Save as CSV",
            command=self.save_to_csv
        )
        self.save_csv_button.config(state="disabled")
        self.save_csv_button.grid(
            row=row, column=column, pady=10, sticky="ew")

    def update_copy_button(self):
        """Enable or disable copy button based on results text"""
        results_text = self.results_text.get("1.0", tk.END)
        if results_text.strip() == "":
            # Disable copy button if results text is empty
            self.copy_button.config(state="disabled")
            self.save_json_button.config(state="disabled")
            self.save_csv_button.config(state="disabled")
        else:
            # Enable copy button if results text is not empty
            self.copy_button.config(state="normal")
            self.save_json_button.config(state="normal")
            self.save_csv_button.config(state="normal")

    def copy_to_clipboard(self):
        """Copy generated content to clipboard"""
        content = self.results_text.get(1.0, tk.END).strip()
        if content:
            self.clipboard_clear()
            self.clipboard_append(content)

            # Count lines in the text
            line_count = self.results_text.index('end-1c').split('.')[0]
            message = f"{line_count} item(s) copied to clipboard!"
            self.show_fading_message(self.status_message_label, message)

    def add_reset_button(self, frame=None, row=0, column=0):
        """Add a reset button to the copy button frame."""
        if frame is None:
            frame = self.content_frame
        self.reset_button = ttk.Button(
            frame,
            text="Reset",
            command=self.reset_options
        )
        self.reset_button.grid(row=row, column=column, pady=10, sticky="nsew")

    def display_results(self, results):
        """Display generated results in the results text area."""
        self.results_text.config(state="normal")
        self.results_text.delete("1.0", tk.END)
        self.results_text.insert(tk.END, "\n".join(results))
        self.results_text.config(state="disabled")
        self.update_copy_button()

    def reset_options(self):
        """Reset view to initial state"""
        self.show_fading_message(
            self.status_message_label, "Options reset!", color="red")
        self.results_text.config(state="normal")
        self.results_text.delete("1.0", tk.END)
        self.results_text.insert(
            tk.END, "Generated data will appear here...\n")
        self.results_text.config(state="disabled")
        self.copy_button.config(state="disabled")
        self.save_json_button.config(state="disabled")
        self.save_csv_button.config(state="disabled")

    def show_fading_message(self, label, message, color="green", duration=2000):
        """Display a temporary message on a specific label with automatic fade-out"""
        label.config(text=message, fg=color)
        label.after(duration, lambda: label.config(text=""))

    def show_confirmation_dialog(self, title, message):
        """Show a confirmation dialog with a title and message."""
        response = messagebox.askyesno(
            title, f"{message} Do you want to overwrite the file?"
        )
        return response

    def save_to_json(self):
        """
        Save Results text box content to "data.json" file.

        """
        file_path = "data.json"
        self.save_file(file_path, file_format="json")

    def save_to_csv(self):
        """
        Save Results text box content to "data.csv" file.

        """
        file_path = "data.csv"
        self.save_file(file_path, file_format="csv")

    def save_file(self, file_path, file_format="csv"):
        """
        Save the file to the specified path.
        """
        # Check if file already exists
        if os.path.exists(file_path):
            # Show confirmation dialog if file exists
            response = self.show_confirmation_dialog(
                "Overwrite existing file", "File already exists."
            )
            if not response:
                return  # Exit if user cancels

        # Get the content of the text area
        content = self.results_text.get(1.0, tk.END).strip()

        # Split the content into lines
        data = [line.strip().split(',') for line in content.splitlines()]

        # Save file based on format
        if file_format == "json":
            # Convert data to JSON string with indentation
            json_str = json.dumps(data, indent=4)
            with open(file_path, "w") as f:
                f.write(json_str)
        elif file_format == "csv":
            # Use csv module to write CSV file
            with open(file_path, 'w', newline='') as csvfile:
                for row in data:
                    csvfile.write(row[0] + ",\n")

        # Count lines in the text and show status message
        line_count = self.results_text.index('end-1c').split('.')[0]
        message = f"{line_count} item(s) saved to {file_path}!"
        self.show_fading_message(self.status_message_label, message)
