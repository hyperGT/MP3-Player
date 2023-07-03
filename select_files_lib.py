class select_files:        
    def select_file():    
        file_index = song_listbox.curselection()
        if file_index:       
            play_audio(file_index[0])    
            
    def load_songs_from_folder(folder_path):
        songs = []
        song_listbox.delete(0, tk.END)
        for filename in os.listdir(folder_path):
            if filename.endswith(".mp3"):
                song_path = os.path.join(folder_path, filename)
                songs.append(song_path)
                song_listbox.insert(tk.END, filename)
        # Atualizar a lista de musicas        
        available_songs.clear()
        available_songs.extend(songs)
        
    def select_folder():
        folder_path = filedialog.askdirectory(initialdir="/", title="Select a folder")            
        if folder_path:
            load_songs_from_folder(folder_path)        



