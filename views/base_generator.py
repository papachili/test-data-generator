import tkinter as tk
from tkinter import ttk


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
        # Generate button
        self.add_generate_button(command=None)
        # Results area
        self.add_results_area("Results")
        # Copy button and message label
        self.add_copy_button()
        self.add_copy_reset_message_label()
        # Reset button
        self.add_reset_button()

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
        self.options_frame.pack(fill="x", pady=(0, 20))

    def add_locale_option(self, default_locale_key=None, locale_mapping_dict=None, label_text="Region/Language"):
        """Add a locale selection option to the options frame."""
        tk.Label(self.options_frame, text=label_text).grid(
            row=0, column=0, padx=5, pady=5, sticky="w")

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
        self.locale_combo.grid(row=0, column=1, padx=5, sticky="w")
        self.locale_combo.bind("<<ComboboxSelected>>", self.on_locale_select)

    def on_locale_select(self, event=None):
        """Handle locale selection from dropdown"""
        # Get the selected display value
        selected_display = self.locale_var.get()

        for key, value in self.locale_mapping_dict.items():
            if value == selected_display:
                self.current_locale_key = key
                break
        print(f"Selected locale key: {self.current_locale_key}")

    def add_generate_button(self, text="Generate", command=None):
        """Add a generate button to the content frame."""
        self.generate_button = ttk.Button(
            self.content_frame,
            text=text,
            command=command,
            width=20
        )
        self.generate_button.pack(pady=(0, 20))

    def add_results_area(self, title="Results"):
        """Add a results area to the content frame."""
        # Results area
        self.results_frame = tk.LabelFrame(
            self.content_frame, text=title, padx=10, pady=10)
        self.results_frame.pack(expand=True, fill="both")

        # Text widget for displaying results
        self.results_text = tk.Text(self.results_frame, height=10, width=40)
        self.results_text.pack(side="left", expand=True, fill="both")
        self.results_text.insert(
            tk.END, "Generated data will appear here...\n")
        self.results_text.config(state="disabled")
        self.scrollbar = tk.Scrollbar(self.results_frame)
        self.scrollbar.pack(side="right", fill="y")
        self.results_text.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.results_text.yview)

    def add_copy_button(self):
        """Add a copy to clipboard button below the results area."""
        self.copy_button_frame = tk.Frame(self.content_frame)
        self.copy_button_frame.pack(pady=10)

        self.copy_button = ttk.Button(
            self.copy_button_frame,
            text="Copy to Clipboard",
            command=self.copy_to_clipboard
        )
        self.copy_button.pack(pady=10)

    def add_copy_reset_message_label(self):
        """Add a label for copy and reset status messages."""
        # Label for copy and reset status messages
        self.copy_reset_message_label = tk.Label(
            self.copy_button_frame, text="")
        self.copy_reset_message_label.pack()

    def copy_to_clipboard(self):
        """Copy generated content to clipboard"""
        content = self.results_text.get(1.0, tk.END).strip()
        if content:
            self.clipboard_clear()
            self.clipboard_append(content)

            # Count lines in the text
            line_count = self.results_text.index('end-1c').split('.')[0]
            message = f"{line_count} item(s) copied to clipboard!"
            self.show_fading_message(self.copy_reset_message_label, message)

    def add_reset_button(self):
        """Add a reset button to the copy button frame."""
        self.reset_button = ttk.Button(
            self.copy_button_frame,
            text="Reset",
            command=self.reset_options
        )
        self.reset_button.pack(pady=10)

    def reset_options(self):
        """Reset view to initial state"""
        self.show_fading_message(
            self.copy_reset_message_label, "Options reset!", color="red")
        self.results_text.config(state="normal")
        self.results_text.delete("1.0", tk.END)
        self.results_text.insert(
            tk.END, "Generated data will appear here...\n")
        self.results_text.config(state="disabled")
        self.copy_button.config(state="disabled")

    def show_fading_message(self, label, message, color="green", duration=2000):
        """Display a temporary message on a specific label with automatic fade-out"""
        label.config(text=message, fg=color)
        label.after(duration, lambda: label.config(text=""))
