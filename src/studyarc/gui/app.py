import customtkinter as ctk

from studyarc.gui.main_window import MainWindow


def run():
    ctk.set_appearance_mode("System")
    ctk.set_default_color_theme("blue")

    app = MainWindow()
    app.mainloop()
