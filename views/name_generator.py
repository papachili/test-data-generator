import tkinter as tk
from tkinter import ttk, messagebox
from utils import generate_random_name


class NameGenerator(tk.Frame):
    """Name generator view"""
    MAX_PEOPLE = 9999  # maximum number of people to generate

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.parent = parent
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

        # Number of names
        tk.Label(self.options_frame, text="Number of names:").grid(
            row=2, column=0, sticky="w", padx=5, pady=5)
        self.entry_count = tk.IntVar(value=5)
        num_spinbox = ttk.Spinbox(
            self.options_frame, from_=1, to=self.MAX_PEOPLE, textvariable=self.entry_count, width=10)
        num_spinbox.grid(row=2, column=1, columnspan=3, sticky="w", padx=5)

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
        self.results_text.insert(tk.END, "Default text will appear here...\n")
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
        try:
            count = int(self.entry_count.get())
            if count > self.MAX_PEOPLE:
                messagebox.showwarning(
                    "Warning",
                    f"Number exceeds the maximum allowed ({self.MAX_PEOPLE}). Setting to maximum."
                )
                count = self.MAX_PEOPLE
                self.entry_count.set(0)
                self.entry_count.set(self.MAX_PEOPLE)
                return
            elif count <= 0:
                messagebox.showerror(
                    "Error",
                    "Please enter a positive number."
                )
                return
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number.")
            self.entry_count.set(0, tk.END)
            entry_count.set(0, "1")
            return

        action = self.action_var.get()
        gender = self.gender_var.get()
        print(f"gender: {gender}")

        results = []
        for _ in range(count):
            if action == "Full Name":
                name = generate_random_name(sex=gender)
            elif action == "First Name":
                name = generate_random_name(sex=gender).split()[0]
            elif action == "Last Name":
                name = generate_random_name(sex=gender).split()[-1]
            else:
                name = ""
            results.append(name)

        # Show results in the text box
        self.results_text.config(state="normal")
        self.results_text.delete("1.0", tk.END)
        self.results_text.insert(tk.END, "\n".join(results))
        self.results_text.config(state="disabled")
        self.update_copy_button()

    def copy_to_clipboard(self):
        """Copy generated names to clipboard"""
        names = self.results_text.get(1.0, tk.END).strip()
        if names:
            self.clipboard_clear()
            self.clipboard_append(names)
            self.copy_reset_message_label.config(
                text="Names copied to clipboard!", fg="green")
            self.copy_reset_message_label.after(
                2000, self.hide_copy_reset_message)  # hide after 2 seconds
        else:
            self.copy_reset_message_label.config(
                text="No names to copy. Generate some names first.", fg="red")
            self.copy_reset_message_label.after(
                3000, self.hide_copy_reset_message)  # hide after 3 seconds

    def hide_copy_reset_message(self):
        self.copy_reset_message_label.config(text="")

    # Function to update the copy button's state
    def update_copy_button(self):
        if self.results_text.get("1.0", tk.END) == "\n":
            self.copy_button.config(state="disabled")
        else:
            self.copy_button.config(state="normal")

    def reset_state(self):
        self.copy_reset_message_label.config(text="Options reset!", fg="red")
        self.copy_reset_message_label.after(
            2000, self.hide_copy_reset_message)  # hide after 2 seconds

        self.action_var.set("Full Name")
        self.gender_var.set("any")
        self.entry_count.set(5)
        self.results_text.config(state="normal")
        self.results_text.delete("1.0", tk.END)
        self.results_text.insert(tk.END, "Default text will appear here...\n")
        self.results_text.config(state="disabled")
        self.copy_button.config(state="disabled")
