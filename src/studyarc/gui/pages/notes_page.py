import customtkinter as ctk

from studyarc.config import colors
from studyarc.config import fonts

from studyarc.gui.dialogs.note_editor import NoteEditor


class NotesPage(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        new_note_button = ctk.CTkButton(
            self, text="+ New Note", command=self.open_note_editor
        )

        new_note_button.pack(pady=(40, 20))

        empty_message = ctk.CTkLabel(
            self,
            text="No notes yet.\nClick '+ New Note' to create one.",
            font=fonts.BODY_FONT,
            text_color=colors.TEXT_SECONDARY,
        )

        empty_message.pack(expand=True)

    def open_note_editor(self):
        NoteEditor(self)
