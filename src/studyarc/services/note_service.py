from studyarc.models.note import Note


class NoteService:

    def __init__(self):
        self.notes = []

    def add_note(self, note: Note):
        self.notes.append(note)

    def get_notes(self):
        return self.notes

    def update_note(self, old_note, new_note):
        index = self.notes.index(old_note)
        self.notes[index] = new_note

    def delete_note(self, note):
        self.notes.remove(note)
