"""Beautiful GUI Wordle Game with Modern Design"""

import tkinter as tk
from tkinter import messagebox
import tkinter.font as tkFont
from encrypted_word import get_word, data
from check import right_pos, letter_found, validate_input
import random

WORD_LENGTH = 5
MAX_ATTEMPTS = 6

# Color Palette - Modern Vibrant Design
COLORS = {
    'bg_dark': '#0a0e27',
    'bg_light': '#1a1f3a',
    'bg_input': '#16213e',
    'accent_green': '#10b981',
    'accent_yellow': '#f59e0b',
    'accent_red': '#ef4444',
    'accent_blue': '#3b82f6',
    'accent_purple': '#8b5cf6',
    'text_primary': '#ffffff',
    'text_secondary': '#94a3b8',
    'border': '#334155',
    'success': '#34d399',
    'warning': '#fbbf24',
}


class WordleGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("🎮 Wordle Game - Guess the Word!")
        self.root.geometry("800x700")
        self.root.configure(bg=COLORS['bg_dark'])
        
        # Game state
        self.encrypted_word = get_word().lower()
        self.attempts = []
        self.current_attempt = 0
        self.game_won = False
        self.game_over = False
        
        # Fonts
        self.font_title = tkFont.Font(family="Helvetica", size=32, weight="bold")
        self.font_large = tkFont.Font(family="Helvetica", size=18, weight="bold")
        self.font_medium = tkFont.Font(family="Helvetica", size=14, weight="bold")
        self.font_small = tkFont.Font(family="Helvetica", size=11)
        self.font_tiny = tkFont.Font(family="Helvetica", size=9)
        
        self.setup_ui()
        self.update_display()
        
    def setup_ui(self):
        """Setup the user interface"""
        # Main container
        main_frame = tk.Frame(self.root, bg=COLORS['bg_dark'])
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Header
        header_frame = tk.Frame(main_frame, bg=COLORS['bg_dark'])
        header_frame.pack(fill=tk.X, pady=(0, 20))
        
        title = tk.Label(
            header_frame,
            text="🎮 WORDLE",
            font=self.font_title,
            bg=COLORS['bg_dark'],
            fg=COLORS['accent_blue']
        )
        title.pack(side=tk.LEFT)
        
        # Subtitle
        subtitle = tk.Label(
            header_frame,
            text="Guess the 5-letter word!",
            font=self.font_small,
            bg=COLORS['bg_dark'],
            fg=COLORS['text_secondary']
        )
        subtitle.pack(side=tk.LEFT, padx=20)
        
        # Game info bar
        info_frame = tk.Frame(main_frame, bg=COLORS['bg_light'], highlightthickness=2, highlightbackground=COLORS['border'])
        info_frame.pack(fill=tk.X, pady=(0, 15))
        
        self.attempts_label = tk.Label(
            info_frame,
            text=f"Attempts: 0/{MAX_ATTEMPTS}",
            font=self.font_medium,
            bg=COLORS['bg_light'],
            fg=COLORS['accent_blue']
        )
        self.attempts_label.pack(side=tk.LEFT, padx=15, pady=10)
        
        self.status_label = tk.Label(
            info_frame,
            text="🎯 Game in Progress",
            font=self.font_medium,
            bg=COLORS['bg_light'],
            fg=COLORS['text_secondary']
        )
        self.status_label.pack(side=tk.RIGHT, padx=15, pady=10)
        
        # Previous attempts display
        attempts_frame = tk.Frame(main_frame, bg=COLORS['bg_dark'])
        attempts_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 20))
        
        attempts_label = tk.Label(
            attempts_frame,
            text="Previous Guesses:",
            font=self.font_medium,
            bg=COLORS['bg_dark'],
            fg=COLORS['text_primary']
        )
        attempts_label.pack(anchor=tk.W, pady=(0, 10))
        
        # Scrollable attempts area
        self.attempts_display = tk.Frame(attempts_frame, bg=COLORS['bg_light'], highlightthickness=1, highlightbackground=COLORS['border'])
        self.attempts_display.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Input frame
        input_frame = tk.Frame(main_frame, bg=COLORS['bg_dark'])
        input_frame.pack(fill=tk.X, pady=(0, 15))
        
        input_label = tk.Label(
            input_frame,
            text="Your Guess:",
            font=self.font_medium,
            bg=COLORS['bg_dark'],
            fg=COLORS['text_primary']
        )
        input_label.pack(anchor=tk.W, pady=(0, 8))
        
        # Input entry with modern styling
        entry_wrapper = tk.Frame(input_frame, bg=COLORS['bg_input'], highlightthickness=2, highlightbackground=COLORS['accent_blue'])
        entry_wrapper.pack(fill=tk.X)
        
        self.entry = tk.Entry(
            entry_wrapper,
            font=self.font_large,
            bg=COLORS['bg_input'],
            fg=COLORS['text_primary'],
            border=0,
            justify=tk.CENTER,
            insertbackground=COLORS['accent_blue']
        )
        self.entry.pack(fill=tk.X, padx=15, pady=12)
        self.entry.bind('<Return>', lambda e: self.submit_guess())
        self.entry.bind('<FocusIn>', self.on_entry_focus_in)
        self.entry.bind('<FocusOut>', self.on_entry_focus_out)
        
        # Button frame
        button_frame = tk.Frame(main_frame, bg=COLORS['bg_dark'])
        button_frame.pack(fill=tk.X)
        
        self.submit_btn = self.create_button(
            button_frame,
            text="🎯 SUBMIT GUESS",
            command=self.submit_guess,
            color=COLORS['accent_green']
        )
        self.submit_btn.pack(side=tk.LEFT, padx=5, expand=True, fill=tk.BOTH)
        
        hint_btn = self.create_button(
            button_frame,
            text="💡 HINT",
            command=self.show_hint,
            color=COLORS['accent_yellow']
        )
        hint_btn.pack(side=tk.LEFT, padx=5, expand=True, fill=tk.BOTH)
        
        reset_btn = self.create_button(
            button_frame,
            text="🔄 NEW GAME",
            command=self.reset_game,
            color=COLORS['accent_purple']
        )
        reset_btn.pack(side=tk.LEFT, padx=5, expand=True, fill=tk.BOTH)
        
        # Focus on entry field
        self.entry.focus()
    
    def create_button(self, parent, text, command, color):
        """Create a styled button"""
        btn = tk.Button(
            parent,
            text=text,
            command=command,
            font=self.font_medium,
            bg=color,
            fg=COLORS['bg_dark'],
            border=0,
            padx=15,
            pady=12,
            cursor="hand2",
            activebackground=color,
            activeforeground=COLORS['bg_dark']
        )
        btn.pack(side=tk.LEFT, padx=5, expand=True, fill=tk.BOTH)
        
        # Hover effect
        btn.bind('<Enter>', lambda e: btn.config(relief=tk.RAISED))
        btn.bind('<Leave>', lambda e: btn.config(relief=tk.FLAT))
        
        return btn
    
    def on_entry_focus_in(self, event):
        """Handle entry focus in"""
        wrapper = event.widget.master
        wrapper.config(highlightbackground=COLORS['accent_green'])
    
    def on_entry_focus_out(self, event):
        """Handle entry focus out"""
        wrapper = event.widget.master
        wrapper.config(highlightbackground=COLORS['accent_blue'])
    
    def submit_guess(self):
        """Submit a guess"""
        if self.game_over:
            messagebox.showinfo("Game Over", "Game is finished! Click 'NEW GAME' to play again.")
            return
        
        guess = self.entry.get().strip().lower()
        self.entry.delete(0, tk.END)
        
        is_valid, error_msg, normalized_guess = validate_input(guess, data)
        if not is_valid:
            messagebox.showerror("Invalid Input", error_msg)
            self.entry.focus()
            return
        
        # Check if already guessed
        if any(attempt[0] == normalized_guess for attempt in self.attempts):
            messagebox.showwarning("Already Guessed", "You already guessed this word!")
            self.entry.focus()
            return
        
        self.current_attempt += 1
        self.attempts.append((normalized_guess, self.get_feedback(normalized_guess)))
        
        if normalized_guess == self.encrypted_word:
            self.game_won = True
            self.game_over = True
        elif self.current_attempt >= MAX_ATTEMPTS:
            self.game_over = True
        
        self.update_display()
        
        if self.game_won:
            self.show_win_dialog()
        elif self.game_over:
            self.show_loss_dialog()
        
        self.entry.focus()
    
    def get_feedback(self, guess):
        """Get color feedback for a guess"""
        correct_positions = right_pos(guess, self.encrypted_word)
        wrong_positions = letter_found(guess, self.encrypted_word)
        
        feedback = []
        for i in range(WORD_LENGTH):
            if correct_positions[i] == 1:
                feedback.append(('green', guess[i]))
            elif wrong_positions[i] == 1:
                feedback.append(('yellow', guess[i]))
            else:
                feedback.append(('gray', guess[i]))
        
        return feedback
    
    def update_display(self):
        """Update the display with current game state"""
        # Clear previous attempts display
        for widget in self.attempts_display.winfo_children():
            widget.destroy()
        
        if not self.attempts:
            placeholder = tk.Label(
                self.attempts_display,
                text="No guesses yet...",
                font=self.font_small,
                bg=COLORS['bg_light'],
                fg=COLORS['text_secondary']
            )
            placeholder.pack(pady=20)
        
        # Display all attempts
        for idx, (guess, feedback) in enumerate(self.attempts):
            attempt_frame = tk.Frame(self.attempts_display, bg=COLORS['bg_light'])
            attempt_frame.pack(fill=tk.X, padx=10, pady=5)
            
            attempt_num = tk.Label(
                attempt_frame,
                text=f"#{idx + 1}",
                font=self.font_small,
                bg=COLORS['bg_light'],
                fg=COLORS['text_secondary'],
                width=4
            )
            attempt_num.pack(side=tk.LEFT, padx=(0, 10))
            
            # Display each letter with color
            for color, letter in feedback:
                if color == 'green':
                    bg_color = COLORS['accent_green']
                elif color == 'yellow':
                    bg_color = COLORS['accent_yellow']
                else:
                    bg_color = COLORS['border']
                
                letter_label = tk.Label(
                    attempt_frame,
                    text=letter.upper(),
                    font=self.font_medium,
                    bg=bg_color,
                    fg=COLORS['bg_dark'] if color != 'gray' else COLORS['text_secondary'],
                    width=3,
                    relief=tk.RAISED,
                    bd=2
                )
                letter_label.pack(side=tk.LEFT, padx=3)
        
        # Update attempts label
        self.attempts_label.config(text=f"Attempts: {self.current_attempt}/{MAX_ATTEMPTS}")
        
        # Update status label
        if self.game_won:
            self.status_label.config(text="✅ YOU WON!", fg=COLORS['success'])
        elif self.game_over:
            self.status_label.config(text="❌ GAME OVER", fg=COLORS['accent_red'])
        else:
            remaining = MAX_ATTEMPTS - self.current_attempt
            self.status_label.config(text=f"🎯 {remaining} attempts left", fg=COLORS['accent_blue'])
    
    def show_hint(self):
        """Show a hint about the word"""
        if self.game_over:
            messagebox.showinfo("Game Over", "Game is finished! Click 'NEW GAME' to play again.")
            return
        
        hints = {
            'animal': 'It could be an animal',
            'color': 'It could be a color',
            'food': 'It could be food',
            'place': 'It could be a place',
            'action': 'It could be an action word',
            'object': 'It could be an object',
            'person': 'It could be a person',
            'nature': 'It could be from nature',
        }
        
        word_hint = random.choice(list(hints.values()))
        messagebox.showinfo("Hint 💡", f"{word_hint}\n\nThe word is: {self.encrypted_word[0]}__{self.encrypted_word[-1]}")
    
    def reset_game(self):
        """Start a new game"""
        self.encrypted_word = get_word().lower()
        self.attempts = []
        self.current_attempt = 0
        self.game_won = False
        self.game_over = False
        self.entry.delete(0, tk.END)
        self.entry.focus()
        self.update_display()
    
    def show_win_dialog(self):
        """Show win dialog"""
        messagebox.showinfo(
            "🎉 YOU WON! 🎉",
            f"Congratulations! 🎊\n\nYou guessed '{self.encrypted_word.upper()}' in {self.current_attempt} attempts!\n\nClick 'NEW GAME' to play again."
        )
    
    def show_loss_dialog(self):
        """Show loss dialog"""
        messagebox.showinfo(
            "❌ GAME OVER ❌",
            f"Game Over!\n\nThe word was: {self.encrypted_word.upper()}\n\nClick 'NEW GAME' to try again."
        )


def main():
    root = tk.Tk()
    app = WordleGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()