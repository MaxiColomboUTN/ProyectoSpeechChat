window_files = Toplevel()
    window_files.title("Agregar aplicaciones")
    window_files.configure(bg="#2C5364")
    window_files.geometry("500x300")
    window_files.resizable(0,0)
    main_window.eval(f'tk::PlaceWindow {str(window_files)} center')
    
    title_label = Label(window_files, text="Agrega una aplicacion", fg="white", bg="#2C5364", font=('Arial',15,'bold'))
    title_label.pack(pady=3)  
    
    name_label = Label(window_files, text="Nombre del la aplicacion", fg="white", bg="#2C5364", font=('Arial',11,'bold'))
    name_label.pack(pady=2)
    
    namefile_entry = Entry(window_files)
    namefile_entry.pack(pady=1) 
    
    path_label = Label(window_files, text="Directorio de la aplicacion", fg="white", bg="#2C5364", font=('Arial',11,'bold'))
    path_label.pack(pady=2)
    
    path_entry = Entry(window_files, width=50)
    path_entry.pack(pady=1) 
    
    save_button = Button(window_files, text="Guardar", bg= "#283c86", fg="white", font=('Arial',15,'bold'), width=8, height=1)#, command= add_apps)
    save_button.pack(pady=4)