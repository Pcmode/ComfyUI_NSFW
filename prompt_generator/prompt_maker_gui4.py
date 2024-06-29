import tkinter as tk
from tkinter import ttk
import pandas as pd
import os

# Setup the main window
root = tk.Tk()
root.title("AI CSV Prompt Maker")

# Base prompt with placeholders for variable selections
base_prompt = ("lips, {}, {}, {}, full body shot, 4K resolution, {}, {}, cleavage, {}, {}, {}, {}, {}, {}, {}, ((masterpiece)), "
               "(best quality), nsfw, perfect anatomy (nude!!!!!), {}, {}, {}, posing {}, {}")

# Options for each variable with updated descriptions
variables = {
    "sex": ["Male", "Female"],
    "tattoo": ["tribal tattoo", "mondolla tattoo", "bunny tattoo"],
    "facing direction": ["looking at viewer", "looking at viewer over shoulder", "facing away from viewer", "looking up at the sky", "looking down at the ground", "looking to the right of viewer", "looking to the left of viewer", "laying on ground + facing up + looking at viewer"],
    "hair length": ["short hair", "medium length hair", "long hair"],
    "jewelry type": ["earrings", "necklace", "bracelets"],
    "mouth": ["mouth open", "mouth closed", "mouth smiling"],
    "emotion": ["happy", "sad", "angry", "playful", "funny", "sexy", "bashful"],
    "hair color": ["blonde hair", "brown hair", "black hair", "rainbow hair", "blue hair", "purple hair", "red hair", "green hair"],
    "breasts size": ["small breasts", "medium breasts", "large breasts"],
    "ass size": ["small ass", "medium ass", "large ass"],
    "location": ["at the beach", "in the studio", "urban", "in the jungle", "in the city", "forest", "desert", "ocean"],
    "race": ["Caucasian", "African", "Asian", "Hispanic", "Middle Eastern", "Brazilian", "British", "Czech", "Ebony", "French", "German", "Indian", "Latina", "Italian", "Japanese", "Korean", "Russian", "Swedish"],
    "eye color": ["blue eyes", "brown eyes", "amber eyes", "hazel eyes", "green eyes", "violet eyes", "purple eyes"],
    "eyewear": ["glasses", "none"],
    "outfit type": ["casual wear", "formal wear", "sport wear", "Navy hat", "Cheerleader outfit"],
    "pose": ["standing straight", "hands on hips", "sitting cross-legged", "sitting one leg up", "lying on back", "lying on stomach", "bent over", "kneeling", "legs spread"],
    "art style": ["(Painted in Monet style!!!!!)", "(Painted in Leonardo da Vinci style!!!!!)", "(Painted in Salvador Dali style!!!!!)", "(Painted in Vincent van Gogh style!!!!!)", "(Painted in Rembrandt style!!!!!)", "(Painted in Michelangelo style!!!!!)", "(Painted in Jackson Pollock!!!!!)", "(Painted in Andy Warhol style!!!!!)"]
}

# Dictionary to hold the state (enabled/disabled) of each variable
checkbox_states = {var: tk.IntVar(value=1) for var in variables}

# Function to generate the prompt
def generate_prompt():
    age = age_slider.get()
    selections = [dropdowns[var].get() if checkbox_states[var].get() else "{}" for var in variables]
    selections.append(str(age))  # Convert age to string and append
    prompt = base_prompt.format(*selections)
    
    # Check if the file exists and then decide whether to write header
    file_exists = os.path.isfile("prompts.csv")
    
    # Save to CSV
    df = pd.DataFrame([prompt], columns=["Prompt"])
    df.to_csv("prompts.csv", mode='a', header=not file_exists, index=False)
    result_label.config(text=f"Generated Prompt: {prompt}")

# Create dropdown menus and checkboxes for each variable
dropdowns = {}
for i, (var, options) in enumerate(variables.items()):
    tk.Label(root, text=var).grid(row=i, column=0, padx=10, pady=10)
    checkbox = tk.Checkbutton(root, text="Enable", variable=checkbox_states[var])
    checkbox.grid(row=i, column=2, padx=10, pady=10)
    dropdowns[var] = ttk.Combobox(root, values=options)
    dropdowns[var].grid(row=i, column=1, padx=10, pady=10)
    dropdowns[var].set(options[0])  # Set the default value

# Add age slider
tk.Label(root, text="Age").grid(row=len(variables), column=0, padx=10, pady=10)
age_slider = tk.Scale(root, from_=18, to=60, orient=tk.HORIZONTAL)
age_slider.grid(row=len(variables), column=1, padx=10, pady=10)

# Button to generate prompt
generate_button = tk.Button(root, text="Generate Prompt", command=generate_prompt)
generate_button.grid(row=len(variables) + 1, column=0, columnspan=3, pady=20)

# Label to display the generated prompt
result_label = tk.Label(root, text="")
result_label.grid(row=len(variables) + 2, column=0, columnspan=3)

root.mainloop()
