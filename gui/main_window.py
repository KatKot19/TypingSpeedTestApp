import tkinter as tk
from tkinter import ttk
from utils.helpers import load_random_text
from logic.typing_logic import TypingLogic
import time



class TypingSpeedTestApp:
    def __init__(self):

        self.window=tk.Tk()
        self.window.title("Typing Speed Test")
        self.window.geometry("900x500")
        self.window.config(bg="#f4f6f8")

        style=ttk.Style(self.window)
        style.configure("Card.TFrame", background="#ffffff")
        style.configure("Title.TLabel", font=("Segoe UI", 16, "bold"), background="#ffffff")
        style.configure("Body.TLabel", font=("Segoe UI", 12), background="#ffffff")
        style.configure("Timer.TLabel", font=("Segoe UI", 12, "bold"), background="#f4f6f8")
        style.configure("TButton", font=("Segoe UI", 12))


        self.main_frame=ttk.Frame(self.window,style="Card.TFrame",padding=(20,10))
        self.main_frame.place(relx=0.5, rely=0.5, anchor="center", relwidth=0.9, relheight=0.9)

        self.text_frame = ttk.Frame(self.main_frame, style="Card.TFrame")
        self.text_frame.pack(fill='both', expand=False, pady=(0, 12))

        self.entry_frame = ttk.Frame(self.main_frame, style="Card.TFrame")
        self.entry_frame.pack(fill='x', pady=(0, 12))

        self.footer_frame = ttk.Frame(self.main_frame, style="Card.TFrame")
        self.footer_frame.pack(fill='x')

        self.text_label=ttk.Label(
            self.main_frame,
            text='',
            style="Title.TLabel",
            wraplength=760,
            justify="center"
        )
        self.text_label.pack(anchor="n",pady=(0,10))

        entry_container = tk.Frame(self.entry_frame, bg="#eef2f6", padx=6, pady=6)
        entry_container.pack(fill='x', padx=10)

        self.entry = tk.Text(entry_container, height=6, font=('Segoe UI', 13), bd=0, wrap="word")
        self.entry.pack(fill='x', pady=(0,10))

        controls_frame = ttk.Frame(self.entry_frame)
        controls_frame.pack(fill='x', padx=10, pady=(8,0))


        self.submit_button = ttk.Button(controls_frame, text='Submit', command=self.on_submit)
        self.submit_button.pack(pady=(0,20))

        self.timer_label = ttk.Label(self.footer_frame, text="Time: 0s", style="Timer.TLabel")
        self.timer_label.pack(side="left", padx=(10,0))

        self.info_label = ttk.Label(self.footer_frame, text="Ο χρόνος θα ξεκινήσει με κλικ στο πεδίο κειμένου.", style="Body.TLabel")
        self.info_label.pack(side="right", padx=(0,10))

        self.logic = TypingLogic()
        self.target_text = load_random_text()
        self.text_label.config(text=self.target_text)


        self.start_time=None
        self.running=False
        self.timer_started=False
        self.entry.bind("<Button-1>",self.start_timer_on_click)


    def start_timer_on_click(self,event=None):
        if not self.timer_started:
            self.start_time=time.time()
            self.running=True
            self.timer_started=True
            self.info_label.config(text="Timer running...")
            self.update_timer()

    def on_submit(self):
            typed_text=self.entry.get("1.0","end-1c")
            elapsed_time=time.time()-self.start_time if self.start_time else 0

            wpm=self.logic.calculate_wpm(typed_text, elapsed_time)
            accuracy=self.logic.calculate_accuracy(typed_text,self.target_text)

            self.running=False
            self.show_results_popup(wpm,accuracy)

    def show_results_popup(self, wpm, accuracy):

        popup = tk.Toplevel(self.window)
        popup.title("Results")
        popup.geometry("380x220")
        popup.config(bg="#f4f6f8")

        card = ttk.Frame(popup, style="Card.TFrame", padding=12)
        card.place(relx=0.5, rely=0.5, anchor="center", relwidth=0.95, relheight=0.9)

        result_text = f"WPM: {wpm:.2f}\nAccuracy: {accuracy:.2f}"
        card = ttk.Frame(popup, style="Card.TFrame", padding=12)
        card.place(relx=0.5, rely=0.5, anchor="center", relwidth=0.95, relheight=0.9)

        result_text = f"WPM: {wpm:.2f}\nAccuracy: {accuracy:.2f}%"
        result_label = ttk.Label(card, text=result_text, style="Body.TLabel", justify="center")
        result_label.pack(expand=True, pady=(8, 10))

        button_frame = ttk.Frame(card)
        button_frame.pack(pady=(6, 4))

        close_button = ttk.Button(button_frame, text="Close", command=popup.destroy)
        close_button.pack(side="left", padx=8)

        restart_button = ttk.Button(button_frame, text="Restart", command=lambda: self.restart_test(popup))
        restart_button.pack(side="left", padx=8)

    def restart_test(self,popup):
            try:
                popup.destroy()
            except Exception:
                pass

            self.entry.delete("1.0", "end")

            self.target_text = load_random_text()
            self.text_label.config(text=self.target_text)

            self.start_time = None
            self.running = False
            self.timer_started = False
            self.timer_label.config(text="Time: 0s")
            self.info_label.config(text="Ο χρόνος θα ξεκινήσει με κλικ στο πεδίο κειμένου.")

    def update_timer(self):
        if self.running:
            elapsed = int(time.time() - self.start_time)
            self.timer_label.config(text=f"Time: {elapsed}s")
            self.window.after(1000, self.update_timer)

    def run(self):
            self.window.mainloop()




if __name__=="__main__":
    app=TypingSpeedTestApp()
    app.run()