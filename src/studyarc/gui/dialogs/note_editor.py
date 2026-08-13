import customtkinter as ctk
from studyarc.models import note
from studyarc.models.note import Note


class NoteEditor(ctk.CTkToplevel):
    def __init__(self, master, note_service, note=None):
        super().__init__(master)

        self.note_service = note_service
        self.note = note

        if self.note:
            self.title("Edit Note")
        else:
            self.title("New Note")

        self.geometry("700x600")
        self.resizable(False, False)

        title_label = ctk.CTkLabel(self, text="Title")
        title_label.pack(anchor="w", padx=20, pady=(20, 5))

        self.title_entry = ctk.CTkEntry(self, placeholder_text="Enter note title...")
        self.title_entry.pack(fill="x", padx=20)

        subject_label = ctk.CTkLabel(self, text="Subject")
        subject_label.pack(anchor="w", padx=20, pady=(20, 5))

        self.subject_entry = ctk.CTkEntry(self, placeholder_text="e.g. Python")
        self.subject_entry.pack(fill="x", padx=20)

        content_label = ctk.CTkLabel(self, text="Content")
        content_label.pack(anchor="w", padx=20, pady=(20, 5))

        self.content_text = ctk.CTkTextbox(self, height=250)
        self.content_text.pack(fill="both", expand=True, padx=20)

        if self.note:
            self.title_entry.insert(0, self.note.title)
            self.subject_entry.insert(0, self.note.subject)
            self.content_text.insert("1.0", self.note.content)

        button_frame = ctk.CTkFrame(self, fg_color="transparent")

        button_frame.pack(fill="x", padx=20, pady=20)

        cancel_button = ctk.CTkButton(button_frame, text="Cancel", command=self.destroy)

        cancel_button.pack(side="right", padx=(10, 0))

        delete_button = ctk.CTkButton(
            button_frame,
            text="Delete",
            fg_color="red",
            hover_color="#b22222",
            command=self.delete_note,
        )
        if self.note:
            delete_button.pack(side="left")

        save_button = ctk.CTkButton(button_frame, text="Save", command=self.save_note)

        save_button.pack(side="right")

    def save_note(self):
        note = Note(
            title=self.title_entry.get(),
            subject=self.subject_entry.get(),
            content=self.content_text.get("1.0", "end-1c"),
        )

        if self.note:
            self.note_service.update_note(self.note, note)
        else:
            self.note_service.add_note(note)

        self.destroy()

    def delete_note(self):
        self.note_service.delete_note(self.note)
        self.destroy()
