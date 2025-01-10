import json

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


def save_notes_to_file(filename="notes.json"):
    with open(filename, "w") as file:
        json.dump(notes, file)


def load_notes_from_file(filename="notes.json"):
    global notes
    try:
        with open(filename, "r") as file:
            notes = json.load(file)
    except FileNotFoundError:
        notes = []


def sort_notes():
    global notes
    notes.sort()


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
load_notes_from_file()
add_note("Call the doctor")
save_notes_to_file()
print("Notes saved to file and reloaded:", view_notes())

add_note("Buy groceries")
add_note("Call the doctor")
add_note("Read a book")
print("Before sorting:", view_notes())
sort_notes()
print("After sorting:", view_notes())
