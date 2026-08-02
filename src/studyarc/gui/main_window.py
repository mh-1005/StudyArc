import customtkinter as ctk

from studyarc.config import colors
from studyarc.config import constants

from studyarc.gui.components.sidebar import Sidebar
from studyarc.gui.components.content import Content
from studyarc.gui.components.topbar import TopBar


class MainWindow(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("StudyArc")
        self.geometry(
            f"{constants.WINDOW_WIDTH}x{constants.WINDOW_HEIGHT}"
        )
        self.configure(
            fg_color=colors.BACKGROUND
        )
        self.sidebar = Sidebar(self,self.change_page)
        self.sidebar.pack(side="left", fill="y")
        self.sidebar.set_active("home")

        self.main_area = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        self.main_area.pack(
            side="right",
            expand=True,
            fill="both"
        )

        self.topbar = TopBar(self.main_area)

        self.topbar.pack(
            side="top",
            fill="x"
        )

        self.content = Content(self.main_area)

        self.content.pack(
            expand=True,
            fill="both"
        )


    def change_page(self, page):

            self.sidebar.set_active(page)

            self.content.show_page(page)

            self.topbar.set_title(page.capitalize())
