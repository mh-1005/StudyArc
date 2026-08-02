import customtkinter as ctk

from studyarc.config import constants, fonts
from studyarc.config import colors

from studyarc.gui.components.card import Card
from studyarc.gui.components.content_card import ContentCard


class HomePage(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        title = ctk.CTkLabel(
            self,
            text="Welcome to StudyArc",
            font=fonts.TITLE_FONT,
            text_color=colors.TEXT_PRIMARY
        )

        subtitle = ctk.CTkLabel(
            self,
            text="Your AI-powered study companion",
            font=fonts.BODY_FONT,
            text_color=colors.TEXT_SECONDARY
        )

        title.pack(pady=(60, 10))
        subtitle.pack()

        actions_frame = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        actions_frame.pack(
            pady=(40,20)
        )

        new_note = Card(
            actions_frame,
            "🗒️ New Note"
        )

        new_note.pack(
            side="left",
            padx=10
        )

        new_note.configure(
           width=constants.ACTION_CARD_WIDTH,
           height=constants.ACTION_CARD_HEIGHT
        )

        new_note.pack_propagate(False)


        flashcards = Card(
            actions_frame,
            "📚 Flashcards"
        )

        flashcards.pack(
            side="left",
            padx=10
        )

        flashcards.configure(
            width=constants.ACTION_CARD_WIDTH,
            height=constants.ACTION_CARD_HEIGHT
        )

        flashcards.pack_propagate(False)


        quiz = Card(
            actions_frame,
            "🧩 Quiz"
        )

        quiz.pack(
            side="left",
            padx=10
        )

        quiz.configure(
            width=constants.ACTION_CARD_WIDTH,
            height=constants.ACTION_CARD_HEIGHT
        )

        quiz.pack_propagate(False)

        recent_activity = ContentCard(
            self,
            "Recent Activity"
        )

        recent_activity.configure(
            width=constants.CARD_WIDTH,
            height=constants.ACTIVITY_CARD_HEIGHT
        )

        recent_activity.pack(
            pady=(20, 10)
        )

        recent_activity.pack_propagate(False)

        activity_text = ctk.CTkLabel(
            recent_activity.body,
            text="No recent activity yet.",
            font=fonts.BODY_FONT,
            text_color=colors.TEXT_SECONDARY
        )

        activity_text.pack(
            anchor="w"
        )

        stats = ContentCard(
            self,
            "Statistics"
        )

        stats.configure(
            width=constants.CARD_WIDTH,
            height=constants.STATS_CARD_HEIGHT
        )

        stats.pack(
            pady=(10, 20)
        )

        stats.pack_propagate(False)

        notes_label = ctk.CTkLabel(
            stats.body,
            text="Notes: 0",
            font=fonts.BODY_FONT,
            text_color=colors.TEXT_SECONDARY
        )

        notes_label.pack(
            anchor="w",
            pady=3
        )


        flashcards_label = ctk.CTkLabel(
            stats.body,
            text="Flashcards: 0",
            font=fonts.BODY_FONT,
            text_color=colors.TEXT_SECONDARY
        )

        flashcards_label.pack(
            anchor="w",
            pady=3
        )


        quiz_label = ctk.CTkLabel(
            stats.body,
            text="Quizzes: 0",
            font=fonts.BODY_FONT,
            text_color=colors.TEXT_SECONDARY
        )

        quiz_label.pack(
            anchor="w",
            pady=3
        )