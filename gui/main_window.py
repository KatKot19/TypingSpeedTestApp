import tkinter as tk
from tkinter import ttk
from utils.helpers import load_random_text
from logic.typing_logic import TypingLogic
import time



class TypingSpeedTestApp:
    def __init__(self):
        self.window=tk.Tk()
        self.window.title("Typing Speed Test")
        self.window.geometry("800x400")

        self.main_frame=ttk.Frame(self.window,padding=20)
        self.main_frame.pack(fill="both",expand=True)

        self.text_label=ttk.Label(
            self.main_frame,
            text='',
            wraplength=700,
            font=("Segoe UI",12)
        )
        self.text_label.pack(pady=20)

        self.entry=tk.Text(self.main_frame,height=5,font=('Segoe UI',12))
        self.entry.pack(fill='x')


        self.submit_button=ttk.Button(
            self.main_frame,
            text='Submit',
            command=self.on_submit
        )
        self.submit_button.pack(pady=10)

        self.timer_label = ttk.Label(
            self.main_frame,
            text="Time: 0s",
            font=("Segoe UI", 12)
        )
        self.timer_label.pack(pady=10)

        self.logic=TypingLogic()
        self.target_text=load_random_text()
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
        popup.geometry("300x220")

        result_label = ttk.Label(
            popup,
            text=f"WPM: {wpm:.2f}\nAccuracy: {accuracy:.2f}%",
            font=("Segoe UI", 12),
            justify="center"
        )
        result_label.pack(expand=True, pady=20)

        close_button = ttk.Button(popup, text="Close", command=popup.destroy)
        close_button.pack(pady=10)

        restart_button=ttk.Button(popup,text="Restart",command=lambda: self.restart_test(popup))
        restart_button.pack(pady=10)


    def restart_test(self,popup):
        popup.destroy()
        self.entry.delete("1.0","end")
        self.target_text=load_random_text()
        self.text_label.config(text=self.target_text)
        self.start_time=None
        self.running=False
        self.timer_started=False
        self.timer_label.config(text="Time: 0s")










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