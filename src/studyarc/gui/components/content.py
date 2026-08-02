import customtkinter as ctk

from studyarc.config import colors
from studyarc.config import fonts
from studyarc.config import constants

from studyarc.gui.pages.home_page import HomePage
from studyarc.gui.pages.notes_page import NotesPage
from studyarc.gui.pages.flashcards_page import FlashcardsPage
from studyarc.gui.pages.quiz_page import QuizPage
from studyarc.gui.pages.settings_page import SettingsPage

class Content(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.current_page = None
        self.pages = {
            "home": HomePage,
            "notes": NotesPage,
            "flashcards": FlashcardsPage,
            "quiz": QuizPage,
            "settings": SettingsPage
        }
        
        self.configure(fg_color=colors.BACKGROUND)

        self.show_page("home")
 

    def show_page(self, page):
        # Remove the currently displayed page
        if self.current_page is not None:
            self.current_page.destroy()

        # Find the requested page class
        page_class = self.pages[page]

        # Create the new page
        self.current_page = page_class(self)

        # Display it
        self.current_page.pack(expand=True, fill="both")
