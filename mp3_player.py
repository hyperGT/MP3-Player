# Para criar a interface gráfica | colocar no código que vai conter somente a interface
import tkinter as tk
# Manter nesse código | filedialog serve para abrir a caixa de seleção de arquivos
from tkinter import filedialog

# importando as bibliotecas PYGAME para reproduzir o audio e OS para ter acesso a comandos e diretorios
import pygame
import os 

pygame.init()

def play_mp3(filename): 
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()
    
def select_file():    
    file_path = filedialog.askopenfilename(initialdir="/", title="Select a MP3 file", filetypes=(("Arquivos MP3", "*.mp3"),))
    if file_path: 
        play_mp3(file_path) 
        
root = tk.Tk()
root.title("MP3 Player")           
root.geometry("400x200")

select_button = tk.Button(root, text="Select a MP3 file", command=select_file)
select_button.pack(pady=50, padx=50)

root.mainloop()