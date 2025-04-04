# 🗒️ Python Flask Notes App

A simple note-taking web app using Python and Flask. Notes are saved in a plain text file (`notes.txt`) with no database setup required.

## ✨ Features
- ➕ Add a note
- ❌ Delete a note
- 🗂️ Stores notes in `notes.txt`
- 🧑‍💻 Renders notes using a basic HTML template

## 📁 Folder Structure

app.py 
notes.txt 
templates
└── index.html 
README.md

## 💡 How It Works
- Notes are stored line-by-line in a local file
- Flask renders them dynamically
- Deleting removes a line by index

## ⚙️ Requirements
- Python 3.x
- Flask (`pip install flask`)
