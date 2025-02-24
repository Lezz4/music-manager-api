# ui/app.py
import tkinter as tk
from tkinter import messagebox, ttk
import requests

API_URL = "http://127.0.0.1:8000/songs/"


class MusicManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Music Manager")
        self.root.geometry("500x400")

        self.setup_ui()
        self.fetch_songs()

    def setup_ui(self):
        self.tree = ttk.Treeview(self.root, columns=("ID", "Title", "Artist", "Album", "Year"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Title", text="Title")
        self.tree.heading("Artist", text="Artist")
        self.tree.heading("Album", text="Album")
        self.tree.heading("Year", text="Year")
        self.tree.pack(fill=tk.BOTH, expand=True)

        self.add_button = tk.Button(self.root, text="Add Song", command=self.add_song)
        self.add_button.pack(pady=5)

    def fetch_songs(self):
        response = requests.get(API_URL)
        if response.status_code == 200:
            songs = response.json()
            for song in songs:
                self.tree.insert("", "end",
                                 values=(song["id"], song["title"], song["artist"], song["album"], song["year"]))

    def add_song(self):
        self.add_window = tk.Toplevel(self.root)
        self.add_window.title("Add Song")

        tk.Label(self.add_window, text="Title:").grid(row=0, column=0)
        tk.Label(self.add_window, text="Artist:").grid(row=1, column=0)
        tk.Label(self.add_window, text="Album:").grid(row=2, column=0)
        tk.Label(self.add_window, text="Year:").grid(row=3, column=0)

        self.title_entry = tk.Entry(self.add_window)
        self.artist_entry = tk.Entry(self.add_window)
        self.album_entry = tk.Entry(self.add_window)
        self.year_entry = tk.Entry(self.add_window)

        self.title_entry.grid(row=0, column=1)
        self.artist_entry.grid(row=1, column=1)
        self.album_entry.grid(row=2, column=1)
        self.year_entry.grid(row=3, column=1)

        tk.Button(self.add_window, text="Save", command=self.save_song).grid(row=4, column=1)

    def save_song(self):
        data = {
            "id": len(self.tree.get_children()) + 1,  # Temporary ID assignment
            "title": self.title_entry.get(),
            "artist": self.artist_entry.get(),
            "album": self.album_entry.get(),
            "year": int(self.year_entry.get()),
        }
        response = requests.post(API_URL, json=data)
        if response.status_code == 200:
            messagebox.showinfo("Success", "Song added successfully!")
            self.tree.insert("", "end", values=(data["id"], data["title"], data["artist"], data["album"], data["year"]))
            self.add_window.destroy()
        else:
            messagebox.showerror("Error", "Failed to add song.")


if __name__ == "__main__":
    root = tk.Tk()
    app = MusicManagerApp(root)
    root.mainloop()
