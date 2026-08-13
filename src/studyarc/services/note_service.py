from studyarc.models.note import Note


class NoteService:

    def __init__(self):
        self.notes = []
        self._listeners = []

    def add_listener(self, callback):
        self._listeners.append(callback)

    def remove_listener(self, callback):
        if callback in self._listeners:
            self._listeners.remove(callback)

    def _notify(self):
        for callback in self._listeners:
            callback()

    def add_note(self, note: Note):
        self.notes.append(note)
        self._notify()

    def get_notes(self):
        return self.notes

    def update_note(self, old_note, new_note):
        index = self.notes.index(old_note)
        self.notes[index] = new_note
        self._notify()

    def delete_note(self, note):
        self.notes.remove(note)
        self._notify()
