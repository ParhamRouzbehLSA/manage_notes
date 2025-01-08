notes = []


def add_note(note):
    notes.append(note)


def view_notes():
    return notes


def delete_note(index):
    if 0 <= index < len(notes):
        del notes[index]


# Test the application
add_note("Buy groceries")
add_note("Read a book")
print("All notes:", view_notes())
delete_note(0)
print("Notes after deletion:", view_notes())


def search_notes(keyword):
    results = [note for note in notes if keyword in note]
    return results if results else "No notes found!"


# Test the new feature
add_note("Learn Python")
print("Search results for 'book':", search_notes("book"))
