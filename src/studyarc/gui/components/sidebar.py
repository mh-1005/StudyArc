import customtkinter as ctk

from studyarc.config import colors
from studyarc.config import fonts
from studyarc.config import constants

class Sidebar(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.configure(
            width=constants.SIDEBAR_WIDTH,
            fg_color=colors.SIDEBAR
        )

        title = ctk.CTkLabel(
            self,
            text="StudyArc",
            font=fonts.TITLE_FONT,
            text_color=colors.TEXT_PRIMARY 
        )

        title.pack(
            pady=(
                constants.PADDING + 10,
                constants.SECTION_SPACING
            )
            )

        buttons = [
            "🏠 Home",
            "📝 Notes",
            "🃏 Flashcards",
            "❓ Quiz",
            "⚙️ Settings"
            ]

        for text in buttons:
            button = ctk.CTkButton(
                self,
                text=text,
                font=fonts.BUTTON_FONT,
                height=constants.BUTTON_HEIGHT,
                corner_radius=constants.CORNER_RADIUS,
                fg_color="transparent",
                hover_color=colors.HOVER,
                text_color=colors.TEXT_PRIMARY,
                anchor="w"
            )
            button.pack(
                padx=constants.PADDING,
                pady=constants.WIDGET_SPACING,
                fill="x"
            )
