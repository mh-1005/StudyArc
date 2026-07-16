import customtkinter as ctk


class MainWindow(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("StudyArc")
        self.geometry("1000x700")

        label = ctk.CTkLabel(
            self,
            text="Welcome to StudyArc 🚀",
            font=("Arial", 24),
        )
        label.pack(expand=True)
