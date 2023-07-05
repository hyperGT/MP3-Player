import tkinter as tk
from tkinter import filedialog
from tkinter import Scale
from tkinter import Listbox
import pygame
import os

pygame.init()


def play_audio(song_index):
    pygame.mixer.music.load(available_songs[song_index])
    pygame.mixer.music.play()


def pause_audio():
    pygame.mixer.music.pause()


def continue_audio():
    pygame.mixer.music.unpause()


def adjust_volume(value):
    volume = int(value) / 100.0
    pygame.mixer.music.set_volume(volume)


def select_file(song_listbox):
    file_index = song_listbox.curselection()
    if file_index:
        play_audio(file_index[0])  # Sound index


def select_folder():
    folder_path = filedialog.askdirectory(initialdir="/", title="Selecione uma pasta")
    if folder_path:
        load_songs_from_folder(folder_path)


def load_songs_from_folder(folder_path, song_listbox):
    songs = []
    song_listbox.delete(0, tk.END)
    for filename in os.listdir(folder_path):
        if filename.endswith(".mp3"):
            song_path = os.path.join(folder_path, filename)
            songs.append(song_path)
            song_listbox.insert(tk.END, filename)
    # Atualize a lista de músicas disponíveis
    available_songs.clear()
    available_songs.extend(songs)

root = tk.Tk()
root.title("MP3 Player")
root.geometry("400x300")

volume_slider = Scale(
        root,
        from_=0,
        to=100,
        orient="horizontal",
        label="Volume",
    command=adjust_volume,
)
volume_slider.pack(pady=10)

song_listbox = Listbox(root)
song_listbox.pack(pady=10)

load_songs_from_folder(root, song_listbox=song_listbox)
select_file(song_listbox)

select_button = tk.Button(root, text="Selecionar Música", command=select_file)
select_button.pack(pady=10)

pause_button = tk.Button(root, text="Pause", command=pause_audio)
pause_button.pack(pady=10)

resume_button = tk.Button(root, text="Continue", command=continue_audio)
resume_button.pack(pady=10)

select_folder_button = tk.Button(
    root, text="Selecionar Pasta", command=select_folder
)
select_folder_button.pack(pady=10)

root.mainloop()

available_songs = []