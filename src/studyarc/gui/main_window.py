import customtkinter as ctk


from studyarc.gui.components.sidebar import Sidebar
from studyarc.gui.components.content import Content


class MainWindow(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("StudyArc")
        self.geometry("1000x700")

        sidebar = Sidebar(self)
        sidebar.pack(side="left", fill="y")

        content = Content(self)
        content.pack(side="right", expand=True, fill="both")
