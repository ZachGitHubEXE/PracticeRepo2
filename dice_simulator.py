import tkinter as tk
from tkinter import messagebox
import random


def roll_dice(dice_type, count):
    """Rolls a given number of a specific dice type."""
    return [random.randint(1, dice_type) for _ in range(count)]


def roll_selected_dice():
    """Rolls all selected dice and displays the results."""
    try:
        # Get values from entry fields
        d20_count = int(d20_entry.get()) if d20_entry.get().isdigit() else 0
        d12_count = int(d12_entry.get()) if d12_entry.get().isdigit() else 0
        d10_count = int(d10_entry.get()) if d10_entry.get().isdigit() else 0
        d8_count = int(d8_entry.get()) if d8_entry.get().isdigit() else 0
        d6_count = int(d6_entry.get()) if d6_entry.get().isdigit() else 0
        d4_count = int(d4_entry.get()) if d4_entry.get().isdigit() else 0
        d2_count = int(d2_entry.get()) if d2_entry.get().isdigit() else 0

        # Roll dice
        results = {
            "d20": roll_dice(20, d20_count),
            "d12": roll_dice(12, d12_count),
            "d10": roll_dice(10, d10_count),
            "d8": roll_dice(8, d8_count),
            "d6": roll_dice(6, d6_count),
            "d4": roll_dice(4, d4_count),
            "d2": roll_dice(2, d2_count),
        }

        # Prepare results text
        result_text = ""
        for dice, rolls in results.items():
            if rolls:
                result_text += f"{dice}: {', '.join(map(str, rolls))} (Total: {sum(rolls)})\n"

        if result_text:
            messagebox.showinfo("Roll Results", result_text)
        else:
            messagebox.showwarning("No Rolls", "You didn't select any dice to roll!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")


# Set up the GUI
root = tk.Tk()
root.title("Dice Rolling Simulator")

# Create labels and entry fields for each dice type
dice_types = [
    ("d20", 20),
    ("d12", 12),
    ("d10", 10),
    ("d8", 8),
    ("d6", 6),
    ("d4", 4),
    ("d2", 2),
]

entries = {}

for i, (dice, sides) in enumerate(dice_types):
    label = tk.Label(root, text=f"Number of {dice} to roll:")
    label.grid(row=i, column=0, padx=10, pady=5)
    entry = tk.Entry(root, width=5)
    entry.grid(row=i, column=1, padx=10, pady=5)
    entries[dice] = entry

# Access the entries for each dice type
d20_entry = entries["d20"]
d12_entry = entries["d12"]
d10_entry = entries["d10"]
d8_entry = entries["d8"]
d6_entry = entries["d6"]
d4_entry = entries["d4"]
d2_entry = entries["d2"]

# Add a roll button
roll_button = tk.Button(root, text="Roll Dice", command=roll_selected_dice, font=("Arial", 14))
roll_button.grid(row=len(dice_types), column=0, columnspan=2, pady=20)

# Start the application
root.mainloop()
