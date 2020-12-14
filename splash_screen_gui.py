from tkinter import *

splash_root = Tk()
splash_root.title("Splash Screen!")
splash_root.geometry("300x200")

splash_label = Label(splash_root, text="Splash Screen!", font=("Helvetica", 18))
splash_label.pack(pady=20)

def main_window():
    splash_root.destroy()
    root = Tk()
    root.title("Main Screen")
    root.geometry("500x550")

# Splash Screen timer
splash_root.after(3000, main_window)

mainloop()