import json
from datetime import datetime

notes = []


def add_note(note):
    notes.append(note)


def view_notes():
    return notes


def delete_note(index):
    if 0 <= index < len(notes):
        del notes[index]


def search_notes(keyword):
    results = [note for note in notes if keyword in note]
    return results if results else "No notes found!"


def sort_notes():
    global notes
    notes.sort(key=lambda note: note['content'])


def add_note_with_date(content):
    note = {"content": content, "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
    notes.append(note)


def save_notes_to_file_with_date(filename="notes.json"):
    with open(filename, "w") as file:
        json.dump(notes, file)


def load_notes_from_file_with_date(filename="notes.json"):
    global notes
    try:
        with open(filename, "r") as file:
            notes = json.load(file)
    except FileNotFoundError:
        notes = []


# Test the application
add_note("Buy groceries")
add_note("Read a book")
print("All notes:", view_notes())
delete_note(0)
print("Notes after deletion:", view_notes())

# Test the new feature
add_note("Learn Python")
print("Search results for 'book':", search_notes("book"))

# Test persistence
load_notes_from_file_with_date()
add_note_with_date("Learn Python")
save_notes_to_file_with_date()
print("Notes saved with date:", view_notes())


add_note_with_date("Buy groceries")
add_note_with_date("Call the doctor")
add_note_with_date("Read a book")
print("Before sorting:", view_notes())
sort_notes()
print("After sorting:", view_notes())

