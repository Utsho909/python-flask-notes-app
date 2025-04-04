from flask import Flask, request, redirect, render_template

app = Flask(__name__)
NOTES_FILE = "notes.txt"

@app.route('/')
def index():
    if not open(NOTES_FILE, 'a'): pass
    with open(NOTES_FILE, 'r') as f:
        notes = f.readlines()
    return render_template('index.html', notes=notes)

@app.route('/add', methods=['POST'])
def add_note():
    note = request.form['note']
    with open(NOTES_FILE, 'a') as f:
        f.write(note + '\n')
    return redirect('/')

@app.route('/delete/<int:note_id>')
def delete_note(note_id):
    with open(NOTES_FILE, 'r') as f:
        notes = f.readlines()
    if 0 <= note_id < len(notes):
        del notes[note_id]
    with open(NOTES_FILE, 'w') as f:
        f.writelines(notes)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
