#by Gabriel
# Imports
import tkinter as tk
from tkinter import END, PhotoImage, filedialog
from tkinter import Scale

import pygame as pg
from pygame import mixer as mx

import os

"""Global variables guide

    para que serve as variaveis globais usadas?
    
    TODO: explain the global variables use

"""

# Global variables
available_songs = []
current_song = str(None)
    
"""Functions guide
    
    - play_song
        - add_song    
        - select_folder
            - load_songs
            
TODO: Implement the stop music function            
"""

"""GUI guide

TODO: arrumar a interface que nao ta boa
"""


# GUI     
# Graphic Window Interface
root = tk.Tk()
root.title("MP3 Player")
root.geometry("500x300")
root.config(bg="black", border=1)


# Initialze pygame mixer
pg.mixer.init()

# Add Song function
def add_song():
    global current_song, music_path
    
    song = filedialog.askopenfilename(initialdir='', title="Choose a song", filetypes=(('Mp3 Files', '*.mp3'), ))        
    music_path = song
        
    if music_path.endswith(".mp3"):
        available_songs.append(music_path)        
        
    # get only the name song
    song_name = os.path.basename(music_path)
    
    # remove the extension from the filename
    song_name = os.path.splitext(song_name)[0]
    
    song_listbox.insert(END, song_name)
    
    song_listbox.selection_set(0)
    current_song = available_songs[song_listbox.curselection()[0]] 

# Add many songs to playlist    
def add_many_songs():
    global current_song, available_songs, music_path
    songs = filedialog.askopenfilenames(initialdir="", title="Add multiple songs", filetypes=(('Mp3 Files', '*.mp3'), ))

    # loop through song list and pick the base filename
    for song in songs:
        music_path = song
        song_name = os.path.basename(music_path)
        song_name = os.path.splitext(song_name)[0]
        # Insert in the song list
        song_listbox.insert(END, song_name)
        available_songs.append(music_path)
        
        
    song_listbox.selection_set(0)
    current_song = available_songs[song_listbox.curselection()[0]] 
        
def select_folder():
    folder_path = filedialog.askdirectory()
    if folder_path:
        load_songs(folder_path)

# Load Song Function
def load_songs(self):
    global current_song, music_path
    
    music_path = self
    
    
    song_listbox.delete(0, END)        
    
    for song in os.listdir(music_path):        
        if song.endswith(".mp3"):            
            available_songs.append(song)
            
            
    for song in available_songs:
        song = song.replace(".mp3", "")
        song_listbox.insert(END, song)

    song_listbox.selection_set(0)
    current_song = available_songs[song_listbox.curselection()[0]] 

# Create Playlist Box
song_listbox = tk.Listbox(root, bg="black", fg="cyan", width=60, height=10, font=('ds-digital', 9), selectbackground='black', selectforeground="yellow")
song_listbox.pack()

# Get the project root path and the images directory
project_root = os.path.dirname(os.path.abspath(__file__))
image_folder = os.path.join(project_root, "..", "Images")

# Concatenate the images to image_folder and create the final path to reach the images
stop_btn_path = os.path.join(image_folder, "stop.png")
play_btn_path = os.path.join(image_folder, "play.png")
pause_btn_path = os.path.join(image_folder, "pause.png")
next_btn_path = os.path.join(image_folder, "next.png")
prev_btn_path = os.path.join(image_folder, "previous.png")

# Define Player Control Button Images
stop_btn_image = PhotoImage(file=stop_btn_path)
play_btn_image = PhotoImage(file=play_btn_path)
pause_btn_image = PhotoImage(file=pause_btn_path)
next_btn_image = PhotoImage(file=next_btn_path)
prev_btn_image = PhotoImage(file=prev_btn_path)

# Create Player Control Frame
control_frame = tk.Frame(root)
control_frame.pack()
control_frame.config(bg="black", border=5) 

# Create Menu 
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# Add Files Menu
add_files_menu = tk.Menu(menu_bar, tearoff=False)
menu_bar.add_cascade(label="File", menu=add_files_menu)

# Add song command
add_files_menu.add_command(label="Add Song", command=add_song)

# Add folder command
add_files_menu.add_command(label="Select Folder", command=select_folder)

# Add many songs command
add_files_menu.add_command(label="Add Multiple Song", command=add_many_songs)

# Read me function
def open_readme():
    # Open the README file in other window
    readme_window = tk.Toplevel(root)
    readme_window.title("Help Me!")
    
    #Create the text widget 
    readme_text = tk.Text(readme_window, bg='white', fg='black')
    readme_text.pack(fill='both', expand=True)

    # Open the README file and read it
    readme_path = os.path.join(project_root, "readme.txt")
    with open(readme_path, "r") as f:
        readme_content = f.read()
    
    # Insert the readme file content in text widget
    readme_text.insert("1.0", readme_content)
    
    readme_text.configure(state="disabled")

    
# Create a help menu
help_menu = tk.Menu(menu_bar, tearoff=False)
menu_bar.add_cascade(label="Help", menu=help_menu)

# Add the read me option
help_menu.add_command(label="Readme", command=open_readme)


               
# Play Function       
def play_song():
    global current_song, paused, music_path    
    
    # Strip out the directory and extension from the song name out of listbox             
    name_current_song = os.path.basename(current_song)
    name_current_song = os.path.splitext(name_current_song)[0]
    
    music = os.path.join(music_path, current_song)
        
    if not paused:       
        # Load the song and play it
        mx.music.load(music)
        pg.mixer.music.play(loops=0)          
        # Show the song name out of the listbox
        label.config(text=name_current_song)    
    else: 
        # Unpause the song
        mx.music.unpause()   
        paused = False

# Global variable paused
global paused
paused = False

# Pause Function            
def pause_song(is_paused):
    global paused
    
    paused = is_paused
    
    if paused:
        # Unpause
        pg.mixer.music.unpause()
        paused = False
    else:
        # Pause
        pg.mixer.music.pause()
        paused = True

# Stop the song function
def stop_song():
    pass

# Play the next song                
def next_song():
    global current_song, paused
    
    try:
        song_listbox.selection_clear(0, END) 
        song_listbox.selection_set(available_songs.index(current_song) + 1)       
        current_song = available_songs[song_listbox.curselection()[0]]
        play_song()
    except:
        pass

# Play the previous song    
def previous_song():
    global current_song, paused
    
    try:
        song_listbox.selection_clear(0, END)
        song_listbox.selection_set(available_songs.index(current_song) - 1)
        current_song = available_songs[song_listbox.curselection()[0]]
        play_song()
    except:
        pass    

# Adjust volume function
def adjust_volume(value):    
    volume = int(value) / 100.0 
    pg.mixer.music.set_volume(volume) 
    # Para alterar o texto do slider conforme a alteração do volume da música   
    volume_label.config(text=value)
    

# to show music name
label = tk.Label(root, text='', bg='black', fg="yellow", font=('ds-digital', 13))
label.pack(pady=10, side='top', anchor='center')

########################################################################
    
# Create Player Control Buttons

# play button
play_button = tk.Button(control_frame, image=play_btn_image, borderwidth=5, command=play_song, background="darkgray")
play_button.grid(row=0, column=3, padx=7, pady=10, sticky="w")
# pause button
pause_button = tk.Button(control_frame, image=pause_btn_image, borderwidth=5, command=lambda: pause_song(paused), background="darkgray")
pause_button.grid(row=0, column=2, padx=7, pady=10, sticky="w")
# stop button
stop_button = tk.Button(control_frame, image=stop_btn_image, borderwidth=5, command=stop_song, background="darkgray")
stop_button.grid(row=0, column=1, padx=7, pady=10, sticky="w")
# next button
next_button = tk.Button(control_frame, image=next_btn_image, borderwidth=5, command=next_song, background="darkgray")
next_button.grid(row=0, column=4, padx=7, pady=10, sticky="w")
# previous button
prev_button = tk.Button(control_frame, image=prev_btn_image, borderwidth=5, command=previous_song, background="darkgray")
prev_button.grid(row=0, column=0, padx=7, pady=10, sticky="w")

# Create Volume slider 
volume_slider = Scale(
    control_frame, from_=0, to=100, orient="horizontal", borderwidth=1, command=adjust_volume, showvalue=False
)
volume_slider.grid(row=1, column=0, columnspan=5, padx=5, pady=5)
# setup initial volume slider values
volume_slider.set(50)
mx.music.set_volume(0.5)

# Volume indicator
volume_label = tk.Label(control_frame, text="50", width=3, background="black", fg="yellow", font=("Times New Roman", 10))
volume_label.grid(row=1, column=3, padx=5, pady=5, sticky="e")


root.mainloop()