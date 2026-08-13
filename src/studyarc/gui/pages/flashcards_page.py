import customtkinter as ctk

from studyarc.config import colors
from studyarc.config import fonts


class FlashcardsPage(ctk.CTkFrame):
    def __init__(self, master, note_service):
        super().__init__(master)

        self.note_service = note_service

        title = ctk.CTkLabel(
            self,
            text="Flashcards",
            font=fonts.TITLE_FONT,
            text_color=colors.TEXT_PRIMARY,
        )

        subtitle = ctk.CTkLabel(
            self,
            text="Review concepts using spaced repetition.",
            font=fonts.BODY_FONT,
            text_color=colors.TEXT_SECONDARY,
        )

        title.pack(pady=(60, 10))
        subtitle.pack()
