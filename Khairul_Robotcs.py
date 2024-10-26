import tkinter as tk
from tkinter import font
from PIL import Image, ImageTk
import time
import threading
import random

# Load and configure the background image
def load_background(root, path):
    image = Image.open(path)
    image = image.resize((700, 600), Image.LANCZOS)  # Use LANCZOS for high-quality resize
    background_image = ImageTk.PhotoImage(image)
    background_label = tk.Label(root, image=background_image)
    background_label.image = background_image  # Keep a reference to avoid garbage collection
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Animation and display functions
def animate_cake(label):
    cake = [
        "          i i i i i i i          ",
        "        |   |   |   |   |        ",
        "        |   |   |   |   |        ",
        "     __|___|___|___|___|__       ",
        "     |                 🎂 |      ",
        "     |  Happy 3rd Year, HWS! |   ",
        "     |       Robotics Club     | ",
        "     |_________________________|  "
    ]
    for i, layer in enumerate(cake):
        label.config(text=layer, fg="orange", bg="#f0f0f0")
        time.sleep(0.5)

def display_message(label, messages, delay=2):
    for message in messages:
        label.config(text=message)
        time.sleep(delay)

def display_names_with_sparkles(label, names, delay=1):
    for name in names:
        sparkles = random.choice(["✨", "💖", "🎈", "🎉", "🥳"])  # Choose a random sparkle
        label.config(text=f"{sparkles} {name.title()} {sparkles}", fg="green")
        time.sleep(delay)

def show_final_thank_you(label):
    thank_you_message = "✨✨ THANK YOU! ✨✨"
    label.config(text=thank_you_message, fg="purple", font=("Helvetica", 20, "bold"))
    time.sleep(3)  # Show for a few seconds before ending

def start_celebration():
    threading.Thread(target=run_celebration_program).start()

def run_celebration_program():
    # Title & Introduction
    title_message = [
        "The Hobart and William Smith Robotics Club is celebrating its 3rd year!",
        "This year, we’re commemorating our journey with a fantastic community of members."
    ]
    display_message(message_label, title_message, delay=3)

    # Thanking Faculty Sponsors with sparkles and green color
    faculty_thanks = [
        "Chris Fietkiewicz - Advisor",
        "Hanqing Hu - Mentor",
        "Ileana Dumitriu - Mentor"
    ]
    display_names_with_sparkles(message_label, faculty_thanks, delay=2)

    # Thanking Members (Past and Present)
    members_thanks = ["To our current and previous members, thank you!"]
    display_message(message_label, members_thanks, delay=2)

    # Displaying Members Names with Sparkles
    members_list = [
    "Caroline Kamal", "Khairul Islam", "Yutong Wang", "Vuthy Vey", "Souvick Rodrigues", 
    "Richard Centeno", "Ali", "Trang Linh", "Esme", "Alberto", "Sasha", "Riku", "David",
    "Velocity", "Ryan", "Aaron Tober", "Elvis Njomo", "Zurick Miranda", "Biruk Nardos",
    "John Reyes", "Emmanuel Appiah", "Umama", "Stromberg, Stephen", "Condon, Parker",
    "Carter Morgan", "Garcia, Jonathan", "Oxanya Mackay", "Tara Nickerson", "Sayf Elhawary",
    "Atumonyogo, Jamachukwun", "Johnson, Lucas", "Smith, Victoria", "Mucheru, Sean",
    "Hassini, Anis", "Raicevic, Anastasia", "Malhotra, Tarang", "Jaheim Pierre",
    "Eiler Byberi", "Peace Kiponda", "David Wynne", "David Garvey", 
    "Flavia Arganini Frescobaldi", "Mark Mulflur", "Derrielle Faulkner", "Daud",
    "Debray, Pierre-Olivier", "Maria Galarza", "Zhengrui Wei", "Javier Pacheco",
    "Riley Mccabe", "Elizabeth Martzloff", "Holden May", "Luke Ryan", 
    "Vallabhajosula, Rahul", "Albert Levy", "Javier", "Emmanuel", "Christopher Robles",
    "Namir Dobbs", "Hannah Baker", "Grace Kongoy", "Emine Ozturk", "Leo Bonacci",
    "Eagle Qiu", "Gianluca Loporto", "Leo Arbitman", "Holden May", "Rafael A", "Nadir Khan",
    "Christina Mohonta", "Eiler Byberi", "Aiden Stinebower", "Mal Gjerqeku", 
    "Joy Nguyen", "Autumn Washington", "Najma Ahmed", "Esme Pham", "Clyde Williams",
    "Fairooj Rushmila Suhita", "Reece Wilson", "Alexander Maccluskey", "Zac Chamish",
    "Aliou Sangare", "Tate Tower", "Randy Hong", "Berke Otus", "Evan Nolan",
    "Daniel Adelman", "Clara Adamson", "Anik Biswas", "Vanessa Castillo", "Ryan Easton",
    "Connor Elliott", "Evan Fisher", "Nathan Flores", "Noelle Friel", "Jonathan Holmes",
    "Ethan Huyuk", "Ryan Jackson", "Harrison Keena", "Bryce Keith", "Duncan Kipkoech",
    "Sam Lueck", "Tommy Major", "AJ Mesmer", "Endry Paulino Lora", "Kevin Zou"
]
    display_names_with_sparkles(message_label, members_list, delay=1)

    # Final Thank You Message
    show_final_thank_you(message_label)

    # Final Cake Animation
    animate_cake(cake_label)

# Create the main window
root = tk.Tk()
root.title("HWS Robotics Club - 3rd Year Celebration!")
root.geometry("700x600")  # Adjusted window size for background

# Load the background image
load_background(root, "C:/Users/khair/OneDrive/Documents/GUI Birthday Wish/facility.jpg")

# Set fonts
title_font = font.Font(family="Helvetica", size=20, weight="bold")
message_font = font.Font(family="Helvetica", size=16)
cake_font = font.Font(family="Helvetica", size=14)

# Create the title label with shadow effect
title_label = tk.Label(root, text="🎈 🎉🎈 HWS Robotics Club - 3rd Year Celebration 🎈 🎉 🎈", font=title_font, fg="purple", bg="#f0f0f0")
title_label.place(relx=0.5, y=30, anchor="center")

# Create a label to show cake animation
cake_label = tk.Label(root, font=cake_font, fg="orange", bg="#f0f0f0")
cake_label.place(relx=0.5, y=120, anchor="center")

# Create a label to display messages with an initial blank text
message_label = tk.Label(root, text="", font=message_font, fg="cyan", bg="#f0f0f0", wraplength=650)
message_label.place(relx=0.5, y=300, anchor="center")

# Start button with styling
start_button = tk.Button(root, text="Start Celebration", font=message_font, bg="light blue", fg="white", command=start_celebration)
start_button.place(relx=0.5, y=550, anchor="center")

# Start the GUI event loop
root.mainloop()
