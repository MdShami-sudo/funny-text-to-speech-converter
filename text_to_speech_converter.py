import tkinter as tk
from tkinter import messagebox
import pyttsx3
import random

class FunnyTTS:
    def __init__(self, root):
        self.root = root
        self.root.title("Funny Text-to-Speech Converter")
        self.root.geometry("500x400")
        self.root.configure(bg="skyblue")

        self.label = tk.Label(root, text="Enter your funny message:", font=("Comic Sans MS", 14), bg="#ffefd5")
        self.label.pack(pady=10)

        self.text_area = tk.Text(root, height=5, font=("Comic Sans MS", 12), wrap=tk.WORD, padx=10, pady=10, bg="#ffffff", fg="#333333")
        self.text_area.pack(pady=10)

        self.convert_button = tk.Button(root, text="Make Me Laugh!", font=("Comic Sans MS", 14), bg="#ff6347", fg="#ffffff", command=self.convert_to_speech)
        self.convert_button.pack(pady=20)

        self.funny_quotes_button = tk.Button(root, text="Random Funny Quote", font=("Comic Sans MS", 14), bg="#ff6347", fg="#ffffff", command=self.insert_funny_quote)
        self.funny_quotes_button.pack(pady=10)

        self.funny_quotes = [
            "I'm on a seafood diet. I see food and I eat it.",
            "I'm reading a book on anti-gravity. It's impossible to put down!",
            "Why don't scientists trust atoms? Because they make up everything!",
            "I told my wife she was drawing her eyebrows too high. She looked surprised."
        ]

    def insert_funny_quote(self):
        random_quote = random.choice(self.funny_quotes)
        self.text_area.delete("1.0", tk.END)
        self.text_area.insert(tk.END, random_quote)

    def convert_to_speech(self):
        message = self.text_area.get("1.0", tk.END).strip()
        if message:
            self.speak(message)
        else:
            messagebox.showwarning("Warning", "Please enter a funny message!")

    def speak(self, message):
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[random.choice([0, 1])].id)  
        engine.setProperty('rate', 150)  
        engine.setProperty('volume', 1) 
        engine.say(message)
        engine.runAndWait()

if __name__ == "__main__":
    root = tk.Tk()
    app = FunnyTTS(root)
    root.mainloop()
