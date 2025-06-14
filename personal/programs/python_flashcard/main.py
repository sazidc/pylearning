import tkinter as tk
import pandas as pd
from datetime import datetime, timedelta
import random
import os

# ---------------------------- CONSTANTS ------------------------------- #
BACKGROUND_COLOR = "#B1DDC6"
DATA_PATH = "data"
TERMS_TO_LEARN_FILE = f"{DATA_PATH}/terms_to_learn.csv"
ALL_TERMS_FILE = f"{DATA_PATH}/all_terms.csv"

# ---------------------------- GLOBALS --------------------------------- #
current_card = {}
to_learn = []
data = pd.DataFrame()
flip_timer = None

# ---------------------------- DATA HANDLING --------------------------- #
def load_data():
    global data, to_learn

    today = datetime.now().date()

    # Check if spaced repetition file exists and is not empty
    if os.path.exists(TERMS_TO_LEARN_FILE) and os.path.getsize(TERMS_TO_LEARN_FILE) > 0:
        data = pd.read_csv(TERMS_TO_LEARN_FILE)
        data["NextReview"] = pd.to_datetime(data["NextReview"]).dt.date

        # Cards due for review today or earlier
        due_cards = data[data["NextReview"] <= today]

        # Cards scheduled for future (new cards to introduce gradually)
        new_cards = data[data["NextReview"] > today]

        max_new_cards = 5  # limit new cards per session
        new_cards_to_add = new_cards.head(max_new_cards)

        session_cards = pd.concat([due_cards, new_cards_to_add])

        if session_cards.empty:
            print("🎉 No cards due or new cards to learn today! You can relax.")

        to_learn = session_cards.to_dict(orient="records")

    else:
        # Fallback: load all terms fresh and initialize spaced repetition fields
        print("⚠️ No spaced repetition file found or file empty. Loading all terms fresh.")
        original_data = pd.read_csv(ALL_TERMS_FILE)
        original_data["Repetition"] = 0
        original_data["Interval"] = 1
        original_data["EaseFactor"] = 2.5
        original_data["NextReview"] = today
        data = original_data
        to_learn = data.to_dict(orient="records")

    random.shuffle(to_learn)

# ---------------------------- SPACED REPETITION ----------------------- #
def update_sm2(card, quality):
    """
    SM-2 spaced repetition algorithm.
    quality: int (0-5), where 5 = perfect recall, 0 = complete blackout
    """
    ef = float(card["EaseFactor"])
    rep = int(card["Repetition"])
    interval = int(card["Interval"])

    if quality < 3:
        rep = 0
        interval = 1
    else:
        rep += 1
        if rep == 1:
            interval = 1
        elif rep == 2:
            interval = 6
        else:
            interval = round(interval * ef)
        ef = ef + (0.1 - (5 - quality) * (0.08 + (5 - quality) * 0.02))
        ef = max(1.3, ef)

    next_review_date = datetime.now().date() + timedelta(days=interval)
    return rep, interval, ef, next_review_date

# ---------------------------- UI FUNCTIONS ---------------------------- #
def next_card():
    global current_card, flip_timer
    if flip_timer:
        window.after_cancel(flip_timer)

    if not to_learn:
        canvas.itemconfig(card_title, text="No cards left!", fill="black")
        canvas.itemconfig(card_word, text="🎉 You have reviewed all cards for today.", fill="black")
        canvas.itemconfig(card_category, text="", fill="gray")
        canvas.itemconfig(card_background, image=card_front)
        return

    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="Term", fill="black")
    canvas.itemconfig(card_word, text=current_card["Term"], fill="black")
    canvas.itemconfig(card_word, text=current_card["Term"], fill="black", font=("Ariel", 60, "bold"), width=680)
    canvas.itemconfig(card_category, text=current_card.get("Category", ""), fill="gray")
    canvas.itemconfig(card_background, image=card_front)
    flip_timer = window.after(3000, flip_card)

def flip_card():
    canvas.itemconfig(card_title, text="Definition", fill="white")
    definition = current_card["Definition"]
    # Adjust font size based on length (example heuristic)
    if len(definition) > 100:
        font_size = 24
    elif len(definition) > 50:
        font_size = 30
    else:
        font_size = 40
    canvas.itemconfig(card_word, text=definition, fill="white", font=("Ariel", font_size, "bold"), width=680)
    canvas.itemconfig(card_category, text=current_card.get("Category", ""), fill="lightgray")
    canvas.itemconfig(card_background, image=card_back)  

def is_known():
    global current_card, data, to_learn

    quality = 5  # simulate perfect recall; you can add buttons for 0-5 later

    # Update spaced repetition values
    rep, interval, ef, next_review = update_sm2(current_card, quality)
    current_card["Repetition"] = rep
    current_card["Interval"] = interval
    current_card["EaseFactor"] = round(ef, 2)
    current_card["NextReview"] = next_review

    # Update the row in the DataFrame
    for i, card in data.iterrows():
        if card["Term"] == current_card["Term"]:
            data.at[i, "Repetition"] = current_card["Repetition"]
            data.at[i, "Interval"] = current_card["Interval"]
            data.at[i, "EaseFactor"] = current_card["EaseFactor"]
            data.at[i, "NextReview"] = current_card["NextReview"]
            break


    # Remove the card from to_learn so it won't show again this session
    to_learn[:] = [card for card in to_learn if card["Term"] != current_card["Term"]]

    # Save progress
    if not data.empty:
        data.to_csv(TERMS_TO_LEARN_FILE, index=False)

    next_card()

def is_unknown():
    # You can implement different logic for unknown cards if you want
    next_card()

# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Python Flashcards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card)

canvas = tk.Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = tk.PhotoImage(file="images/card_front.png")
card_back = tk.PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front)

card_title = canvas.create_text(400, 120, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"), width=680)
card_category = canvas.create_text(400, 40, text="", font=("Ariel", 24, "italic"))

canvas.grid(column=0, row=0, columnspan=2)

# Buttons
cross_image = tk.PhotoImage(file="images/wrong.png")
unknown_button = tk.Button(image=cross_image, highlightthickness=0, command=is_unknown)
unknown_button.grid(column=0, row=1)

check_image = tk.PhotoImage(file="images/right.png")
known_button = tk.Button(image=check_image, highlightthickness=0, command=is_known)
known_button.grid(column=1, row=1)

# ---------------------------- MAIN ------------------------------------ #
load_data()
next_card()
window.mainloop()
