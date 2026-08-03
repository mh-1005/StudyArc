import customtkinter as ctk

from studyarc.config import colors
from studyarc.config import constants
from studyarc.config import fonts
from studyarc.gui.components import content


class NoteCard(ctk.CTkFrame):

    def __init__(self, master, note, command=None):
        super().__init__(master)

        self.note = note
        self.command = command

        self.configure(
            fg_color=colors.CARD,
            corner_radius=constants.CORNER_RADIUS,
            width=560,
        )

        self.pack_propagate(False)

        title = ctk.CTkLabel(
            self,
            text=note.title,
            font=fonts.HEADING_FONT,
            text_color=colors.TEXT_PRIMARY,
        )

        title.pack(anchor="w", padx=20, pady=(18, 8))

        subject = ctk.CTkLabel(
            self,
            text=f"📄 {note.subject}",
            font=fonts.BODY_FONT,
            text_color=colors.TEXT_SECONDARY,
        )

        subject.pack(anchor="w", padx=20, pady=(0, 10))

        preview = note.content.strip()

        # Show only the first paragraph
        preview = preview.split("\n")[0]

        if len(preview) > 100:
            preview = preview[:100]
            preview = preview.rsplit(" ", 1)[0]
            preview += "..."

        content = ctk.CTkLabel(
            self, text=preview, justify="left", wraplength=500, font=fonts.BODY_FONT
        )

        content.pack(anchor="w", padx=20, pady=(0, 18))

        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)
        self.bind("<Button-1>", self.on_click)

    def on_enter(self, event):
        self.configure(fg_color=colors.CARD_HOVER)

    def on_leave(self, event):
        self.configure(fg_color=colors.CARD)

    def on_click(self, event):
        if self.command:
            self.command(self.note)
