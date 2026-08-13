import customtkinter as ctk

from studyarc.config import colors
from studyarc.config import fonts

from studyarc.gui.dialogs.note_editor import NoteEditor
from studyarc.gui.components.note_card import NoteCard


class NotesPage(ctk.CTkFrame):
    def __init__(self, master, note_service):
        super().__init__(master)

        self.note_service = note_service
        self.note_service.add_listener(self.refresh_notes)

        new_note_button = ctk.CTkButton(
            self, text="+ New Note", command=self.open_note_editor
        )

        new_note_button.pack(pady=(35, 30))

        self.notes_container = ctk.CTkFrame(self, fg_color="transparent")

        self.notes_container.pack(fill="both", expand=True, padx=40, pady=(0, 25))

        self.refresh_notes()

    def open_note_editor(self):
        NoteEditor(self, self.note_service)

    def refresh_notes(self):
        for widget in self.notes_container.winfo_children():
            widget.destroy()

        notes = self.note_service.get_notes()

        if not notes:
            empty_message = ctk.CTkLabel(
                self.notes_container,
                text="📝\n\nNo notes yet\n\nCreate your first note to start studying.",
                font=fonts.BODY_FONT,
                text_color=colors.TEXT_SECONDARY,
                justify="center",
            )

            empty_message.pack(expand=True)

            return

        for note in notes:
            note_card = NoteCard(self.notes_container, note, command=self.open_note)

            note_card.pack(pady=10)

    def open_note(self, note):
        NoteEditor(self, self.note_service, note)

    def destroy(self):
        self.note_service.remove_listener(self.refresh_notes)
        super().destroy()
