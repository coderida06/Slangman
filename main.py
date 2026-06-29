import tkinter as tk
import customtkinter as ctk
import random
import threading
import time

# ====================================
# THEME CONSTANTS
# ====================================

ctk.set_appearance_mode("dark")

BG         = "#0F172A"
CARD       = "#1E293B"
CARD_INNER = "#162032"
PURPLE     = "#8B5CF6"
PINK       = "#EC4899"
SUCCESS    = "#22C55E"
DANGER     = "#EF4444"
YELLOW     = "#FACC15"
TEXT       = "#F8FAFC"
MUTED      = "#64748B"
BORDER     = "#8B5CF6"

FONT_TITLE   = ("Arial Black", 36)
FONT_HANGMAN = ("Segoe UI Emoji", 52)
FONT_WORD    = ("Arial Black", 50)
FONT_LABEL   = ("Arial Black", 18)
FONT_BODY    = ("Arial", 15)
FONT_RESULT  = ("Arial Black", 22)
FONT_STREAK  = ("Arial Black", 16)

# ====================================
# WORD BANK & DEFINITIONS
# ====================================

WORDS = [
    "bet", "cap", "rizz", "sus", "bussin",
    "slay", "drip", "vibe", "lit", "fire",
    "goated", "mid", "lowkey", "fr", "bro",
    "bruh", "fam", "homie", "yeet", "flex",
    "stan", "simp", "ratio", "salty", "clout",
    "ghosted", "fumble", "cook", "cooked",
    "delulu", "based", "cringe", "ick", "shook",
    "tea", "spill", "ate", "mood", "wild",
    "extra", "basic", "boujee", "finna",
    "valid", "sigma", "alpha", "chad",
    "aura", "brainrot", "skibidi", "goofy"
]

DEFINITIONS = {
    "rizz":     "Natural charisma / game",
    "bet":      "Okay / for sure / agreed",
    "cap":      "A lie / fake claim",
    "sus":      "Suspicious / sketchy",
    "goated":   "Greatest Of All Time",
    "drip":     "Stylish / fresh fit",
    "vibe":     "Feeling or atmosphere",
    "fam":      "Close friends / squad",
    "homie":    "Close friend",
    "yeet":     "Throw with full force",
    "sigma":    "Independent lone-wolf type",
    "brainrot": "Mind corrupted by internet",
    "skibidi":  "Random unhinged meme term",
    "bussin":   "Really good / slaps hard",
    "slay":     "Absolutely killing it",
    "mid":      "Average / nothing special",
    "lowkey":   "Subtly / kinda sorta",
    "flex":     "Show off your wins",
    "stan":     "Obsessed super-fan",
    "simp":     "Someone who overpleases",
    "ratio":    "Replies > likes (L post)",
    "clout":    "Social media fame",
    "ghosted":  "Left on read / disappeared",
    "delulu":   "Delusional in a funny way",
    "based":    "Confident / unapologetically real",
    "cringe":   "Embarrassingly awkward",
    "shook":    "Shocked / mind blown",
    "tea":      "Gossip / the truth",
    "ate":      "Absolutely nailed it",
    "valid":    "Accepted / makes sense",
    "chad":     "Alpha confident person",
    "aura":     "Mysterious vibes / energy",
    "fumble":   "Mess up a great opportunity",
}

# ====================================
# REACTION MESSAGES
# ====================================

CORRECT_MSGS = [
    "🔥 Bro is cooking",
    "🗿 Let him cook",
    "📈 Aura increasing",
    "😎 W guess",
    "✨ Certified sigma move",
    "💯 Valid",
    "🚀 Rizz detected",
    "👑 Main character energy",
    "⚡ Locked in",
]

WRONG_MSGS = [
    "💀 Bro is cooked",
    "😭 Skill issue",
    "📉 Aura lost",
    "🤡 L guess",
    "🚨 Negative aura",
    "☠️ Catastrophic fumble",
    "🪦 Bro fell off",
    "📦 Pack it up",
    "🥀 Aura evaporated",
]

WIN_TITLES = [
    "🏆 MAXIMUM RIZZ ACHIEVED",
    "🗿 SIGMA DETECTED",
    "🔥 W PLAYER",
    "🚀 BRAINROT MASTER",
    "👑 KING OF RIZZ",
]

LOSE_TITLES = [
    "💀 Bro got cooked",
    "😭 Negative aura detected",
    "📉 Aura bankrupt",
    "🤡 Brainrot revoked",
    "☠️ Skill issue achieved",
]

WRONG_WINDOW_TITLES = {
    1: "🙂 Still Cooking",
    2: "😬 Slightly Cooked",
    3: "😭 Bro is Struggling",
    4: "💀 Bro is Cooked",
    5: "☠️ Extra Cooked",
    6: "🚨 NEGATIVE AURA DETECTED",
}

# ====================================
# HANGMAN CANVAS DRAWING
# ====================================

MAX_WRONG = 6

def draw_hangman(canvas, stage):
    """Draw stick-figure hangman on a tk Canvas. stage = 0..6."""
    canvas.delete("all")

    W, H   = 160, 180
    lw     = 3          
    col    = "#8B5CF6"  
    head_c = "#EC4899"  
    dead_c = "#EF4444"  
    dead   = (stage == MAX_WRONG)


    canvas.create_line(10, H - 10, W - 10, H - 10, width=lw, fill=col)
    
    canvas.create_line(40, H - 10, 40, 10,          width=lw, fill=col)
    
    canvas.create_line(40, 10,     120, 10,          width=lw, fill=col)
    
    canvas.create_line(120, 10,    120, 38,          width=lw, fill=col)

    if stage == 0:
        return


    hcol = dead_c if dead else head_c
    canvas.create_oval(108, 38, 132, 62, width=lw, outline=hcol)   

    if stage == 1:
        return

    
    canvas.create_line(120, 62, 120, 115, width=lw, fill=col)      

    if stage == 2:
        return

    
    canvas.create_line(120, 72, 98,  95,  width=lw, fill=col)       

    if stage == 3:
        return

  
    canvas.create_line(120, 72, 142, 95,  width=lw, fill=col)    

    if stage == 4:
        return

    # ── Left leg ─────────────────────────────────────────────────────────────
    canvas.create_line(120, 115, 100, 148, width=lw, fill=col)      # stage 5

    if stage == 5:
        return

    
    canvas.create_line(120, 115, 140, 148, width=lw, fill=col)      

    
    if dead:
        canvas.create_line(113, 44, 119, 50, width=2, fill=dead_c)
        canvas.create_line(119, 44, 113, 50, width=2, fill=dead_c)
        canvas.create_line(122, 44, 128, 50, width=2, fill=dead_c)
        canvas.create_line(128, 44, 122, 50, width=2, fill=dead_c)

# ====================================
# GAME STATE
# ====================================

word             = ""
guessed_letters  = []
wrong_guesses    = 0
aura             = 100
streak           = 0
game_over        = False

# ====================================
# ANIMATION HELPERS
# ====================================

def flash_label(label, flash_color, original_color, flashes=3, delay=80):
    """Quick color-flash animation for correct guesses."""
    def _run():
        for _ in range(flashes):
            label.configure(text_color=flash_color)
            time.sleep(delay / 1000)
            label.configure(text_color=original_color)
            time.sleep(delay / 1000)
    threading.Thread(target=_run, daemon=True).start()


def shake_widget(widget, distance=6, steps=6, delay=30):
    """Horizontal shake animation for wrong guesses."""
    original_x = widget.winfo_x()
    original_y = widget.winfo_y()

    def _run():
        for i in range(steps):
            offset = distance if i % 2 == 0 else -distance
            widget.place(x=original_x + offset, y=original_y)
            time.sleep(delay / 1000)
        widget.place_forget()
        widget.pack_configure()
    pass


# ====================================
# GAME LOGIC
# ====================================

def start_game():
    global word, guessed_letters, wrong_guesses, aura, game_over

    word            = random.choice(WORDS)
    guessed_letters = []
    wrong_guesses   = 0
    aura            = 100
    game_over       = False

    aura_bar.set(1)
    aura_bar.configure(progress_color=PINK)
    aura_label.configure(text="Aura: 100 ✨", text_color=PURPLE)
    result_label.configure(text="", text_color=TEXT)
    definition_label.configure(text="")
    guess_entry.configure(state="normal")
    guess_entry.delete(0, "end")
    app.title("💀 SLANGMAN 💀")

    update_display()


def update_display():
    display = "  ".join(
        letter.upper() if letter in guessed_letters else "_"
        for letter in word
    )
    word_label.configure(text=display)

    guessed_text = (
        "  ·  ".join(sorted(guessed_letters)).upper()
        if guessed_letters else "—"
    )
    guessed_label.configure(text=f"Guessed:  {guessed_text}")
    draw_hangman(hangman_canvas, wrong_guesses)
    streak_label.configure(text=f"🔥 Streak: {streak}")


def guess_letter(event=None):
    global wrong_guesses, aura, streak, game_over

    if game_over:
        return

    guess = guess_entry.get().lower().strip()
    guess_entry.delete(0, "end")

    if len(guess) != 1 or not guess.isalpha():
        return
    if guess in guessed_letters:
        result_label.configure(
            text="👀 Already guessed that one bro",
            text_color=MUTED
        )
        return

    guessed_letters.append(guess)

    if guess in word:
        result_label.configure(
            text=random.choice(CORRECT_MSGS),
            text_color=SUCCESS
        )
        flash_label(word_label, SUCCESS, YELLOW)
        app.title("🔥 BRO IS COOKING")

    else:
        wrong_guesses += 1
        aura = max(0, 100 - wrong_guesses * 15)
        aura_bar.set(aura / 100)

        if aura > 60:
            bar_color = PINK
        elif aura > 30:
            bar_color = "#F97316"   
        else:
            bar_color = DANGER

        aura_bar.configure(progress_color=bar_color)
        aura_label.configure(
            text=f"Aura: {aura} ✨",
            text_color=bar_color
        )
        result_label.configure(
            text=random.choice(WRONG_MSGS),
            text_color=DANGER
        )
        app.title(WRONG_WINDOW_TITLES.get(wrong_guesses, "💀 SLANGMAN 💀"))

    update_display()

  
    if all(letter in guessed_letters for letter in word):
        _handle_win()
        return

   
    if wrong_guesses >= MAX_WRONG:
        _handle_loss()


def _handle_win():
    global streak, game_over
    streak   += 1
    game_over = True

    win_title = random.choice(WIN_TITLES)
    meaning   = DEFINITIONS.get(word, "Certified Brainrot Term")

    result_label.configure(
        text=win_title,
        text_color=YELLOW
    )
    definition_label.configure(
        text=f"Word: {word.upper()}   ·   Meaning: {meaning}",
        text_color=YELLOW
    )
    guess_entry.configure(state="disabled")
    app.title("🏆 MAXIMUM RIZZ ACHIEVED")
    update_display()
    flash_label(result_label, YELLOW, YELLOW, flashes=4, delay=120)


def _handle_loss():
    global streak, game_over
    streak    = 0
    game_over = True

    lose_title = random.choice(LOSE_TITLES)

    result_label.configure(
        text=lose_title,
        text_color=DANGER
    )
    definition_label.configure(
        text=f"The word was:  {word.upper()}",
        text_color=DANGER
    )
    guess_entry.configure(state="disabled")
    app.title("💀 BRO IS COOKED 💀")
    update_display()


# ====================================
# GUI SETUP
# ====================================

app = ctk.CTk()
app.geometry("920x780")
app.resizable(False, False)
app.title("💀 SLANGMAN 💀")
app.configure(fg_color=BG)

# ── Outer border wrapper ─────────────────────────────────────────────────────
border_frame = ctk.CTkFrame(
    app,
    fg_color=BORDER,
    corner_radius=28
)
border_frame.pack(expand=True, fill="both", padx=20, pady=20)

# ── Main card ────────────────────────────────────────────────────────────────
main_frame = ctk.CTkFrame(
    border_frame,
    fg_color=CARD,
    corner_radius=25
)
main_frame.pack(expand=True, fill="both", padx=3, pady=3)

# ── Title ─────────────────────────────────────────────────────────────────────
title_label = ctk.CTkLabel(
    main_frame,
    text="💀  SLANGMAN  💀",
    font=FONT_TITLE,
    text_color=PINK
)
title_label.pack(pady=(22, 0))

subtitle_label = ctk.CTkLabel(
    main_frame,
    text="guess the brainrot word before your aura expires",
    font=("Arial", 13),
    text_color=MUTED
)
subtitle_label.pack(pady=(2, 8))

# ── Divider ───────────────────────────────────────────────────────────────────
divider_top = ctk.CTkFrame(main_frame, fg_color=BORDER, height=2, corner_radius=2)
divider_top.pack(fill="x", padx=40, pady=(0, 12))

# ── Hangman + Aura row ────────────────────────────────────────────────────────
top_row = ctk.CTkFrame(main_frame, fg_color="transparent")
top_row.pack(fill="x", padx=40)

# Hangman (left)
hangman_card = ctk.CTkFrame(top_row, fg_color=CARD_INNER, corner_radius=16)
hangman_card.pack(side="left", padx=(0, 16), pady=4)

hangman_canvas = tk.Canvas(
    hangman_card,
    width=160, height=180,
    bg=CARD_INNER,
    highlightthickness=0
)
hangman_canvas.pack(padx=16, pady=8)

# Aura + streak (right)
aura_panel = ctk.CTkFrame(top_row, fg_color=CARD_INNER, corner_radius=16)
aura_panel.pack(side="left", expand=True, fill="both", pady=4, ipadx=12, ipady=8)

aura_label = ctk.CTkLabel(
    aura_panel,
    text="Aura: 100 ✨",
    font=FONT_LABEL,
    text_color=PURPLE
)
aura_label.pack(pady=(12, 4))

aura_bar = ctk.CTkProgressBar(
    aura_panel,
    width=320,
    height=14,
    progress_color=PINK,
    corner_radius=7
)
aura_bar.pack(pady=(0, 10))
aura_bar.set(1)

streak_label = ctk.CTkLabel(
    aura_panel,
    text="🔥 Streak: 0",
    font=FONT_STREAK,
    text_color=SUCCESS
)
streak_label.pack(pady=(0, 12))

# ── Word display ──────────────────────────────────────────────────────────────
word_label = ctk.CTkLabel(
    main_frame,
    text="",
    font=FONT_WORD,
    text_color=YELLOW
)
word_label.pack(pady=(18, 6))

# ── Guessed letters ───────────────────────────────────────────────────────────
guessed_label = ctk.CTkLabel(
    main_frame,
    text="Guessed:  —",
    font=FONT_BODY,
    text_color=MUTED
)
guessed_label.pack(pady=(0, 10))

# ── Input row ─────────────────────────────────────────────────────────────────
input_row = ctk.CTkFrame(main_frame, fg_color="transparent")
input_row.pack(pady=6)

guess_entry = ctk.CTkEntry(
    input_row,
    width=180,
    height=44,
    placeholder_text="Type a letter…",
    font=("Arial", 16),
    corner_radius=12,
    border_color=PURPLE,
    border_width=2
)
guess_entry.pack(side="left", padx=(0, 10))
guess_entry.bind("<Return>", guess_letter)

guess_button = ctk.CTkButton(
    input_row,
    text="🔥  GUESS",
    command=guess_letter,
    width=130,
    height=44,
    font=("Arial Black", 15),
    fg_color=PURPLE,
    hover_color=PINK,
    corner_radius=12
)
guess_button.pack(side="left")

# ── Result label ──────────────────────────────────────────────────────────────
result_label = ctk.CTkLabel(
    main_frame,
    text="",
    font=FONT_RESULT,
    text_color=TEXT,
    wraplength=780
)
result_label.pack(pady=(14, 2))

# Definition / word reveal
definition_label = ctk.CTkLabel(
    main_frame,
    text="",
    font=("Arial", 15),
    text_color=YELLOW,
    wraplength=750
)
definition_label.pack(pady=(0, 8))

# ── Divider ───────────────────────────────────────────────────────────────────
divider_bot = ctk.CTkFrame(main_frame, fg_color=BORDER, height=2, corner_radius=2)
divider_bot.pack(fill="x", padx=40, pady=(4, 12))

# ── New Game button ───────────────────────────────────────────────────────────
new_game_btn = ctk.CTkButton(
    main_frame,
    text="🎮  NEW GAME",
    command=start_game,
    width=200,
    height=46,
    font=("Arial Black", 16),
    fg_color=PINK,
    hover_color=PURPLE,
    corner_radius=14
)
new_game_btn.pack(pady=(0, 18))

start_game()
app.mainloop()

