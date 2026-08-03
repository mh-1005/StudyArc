from turtle import heading

import customtkinter as ctk

from studyarc.config import colors
from studyarc.config import fonts
from studyarc.config import constants


class Card(ctk.CTkFrame):
    def __init__(self, master, title, command=None):
        super().__init__(master)

        self.command = command

        self.configure(fg_color=colors.SIDEBAR, corner_radius=constants.CORNER_RADIUS)

        heading = ctk.CTkLabel(
            self,
            text=title,
            font=fonts.HEADING_FONT,
            text_color=colors.TEXT_PRIMARY,
            anchor="center",
        )

        heading.pack(expand=True, pady=constants.PADDING)

        self.bind("<Button-1>", self.on_click)
        heading.bind("<Button-1>", self.on_click)

    def on_click(self, event):
        if self.command:
            self.command()
