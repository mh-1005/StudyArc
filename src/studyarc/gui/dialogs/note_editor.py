import customtkinter as ctk


class NoteEditor(ctk.CTkToplevel):
    def __init__(self, master):
        super().__init__(master)

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

        button_frame = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        button_frame.pack(
            fill="x",
            padx=20,
            pady=20
        )

        cancel_button = ctk.CTkButton(
            button_frame,
            text="Cancel",
            command=self.destroy
        )

        cancel_button.pack(
            side="right",
            padx=(10, 0)
        )

        save_button = ctk.CTkButton(
            button_frame,
            text="Save"
        )

        save_button.pack(
            side="right"
        )
