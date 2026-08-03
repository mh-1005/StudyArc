from studyarc.models.note import Note


class NoteService:

    def __init__(self):
        self.notes = []

    def add_note(self, note: Note):
        self.notes.append(note)

    def get_notes(self):
        return self.notes
