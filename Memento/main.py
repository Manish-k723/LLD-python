from Memento.history import History
from Memento.textEditor import TextEditor

text_editor = TextEditor()
text_history = History()

text_editor.write("Hello ")
text_editor.write("World")
text_history.save_state(text_editor.save())
print("1st ->", text_editor.get_text())
text_editor.write(", Good ")
text_editor.write("Bye!")
text_history.save_state(text_editor.save())
print("2nd ->", text_editor.get_text())
# text_history.get_history()
print("Start ->", text_editor.get_text())
text_editor.restore(text_history.undo())
print("Undo ->", text_editor.get_text())
# text_history.get_redo_history()
text_editor.restore(text_history.redo())
print("Redo ->", text_editor.get_text())
