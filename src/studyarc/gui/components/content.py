import customtkinter as ctk

from studyarc.config import colors
from studyarc.config import fonts
from studyarc.config import constants

class Content(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.configure(fg_color=colors.BACKGROUND)

        title = ctk.CTkLabel(
            self,
            text="Welcome to StudyArc",
            font=fonts.TITLE_FONT,
            text_color=colors.TEXT_PRIMARY
        )

        subtitle = ctk.CTkLabel(
            self,
            text="Your AI-powered study companion",
            font=fonts.SUBHEADING_FONT,
            text_color=colors.TEXT_SECONDARY
        )
        description = ctk.CTkLabel(
            self,
            text="Start by creating your first note or explore the tools from the sidebar.",
            font=fonts.BODY_FONT,
            text_color=colors.TEXT_SECONDARY,
            wraplength=500,
            justify="center"
        )
        

        title.pack(pady=(
                constants.PADDING * 3,
                constants.WIDGET_SPACING
        )
        )
        subtitle.pack()
        description.pack(pady=(constants.SECTION_SPACING, 0))