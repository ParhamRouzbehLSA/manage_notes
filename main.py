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
