import tkinter as tk
from tkinter import ttk



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

    def on_submit(self):
            print("User submitted text!")

    def run(self):
            self.window.mainloop()


if __name__=="__main__":
    app=TypingSpeedTestApp()
    app.run()