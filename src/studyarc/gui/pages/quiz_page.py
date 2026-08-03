import customtkinter as ctk

from studyarc.config import colors
from studyarc.config import fonts


class QuizPage(ctk.CTkFrame):
    def __init__(self, master, note_service=None):
        super().__init__(master)

        title = ctk.CTkLabel(
            self, text="Quiz", font=fonts.TITLE_FONT, text_color=colors.TEXT_PRIMARY
        )

        subtitle = ctk.CTkLabel(
            self,
            text="Generate quizzes and test your knowledge.",
            font=fonts.BODY_FONT,
            text_color=colors.TEXT_SECONDARY,
        )

        title.pack(pady=(60, 10))
        subtitle.pack()
