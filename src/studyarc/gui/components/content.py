import customtkinter as ctk


class Content(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        title = ctk.CTkLabel(
            self,
            text="Welcome to StudyArc",
            font=("Arial", 28, "bold")
        )

        subtitle = ctk.CTkLabel(
            self,
            text="Your AI-powered study companion",
            font=("Arial", 16)
        )

        title.pack(pady=(60, 10))
        subtitle.pack()
