import customtkinter as ctk


class Sidebar(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.configure(width=220)

        title = ctk.CTkLabel(
            self,
            text="StudyArc",
            font=("Arial", 24, "bold")
        )

        title.pack(pady=(30, 20))

        buttons = [
            "🏠 Home",
            "📝 Notes",
            "🃏 Flashcards",
            "❓ Quiz",
            "⚙️ Settings"
        ]

        for text in buttons:
            button = ctk.CTkButton(
                self,
                text=text
            )
            button.pack(
                padx=20,
                pady=8,
                fill="x"
            )
