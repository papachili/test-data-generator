import tkinter as tk
from tkinter import ttk, messagebox
from utils import generate_random_name

MAX_PEOPLE = 9999  # maximum number of people to generate


def generate_names():
    try:
        count = int(entry_count.get())
        if count > MAX_PEOPLE:
            messagebox.showwarning(
                "Warning",
                f"Number exceeds the maximum allowed ({MAX_PEOPLE}). Setting to maximum."
            )
            count = MAX_PEOPLE
            entry_count.delete(0, tk.END)
            entry_count.insert(0, str(MAX_PEOPLE))
            return
        elif count <= 0:
            messagebox.showerror(
                "Error",
                "Please enter a positive number."
            )
            return
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")
        entry_count.delete(0, tk.END)
        entry_count.insert(0, "1")
        return

    action = action_var.get()
    gender = gender_var.get()

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
    output_text.config(state="normal")
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, "\n".join(results))
    output_text.config(state="disabled")
    update_copy_button()


# Copy button functionality
def copy_text():
    app.clipboard_clear()
    app.clipboard_append(output_text.get("1.0", tk.END))
    tk.messagebox.showinfo("Copied!", "Text copied to clipboard.")


# Function to update the copy button's state
def update_copy_button():
    if output_text.get("1.0", tk.END) == "\n":
        copy_button.config(state="disabled")
    else:
        copy_button.config(state="normal")
    # output_text.after(100, update_copy_button)


app = tk.Tk()
app.title("Test Data Generator")

# Action selection
ttk.Label(app, text="Select action:").grid(
    column=0, row=0, padx=5, pady=5, sticky="w")
action_var = tk.StringVar(value="Full Name")
actions = ["Full Name", "First Name", "Last Name"]
ttk.OptionMenu(app, action_var,
               actions[0], *actions).grid(column=1, row=0, padx=5, pady=5)

# Gender selection
ttk.Label(app, text="Select gender:").grid(
    column=0, row=1, padx=5, pady=5, sticky="w")
gender_var = tk.StringVar(value="non-binary")
genders = [("Male", "male"), ("Female", "female"),
           ("Non-binary", "non-binary"), ("Any", None)]
for i, (text, value) in enumerate(genders):
    ttk.Radiobutton(app, text=text, variable=gender_var, value=value).grid(
        column=1, row=1+i, padx=5, pady=2, sticky="w")

# Number of names
ttk.Label(app, text="Number of names:").grid(
    column=0, row=5, padx=5, pady=5, sticky="w")
entry_count = ttk.Entry(app)
entry_count.insert(0, "1")
entry_count.grid(column=1, row=5, padx=0, pady=5)

# Generate button
ttk.Button(app, text="Generate", command=generate_names).grid(
    column=0, row=6, columnspan=2, padx=5, pady=10)

# Output text box
output_text = tk.Text(app, height=10, width=40, state="disabled")
output_text.grid(column=0, row=7, columnspan=2, padx=5, pady=5)

# Copy button
copy_button = ttk.Button(app, text="Copy", command=copy_text)
copy_button.config(state="disabled")
copy_button.grid(column=0, row=8, columnspan=2, padx=5, pady=10)

app.mainloop()
