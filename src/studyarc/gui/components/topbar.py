from turtle import title

import customtkinter as ctk

from studyarc.config import colors
from studyarc.config import fonts
from studyarc.config import constants


class TopBar(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master)

        self.configure(
            height=60,
            fg_color=colors.SIDEBAR
        )

        self.pack_propagate(False)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=3)
        self.grid_columnconfigure(2, weight=1)

        self.title = ctk.CTkLabel(
            self,
            text="Home",
            font=fonts.HEADING_FONT,
            text_color=colors.TEXT_PRIMARY
        )

        self.title.grid(
            row=0,
            column=0,
            sticky="w",
            padx=constants.PADDING,
            pady=10
        )


        search = ctk.CTkEntry(
            self,
            placeholder_text="Search...",
            width=500,
            height=38
        )

        search.grid(
            row=0,
            column=1,
            padx=20,
            pady=10
        )


        profile = ctk.CTkButton(
            self,
            text="MM",
            width=50,
            height=35,
            corner_radius=constants.CORNER_RADIUS
        )

        profile.grid(
            row=0,
            column=2,
            sticky="e",
            padx=constants.PADDING,
            pady=10
        )
    def set_title(self, title):
        self.title.configure(text=title)    