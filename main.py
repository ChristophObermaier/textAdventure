import tkinter as tk
from tkinter import messagebox

# Datastructure for rooms and connections
adventure_map = {
    "Start": {
        "description": "Du bist ein Abenteurer auf der Suche nach dem Schatz im Schwarzen Schloss. Du stehst vor dem Eingang zum Schlosshof.",
        "options": {"Norden": "Schlosshof", "Osten": "Wald", "Süden": "See", "Westen": "Pfad"}
    },
    "Schlosshof":{
        "description": "Du stehst im Schlosshof. Vor dir siehst du das Schwarze Schloss. Du hörst das Knarren von Holz und das Quietschen von Metall.",
        "options": {"Süden": "Start", "Osten": "Schlosstor"}
    },
    "Schlosstor":{
        "description": "Du stehst vor dem Schlosstor. Es ist verschlossen.",
        "options": {"Westen": "Schlosshof"}
    },
    "Wald": {
        "description": "Du stehst im Wald. Es ist dunkel und unheimlich.",
        "options": {"Westen": "Start"}
    },
    "See": {
        "description": "Du stehst am Ufer des Sees. Das Wasser ist klar und kalt.",
        "options": {"Norden": "Start"}
    },
    "Pfad": {
        "description": "Du stehst auf einem dunklen Pfad. Er führt in den Wald.",
        "options": {"Osten": "Start"}
    },
}

# Game State
current_location = "Start"
inventory = []

# Functions
def update_story():
    """Update the story text"""
    description = adventure_map[current_location]["description"]
    options = "\n".join([f"- {direction}" for direction in adventure_map[current_location]["options"]])
    story_text.set(f"{description}\n\nGehe nach:\n{options}")

def move(direction):
    """Moves the player in the given direction, if possible"""
    global current_location
    if direction in adventure_map[current_location]["options"]:
        current_location = adventure_map[current_location]["options"][direction]
        update_story()
    else:
        messagebox.showwarning("Ungültige Aktion", f"Du kannst nicht nach {direction} gehen.")

def submit_command():
    """Handles user input"""
    command = input_field.get().strip().lower()
    input_field.delete(0, tk.END) # Clear the input field
    if command in ["norden", "osten", "süden", "westen"]:
        move(command.capitalize())
    else:
        messagebox.showwarning("Hinweis", "Bitte gib eine Richtung ein (z.B. Norden, Osten, Süden, Westen).")

# GUI
root = tk.Tk()
root.title("Abenteuer im Schwarzen Schloss")

# Story
story_text = tk.StringVar()
story_label = tk.Label(root, textvariable=story_text, wraplength=400, justify="left")
story_label.pack(padx=10, pady=10)

# Input
input_field = tk.Entry(root, width=50)
input_field.pack(padx=10, pady=5)

submit_button = tk.Button(root, text="Befehl senden", command=submit_command)
submit_button.pack(pady=5)

# Initialize the Story
update_story()

root.mainloop()
