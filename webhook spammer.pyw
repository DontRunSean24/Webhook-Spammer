import tkinter as tk
import requests
import threading
import time
from tkinter import ttk

class DiscordWebhookSpammer:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Discord Webhook Spammer")
        self.window.configure(bg="black")

        self.webhook_label = tk.Label(self.window, text="Webhook URL:", bg="black", fg="white")
        self.webhook_label.pack()

        self.webhook_entry = tk.Entry(self.window, width=50)
        self.webhook_entry.pack()

        separator = ttk.Separator(self.window, orient='horizontal')
        separator.pack(fill='x', pady=10)

        self.buffer_label = tk.Label(self.window, text="Delay (in seconds):", bg="black", fg="white")
        self.buffer_label.pack()

        self.buffer_entry = tk.Entry(self.window, width=10)
        self.buffer_entry.pack()

        separator = ttk.Separator(self.window, orient='horizontal')
        separator.pack(fill='x', pady=10)

        self.start_button = tk.Button(self.window, text="Start", command=self.start_spam, bg="black", fg="white", width=20, height=2)
        self.start_button.pack()

        self.stop_button = tk.Button(self.window, text="Stop", command=self.stop_spam, bg="black", fg="white", width=20, height=2, state=tk.DISABLED)
        self.stop_button.pack()

        self.is_spamming = False
        self.spam_thread = None
        self.buffer = 0

    def start_spam(self):
        if not self.is_spamming:
            self.is_spamming = True
            self.start_button.config(state=tk.DISABLED)
            self.stop_button.config(state=tk.NORMAL)
            self.buffer = int(self.buffer_entry.get()) if self.buffer_entry.get().isdigit() else 0
            self.spam_thread = threading.Thread(target=self.spam)
            self.spam_thread.start()

    def stop_spam(self):
        if self.is_spamming:
            self.is_spamming = False
            self.start_button.config(state=tk.NORMAL)
            self.stop_button.config(state=tk.DISABLED)

    def spam(self):
        webhook_url = self.webhook_entry.get()
        while self.is_spamming:
            try:
                requests.post(webhook_url, json={"content": "L SCAMMER"}) #chage this to what you want it to say in the chat [" chat spammer "]
            except Exception as e:
                print(f"Error: {e}")
            time.sleep(self.buffer)

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    spammer = DiscordWebhookSpammer()
    spammer.run()
