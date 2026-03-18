import random
import json
from pathlib import Path
from datetime import datetime
import tkinter as tk
from tkinter import messagebox, scrolledtext

# Data
subjects = [
    "Local man",
    "A confused cat",
    "Government official",
    "Alien from Mars",
    "Sleep-deprived student"
]

actions = [
    "accidentally invents",
    "bans",
    "declares war on",
    "falls in love with",
    "starts a protest against"
]

objects = [
    "his own shadow",
    "a sandwich",
    "WiFi signals",
    "Monday mornings",
    "invisible chairs"
]

endings = [
    "Experts are shocked.",
    "Internet reacts wildly.",
    "No one knows why.",
    "This is getting out of hand.",
    "Scientists demand answers."
]

database = 'news.json'

# Load data
if Path(database).exists():
    try:
        with open(database, 'r') as fs:
            data = json.load(fs)
    except json.JSONDecodeError:
        data = []
else:
    data = []


def update():
    """Save current data to JSON file."""
    with open(database, 'w') as fs:
        json.dump(data, fs, indent=4)


def fake_news():
    return f"{random.choice(subjects)} {random.choice(actions)} {random.choice(objects)}. {random.choice(endings)}"


# GUI Functions
def generate_news():
    try:
        n = int(entry.get())
        if n <= 0:
            messagebox.showwarning("Invalid", "Enter a positive number!")
            return
    except ValueError:
        messagebox.showwarning("Invalid", "Enter a valid number!")
        return

    output_box.delete(1.0, tk.END)

    count = 0
    attempts = 0

    while count < n and attempts < n * 3:
        news = fake_news()
        attempts += 1

        existing = [item["headline"] if isinstance(item, dict) else item for item in data]

        if news not in existing:
            output_box.insert(tk.END, f"{count+1}. {news}\n\n")

            data.append({
                "headline": news,
                "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            })

            count += 1

    update()

    if count < n:
        output_box.insert(tk.END, "\n(Some duplicates skipped)\n")

    # Reset input to 0 and focus
    entry.delete(0, tk.END)
    entry.insert(0, "0")
    entry.focus_set()


def view_saved():
    """Display saved headlines in the output box."""
    output_box.delete(1.0, tk.END)

    if not data:
        output_box.insert(tk.END, "No saved headlines yet.")
        return

    for i, item in enumerate(data, 1):
        if isinstance(item, dict):
            output_box.insert(
                tk.END,
                f"{i}. {item['headline']} ({item['created_at']})\n\n"
            )
        else:
            output_box.insert(tk.END, f"{i}. {item}\n\n")


def delete_history():
    """Delete all saved headlines after confirmation."""
    if messagebox.askyesno("Confirm Delete", "Are you sure you want to delete all saved headlines?"):
        global data
        data = []
        update()
        output_box.delete(1.0, tk.END)
        messagebox.showinfo("Deleted", "All saved headlines have been deleted.")


# GUI Setup
root = tk.Tk()
root.title("📰 Fake News Generator v4")
root.geometry("600x550")

# Input
frame = tk.Frame(root)
frame.pack(pady=10)

tk.Label(frame, text="Number of headlines: ").pack(side=tk.LEFT)

entry = tk.Entry(frame, width=5)
entry.pack(side=tk.LEFT, padx=5)
entry.insert(0, "0")  # Default value

# Buttons
btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Generate", command=generate_news).pack(side=tk.LEFT, padx=5)
tk.Button(btn_frame, text="View Saved", command=view_saved).pack(side=tk.LEFT, padx=5)
tk.Button(btn_frame, text="Delete History", command=delete_history).pack(side=tk.LEFT, padx=5)

# Output box
output_box = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=70, height=25)
output_box.pack(padx=10, pady=10)

# Auto-focus input at start
entry.focus_set()

# Run app
root.mainloop()