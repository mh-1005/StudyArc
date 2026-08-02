import customtkinter as ctk
import os

from PIL import Image

from studyarc.config import colors
from studyarc.config import fonts
from studyarc.config import constants

class Sidebar(ctk.CTkFrame):
    def __init__(self, master, on_page_change):
        super().__init__(master)

        self.on_page_change = on_page_change

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

        buttons = {
            "Home": {
                "page": "home",
                "icon": "home.png"
            },
            "Notes": {
                "page": "notes",
                "icon": "notes.png"
            },
            "Flashcards": {
                "page": "flashcards",
                "icon": "flashcards.png"
            },
            "Quiz": {
                "page": "quiz",
                "icon": "quiz.png"
            },
            "Settings": {
                "page": "settings",
                "icon": "settings.png"
            }
        }

        self.buttons = {}
        self.icons = {}
        icon_path = os.path.join(
            "src",
            "studyarc",
            "assets",
            "icons"
    )

        for text, data in buttons.items():
            page = data["page"]
            icon_name = data["icon"]

            icon_file = os.path.join(
                icon_path,
                icon_name
            )
            icon_image = Image.open(icon_file)

            icon = ctk.CTkImage(
                light_image=icon_image,
                dark_image=icon_image,
                size=(20,20)
            )
            self.icons[page] = icon

            button = ctk.CTkButton(
                self,
                text=text,
                image=self.icons[page],
                compound="left",
                font=fonts.BUTTON_FONT,
                height=constants.BUTTON_HEIGHT,
                corner_radius=constants.CORNER_RADIUS,
                fg_color="transparent",
                hover_color=colors.HOVER,
                text_color=colors.TEXT_PRIMARY,
                anchor="w",
                command=lambda p=page: self.on_page_change(p)
            )
            button.pack(
                padx=constants.PADDING,
                pady=constants.WIDGET_SPACING,
                fill="x"
            )

            self.buttons[page] = button
    def set_active(self, page):
        for name, button in self.buttons.items():
            if name == page:
                button.configure(
                    fg_color=colors.ACTIVE
             )
            else:
                button.configure(
                    fg_color="transparent"
            )