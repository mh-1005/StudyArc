import customtkinter as ctk

from studyarc.config import colors
from studyarc.config import fonts
from studyarc.config import constants


class Card(ctk.CTkFrame):
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
            text_color=colors.TEXT_PRIMARY,
            anchor="center"
            
        )

        heading.pack(
            expand=True,
            pady=constants.PADDING
        )
        

      