#by Gabriel
# Imports
import tkinter as tk
from tkinter import END, PhotoImage, filedialog
from tkinter import Scale

import pygame as pg
from pygame import mixer as mx

import os

pg.init()

# Global variables
available_songs = []
current_song = str(None)
paused = False

# GUI     
# Graphic Window Interface
root = tk.Tk()
root.title("MP3 Player")
root.geometry("500x300")
root.config(bg="black", border=1)



# Logica do programa

def load_songs():
    global current_song        
    
    songlist.delete(0, END)
    root.directory = filedialog.askdirectory()

    for song in os.listdir(root.directory):
        name, extention = os.path.splitext(song)
        if extention.endswith(".mp3"):
            available_songs.append(song)
    # para cada musica disponivel, insira-a e seu nome
    for song in available_songs:
        songlist.insert(END, song)

    songlist.selection_set(0)
    current_song = available_songs[songlist.curselection()[0]]      



# pausar a reprodução
def pause_song():
    global paused
    mx.music.pause()
    paused = True
               
# Tocar a musica            
def play_song():
    global current_song, paused                 
        
    if not paused: # se não estiver tocando        
        mx.music.load(os.path.join(root.directory, current_song))
        pg.mixer.music.play()    
        #label.config(text=current_song)    
    else: 
        mx.music.unpause()   
        paused = False
        
                
# logica para a seleção da prox musica
def next_song():
    global current_song, paused
    
    try:
        songlist.selection_clear(0, END) 
        songlist.selection_set(available_songs.index(current_song) + 1)       
        current_song = available_songs[songlist.curselection()[0]]
        play_song()
    except:
        pass
    
    # logica para a seleção da musica anterior
def previous_song():
    global current_song, paused
    
    try:
        songlist.selection_clear(0, END)
        songlist.selection_set(available_songs.index(current_song) - 1)
        current_song = available_songs[songlist.curselection()[0]]
        play_song()
    except:
        pass    

# Function para alterar o volume durante a musica
def adjust_volume(value):    
    volume = int(value) / 100.0 
    pg.mixer.music.set_volume(volume) 
    
    # Para alterar o texto do slider conforme a alteração do volume da música   
    volume_label.config(text=value)
    
    
# Obter os caminhos absolutos das imagens
play_btn_path = os.path.join("play.png")
pause_bnt_path = os.path.join("pause.png")
next_btn_path = os.path.join("next.png")
prev_btn_path = os.path.join("previous.png")
# Usar as imagens para os botões
play_btn_image = PhotoImage(file=play_btn_path)
pause_btn_image = PhotoImage(file=pause_bnt_path)
next_btn_image = PhotoImage(file=next_btn_path)
prev_btn_image = PhotoImage(file=prev_btn_path)

# Menu "Files" na parte de cima
menubar = tk.Menu(root)
root.config(menu=menubar)
# Criar o menu
organise_menu = tk.Menu(menubar, tearoff=False)
organise_menu.add_command(label="Select Folder", command=load_songs)
menubar.add_cascade(label="File", menu=organise_menu)
  
# List box | Caixa que contem a lista de musicas
songlist = tk.Listbox(root, bg="black", fg="cyan", width=100, height=14, font=('ds-digital', 9), border=2)
songlist.pack()

# MUSIC NAME SHOW
label = tk.Label(root, text='', bg='black', fg="yellow", font=('ds-digital', 13))
#label.pack(pady=10, side='top', anchor='center')

# quadro de controle(onde ficam os botões)
control_frame = tk.Frame(root)
control_frame.pack()
control_frame.config(bg="black", border=5) 


# Volume slider section
volume_slider = Scale(
    control_frame, from_=0, to=100, orient="horizontal", borderwidth=1, command=adjust_volume, showvalue=False
)
volume_slider.grid(row=0, column=4, padx=5, pady=5)

#Ao iniciar o programa, trave o valor do volume em 50
volume_slider.set(50)
mx.music.set_volume(0.5)

volume_label = tk.Label(control_frame, text="50", width=3, background="black", fg="yellow", font=("Times New Roman", 10))
volume_label.grid(row=0, column=5, padx=5, pady=5, sticky="e")



# Botões de controle de musica - next e previous
play_button = tk.Button(control_frame, image=play_btn_image, borderwidth=5, command=play_song, background="darkgray")
pause_button = tk.Button(control_frame, image=pause_btn_image, borderwidth=5, command=pause_song, background="darkgray")
next_button = tk.Button(control_frame, image=next_btn_image, borderwidth=5, command=next_song, background="darkgray")
prev_button = tk.Button(control_frame, image=prev_btn_image, borderwidth=5, command=previous_song, background="darkgray")
# Posicionamento dos botões na janela de controle
play_button.grid(row=0, column=2, padx=7, pady=10, sticky="w")
pause_button.grid(row=0, column=1, padx=7, pady=10, sticky="w")
next_button.grid(row=0, column=3, padx=7, pady=10, sticky="w")
prev_button.grid(row=0, column=0, padx=7, pady=10, sticky="w")

root.mainloop()