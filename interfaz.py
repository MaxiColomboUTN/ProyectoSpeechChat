import speech_recognition as sr #le colocamos un alias a nuestra libreria
import pyttsx3, pywhatkit, wikipedia, datetime,keyboard, os #pyaudio no hace falta importarla
import subprocess as sub #nos permite ejecutar otros programas de nuestra computadora
from pygame import mixer #para poder reproducir la musica de alarma
from tkinter import * #importamos todo, nos servira para poder hacer una interfaz grafica 
from PIL import Image, ImageTk
import threading as tr

main_window = Tk() #ventana principal donde estara todo
main_window.title("Speech Recognition") #titulo de la ventana

main_window.geometry("1000x800") #definimos el alto y ancho en pixeles
main_window.resizable(0,0) #indicamos que la ventana no permita agrandarse
main_window.configure(bg='#2c3e50') #definimos el color del fondo, utilizamos https://uigradients.com

#las triples comillas nos permiten mostrar un texto tal cual lo escribimos
comandos = """ 
    Comandos que puedes utilizar:
        - Reproduce..(cancion)
        - Busca..(algo)
        - Abre..(página web o app)
        - Alarma..(hora en 24Hrs)
        - Archivo..(nombre)
        - Termina
"""


label_title = Label(main_window, text="Speech Recognition AI", bg="#bdc3c7", fg="#283c86", font=('Times New Roman', 30, 'bold'))

label_title.pack(pady=10) #el label pasa a ser un bloque, y lo coloca en el centro, le da un espaciado de 10 px

canvas_comandos = Canvas(bg="#2b5876", height=220, width=260)
canvas_comandos.place(x=20,y=75)
canvas_comandos.create_text(90,80, text=comandos, fill="#F2F2F2", font='Arial 10')

text_info = Text(main_window, bg="#2b5876", fg="#F2F2F2")
text_info.place(x=20, y=300, height=470, width=262)

imagenIa = ImageTk.PhotoImage(Image.open("ia.jpg"))
window_photo = Label(main_window, image=imagenIa)
window_photo.pack(pady=5)

#Declaracion de variables
name = "Juan" #le colocamos un nombre, revisar nombre
listener = sr.Recognizer() #inicializamos Recognizer y lo asignamos a listener
engine = pyttsx3.init() # inicializamos nuestra libreria pyttsx3

voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id) # colocamos la voz en español, se encuentra en la posicion 0 de voices.
engine.setProperty('rate',145)
engine.setProperty('volume',1.0)

#Diccionario
#sites={
            #'google':'www.google.com.ar', #clave:valor
            #'campus':'campus.frm.utn.edu.ar',
            #'youtube':'youtube.com',
            #'whatsapp':'web.whatsapp.com',
            #'facebook':'facebook.com',
            #'github':'github.com',
            #'chatbot':'chat.openai.com'
        #}
#files={
#            'notas':'Notas del proyecto.odt',
#            'readme':'README.md',
#            'prueba':'Prueba.pdf',
#        }
#programs = {
#    'visual' : r"/usr/bin/code",
#    'firefox' : r"/snap/bin/firefox",
#    'documentos' : r"/usr/bin/libreoffice",
#    'calculadora' : r"/usr/bin/gnome-calculator",
#    'calendario' : r"/usr/bin/gnome-calendar",
#    'terminal' : r"/usr/bin/gnome-terminal",
#    'editor de texto' : r"/usr/bin/gedit",
#    'sudoku' : r"/usr/games/gnome-sudoku"
#}

site = dict()
files = dict()
programs = dict()

#Declaracion de funciones
def hablar(text): #Va a hablar nuestra app, siempre y cuando le pasemos un parametro
    engine.say(text)
    engine.runAndWait()

def leer_y_hablar(): #leera el texto de la caja de texto y hablara
    text = text_info.get("1.0", "end") #obtiene todo el texto de principio a fin
    hablar(text)
    
def escribirTexto(text_wiki):
    text_info.insert(INSERT, text_wiki) #inserta el texto en la caja de texto

def escuchar():
    try:
        with sr.Microphone() as source: #toma el microfono como fuente
            hablar("Te escucho")
            pc = listener.listen(source) # le indicamos que escuche desde el microfono
            rec = listener.recognize_google(pc,language="es-AR") #idioma español argentina
            rec = rec.lower() #transforma el texto en minusculas para evitar problemas
            if name in rec:
                rec = rec.replace(name, '') #remplaza el nombre por vacio, se hace esto para evitar que nuestro asistente repita lo que nosotros le decimos
    
    except:
        pass
    
    return rec

#Definimos funcion escribir
def escribir(f):
    hablar("¿Que quieres que escriba?")
    rec_write = escuchar()
    f.write(rec_write + os.linesep) #escribe en el archivo lo que decimos y cada vez que escribe, lo escribe debajo de cada linea con os.linesep
    f.close()
    hablar("Listo, puedes revisarlo")
    sub.Popen("notas.txt",shell=True) #guarda el archivo en el directorio del proyecto
    #sub.Popen(['xdg-open', file_path])

def abrir_archivos():
    global namefile_entry, pathf_entry #hacemos globales nuestras variables
    window_files = Toplevel()
    window_files.title("Agregar archivos")
    window_files.configure(bg="#2C5364")
    window_files.geometry("500x300")
    window_files.resizable(0,0)
    main_window.eval(f'tk::PlaceWindow {str(window_files)} center')
    
    title_label = Label(window_files, text="Agrega un archivo", fg="white", bg="#2C5364", font=('Arial',15,'bold'))
    title_label.pack(pady=3)  
    
    name_label = Label(window_files, text="Nombre del archivo", fg="white", bg="#2C5364", font=('Arial',11,'bold'))
    name_label.pack(pady=2)
    
    namefile_entry = Entry(window_files)
    namefile_entry.pack(pady=1) 
    
    pathf_label = Label(window_files, text="Directorio del archivo", fg="white", bg="#2C5364", font=('Arial',11,'bold'))
    pathf_label.pack(pady=2)
    
    path_entry = Entry(window_files, width=50)
    path_entry.pack(pady=1) 
    
    save_button = Button(window_files, text="Guardar", bg= "#283c86", fg="white", font=('Arial',15,'bold'), width=8, height=1, command= add_files)
    save_button.pack(pady=4)
    
def abrir_apps():
    global nameapps_entry, patha_entry 
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
    
    nameapps_entry = Entry(window_files)
    nameapps_entry.pack(pady=1) 
    
    patha_label = Label(window_files, text="Directorio de la aplicacion", fg="white", bg="#2C5364", font=('Arial',11,'bold'))
    patha_label.pack(pady=2)
    
    path_entry = Entry(window_files, width=50)
    path_entry.pack(pady=1) 
    
    save_button = Button(window_files, text="Guardar", bg= "#283c86", fg="white", font=('Arial',15,'bold'), width=8, height=1, command= add_apps)
    save_button.pack(pady=4)
    

def abrir_sitios():
    global namesite_entry, paths_entry 
    window_files = Toplevel()
    window_files.title("Agregar aplicaciones")
    window_files.configure(bg="#2C5364")
    window_files.geometry("500x300")
    window_files.resizable(0,0)
    main_window.eval(f'tk::PlaceWindow {str(window_files)} center')
    
    title_label = Label(window_files, text="Agrega una pagina web", fg="white", bg="#2C5364", font=('Arial',15,'bold'))
    title_label.pack(pady=3)  
    
    name_label = Label(window_files, text="Nombre de la pagina web", fg="white", bg="#2C5364", font=('Arial',11,'bold'))
    name_label.pack(pady=2)
    
    namesite_entry = Entry(window_files)
    namesite_entry.pack(pady=1) 
    
    paths_label = Label(window_files, text="URL de la pagina web", fg="white", bg="#2C5364", font=('Arial',11,'bold'))
    paths_label.pack(pady=2)
    
    path_entry = Entry(window_files, width=50)
    path_entry.pack(pady=1) 
    
    save_button = Button(window_files, text="Guardar", bg= "#283c86", fg="white", font=('Arial',15,'bold'), width=8, height=1, command= add_site)
    save_button.pack(pady=4)

def add_files():
    name_file = namefile_entry.get().strip() #cortamos espacios en blancos
    path_file = pathf_entry.get().strip()

    files[name_file] = path_file
    namefile_entry.delete(0,"end")
    pathf_entry.delete(0,"end")
    
def add_apps():
    name_app = nameapps_entry.get().strip() #cortamos espacios en blancos
    path_app = patha_entry.get().strip()

    programs[name_app] = path_app
    nameapps_entry.delete(0,"end")
    patha_entry.delete(0,"end")

def add_site():
    name_site = namesite_entry.get().strip() #cortamos espacios en blancos
    url_site = paths_entry.get().strip()

    site[name_site] = url_site
    namesite_entry.delete(0,"end")
    paths_entry.delete(0,"end")

def clock(rec):
    num = rec.replace('alarma', '')
    num = num.strip() #strip elimina el espacio vacio de arriba para que la hora se pueda asignar correctamente
    hablar("Se estableció la alarma a las " + num + " horas")
    if num[0] != '0' and len(num) < 5:
        num = '0' + num
    print(num)
    while True:
        if datetime.datetime.now().strftime('%H:%M') == num:  #obtiene la hora actual del sistema y la devuelve en un formato de cadena de texto.
            # strftime devolverá una cadena que contiene las horas y los minutos actuales en formato de 24 horas. No se puede comparar un objeto de tipo fecha y hora con un string.
            print("¡¡¡ Es hora de levantarse !!!")
            mixer.init() 
            mixer.music.load("alarma.mp3") # mixer nos permite cargar un sonido en formato .mp3
            mixer.music.play()
        else:
            continue #verificamos que la hora del sistema sea igual a la hora que solicitamos para la alarma
        if keyboard.read_key() == "s":
                mixer.music.stop()
                break
            
def ejecutar_SpeakIA():
    while True:  # nos permite que el asistente nos siga escuchando hasta que decidamos parar
        rec = escuchar()
        if 'reproduce' in rec: #si escucha la palabra reproduce, hara lo siguiente
            music = rec.replace('reproduce', '') # se hace esto para evitar que nuestro asistente repita lo que nosotros le decimos
            print("Reproduciendo " + music)
            hablar("Reproduciendo " + music)
            pywhatkit.playonyt(music) #abre youtube y reproduce lo que pidamos
        elif 'busca' in rec:  #busca en wikipedia
            busqueda = rec.replace('busca', '')
            wikipedia.set_lang("es") #colocamos wikipedia en español
            wiki = wikipedia.summary(busqueda, 1) #resume la informacion que buscamos de busqueda, el numero indica la cantidad de oraciones.
            print(busqueda + ": " + wiki)
            hablar(wiki) # nos comenta la informacion que ha buscado
            escribirTexto(busqueda + ": " + wiki)
            break #para que cuando busque algo, haga un break y nos muestre el texto, sino seguira escuchando y no podremos ver lo que nos escriba
        elif 'alarma' in rec:  # nos programa una alarma, se debe decir por ejemplo: "alarma 16"
            t = tr.Thread(target=clock, args=(rec,)) # usamos hilos para poder ejecutar otras cosas a pesar de programar una alarma
            t.start()
        elif 'abrir' in rec:
            for site in sites:
                if site in rec: # firefox se reemplaza por el navegador preferido
                    sub.call(f'firefox {sites[site]}', shell=True) #se llama a firefox y se abre la pagina web que hayamos indicado. shell se utiliza para informar que el comando se ejecuta como en la consola
                    hablar(f'Abriendo {site}')         
            for app in programs:
                if app in rec:
                    hablar(f'Abriendo {app}')
                    sub.Popen(programs[app])
        elif 'archivo' in rec:
            for file in files:
                if file in rec:
                    file_path = files[file]  # Ruta absoluta del archivo
                    sub.Popen(['xdg-open', file_path]) # es un comando en Ubuntu que se utiliza para abrir archivos con la aplicación predeterminada asociada a su tipo de archivo.
                    hablar(f'Abriendo {file}')
        elif 'escribe' in rec:
            try:
                with open("nota.txt",'a') as f: #crea el archivo, 'a' es de agregar, para agregar texto, f es un alias 
                    escribir(f) # le pasamos f, que sera nuestro archivo nota.txt
                    
            except FileNotFoundError as e: #si el archivo no está creado, ocurrira una excepcion
                file = open("nota.txt",'w') #como el archivo no esta creado, se crea en esta linea
                escribir(file) #se llama a la funcion escribir de vuelta para que podamos escribir en nota.txt, pero le pasamos file
        
        elif 'finaliza' in rec:
            hablar('Hasta luego, que tengas un buen dia')
            break

#definicion de funciones para botones
#REVISAR
def cambiar_voz(id):
    engine.setProperty('voices', voices[id].id) 
    engine.setProperty('rate', 145) # velocidad de la voz
    engine.setProperty('volume', 1.0) # volumen de la voz    
    hablar("Hola soy la voz de tu asistente virtual")
    
def mexican_voice():
    cambiar_voz(26)

def spanish_voice():
    cambiar_voz(26)

def english_voice():
    cambiar_voz(26)

#CREACION DE BOTONES
#REVISAR
button_voice_mx = Button(main_window, text="Voz México", fg="white", bg="#0f9b0f", font=("Arial", 12, "bold"), command=mexican_voice)
button_voice_mx.place(x=750, y=75, width=150, height=30)

button_voice_es = Button(main_window, text="Voz España", fg="white", bg="#c31432", font=("Arial", 12, "bold"), command=spanish_voice)    
button_voice_es.place(x=750, y=120,width=150,height=30)

button_voice_us = Button(main_window, text="Voz EEUU", fg="white", bg="#0082c8", font=("Arial", 12, "bold"), command=english_voice)    
button_voice_us.place(x=750, y=165,width=150,height=30)    

button_listen = Button(main_window, text="Escuchar", fg="white", bg="#4CA1AF", font=("Arial", 15, "bold"), width=20, height=2, command=ejecutar_SpeakIA)
button_listen.pack(pady=10)  

button_speak = Button(main_window, text="Hablar", fg="white", bg="#D39D38", font=("Arial", 12, "bold"), command=leer_y_hablar)
button_speak.place(x=750, y=210, width=150, height=30)

button_add_files = Button(main_window, text="Agregar Archivos", fg="white", bg="#4A569D", font=("Arial", 12, "bold"), command=abrir_archivos)
button_add_files.place(x=725, y=255, width=200, height=30)

button_add_apps = Button(main_window, text="Agregar Aplicaciones", fg="white", bg="#4A569D", font=("Arial", 12, "bold"), command=abrir_apps)
button_add_apps.place(x=725, y=300, width=200, height=30)

button_add_pages = Button(main_window, text="Agregar sitios web", fg="white", bg="#4A569D", font=("Arial", 12, "bold"), command=abrir_sitios)
button_add_pages.place(x=725, y=345, width=200, height=30)


main_window.mainloop() #indicamos que todo lo que se encuentre antes de mainloop se ejecute, vendria a ser nuestra funcion main 

