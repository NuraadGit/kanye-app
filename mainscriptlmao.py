import os
import pygame
import tkinter as tk
from tkinter import Canvas, Label
import customtkinter 

pygame.mixer.init()

def play_mp3(file_name):
    try:
        script_directory = os.path.dirname(os.path.abspath(__file__))
 
        mp3_path = os.path.join(script_directory, file_name)

        pygame.mixer.music.load(mp3_path)

    except Exception as e:
        print(f"nah, i dont feel like it: {e}")

def play_button_clicked():
    # PLAY THE THING!!!!!!!!!
    pygame.mixer.music.play()

def on_drag(event):
    x, y = event.x_root, event.y_root
    root.geometry(f"+{x-100}+{y-10}")

def close_window():
    root.destroy()

def minimize_window():
    root.iconify()

if __name__ == "__main__":
    # fire in the hole! joking this is the custom titlebar
    root = tk.Tk()
    root.title("¥$")
    root.overrideredirect(True)

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    window_width = 200
    window_height = 80
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2
    root.geometry(f"{window_width}x{window_height}+{x}+{y}")

    # make it BLACK
    root.configure(bg="#303030")  # background color

    # play the actual mp3
    play_mp3("everybody.mp3")

    # buttons in the titlebar
    button_frame = tk.Frame(root, bg="#303030", bd=1, relief="solid")
    button_frame.pack(side="top", fill="x")

    # close window
    close_button = Canvas(button_frame, width=20, height=20, bg="#303030", highlightthickness=0)
    close_button.create_line(5, 5, 15, 15, fill="white", width=2)
    close_button.create_line(5, 15, 15, 5, fill="white", width=2)
    close_button.bind("<Button-1>", lambda event: close_window())
    close_button.pack(side="right", padx=5)

    # minimize
    minimize_button = Canvas(button_frame, width=20, height=20, bg="#303030", highlightthickness=0)
    minimize_button.create_line(5, 15, 15, 15, fill="white", width=2)
    minimize_button.bind("<Button-1>", lambda event: minimize_window())
    minimize_button.pack(side="right", padx=5)

    title_label = Label(button_frame, text="¥$", bg="#303030", fg="white", font=("Helvetica", 10))
    title_label.pack(side="left", padx=5)

    # dragify
    root.bind("<B1-Motion>", on_drag)

    # custom tkinter thing
    play_button = customtkinter.CTkButton(root, text="Play the thing!!!!", command=play_button_clicked, fg_color="#505050")
    play_button.pack(pady=15, padx=(50, 50))  # Adjust the padx values as needed for the desired width

    # nah i dont feel like explaining
    root.resizable(width=False, height=False)

    # LOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOP
    root.mainloop()
