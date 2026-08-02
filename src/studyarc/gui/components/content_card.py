import customtkinter as ctk

from studyarc.config import colors
from studyarc.config import fonts
from studyarc.config import constants


class ContentCard(ctk.CTkFrame):
    def __init__(self, master, title):
        super().__init__(master)

        self.configure(
            fg_color=colors.SIDEBAR,
            corner_radius=constants.CORNER_RADIUS
        )

        heading = ctk.CTkLabel(
            self,
            text=title,
            font=fonts.HEADING_FONT,
            text_color=colors.TEXT_PRIMARY
        )

        heading.pack(
            anchor="w",
            padx=constants.PADDING,
            pady=constants.PADDING
        )

        self.body = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        self.body.pack(
            fill="both",
            expand=True,
            padx=constants.PADDING,
            pady=(0, constants.PADDING)
        )