import customtkinter as ctk

from studyarc.config import colors
from studyarc.config import constants

from studyarc.gui.components.sidebar import Sidebar
from studyarc.gui.components.content import Content


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
        self.sidebar = Sidebar(self)
        self.sidebar.pack(side="left", fill="y")

        self.content = Content(self)
        self.content.pack(side="right", expand=True, fill="both")
