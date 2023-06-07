import speech_recognition as sr #le colocamos un alias a nuestra libreria
import pyttsx3, pywhatkit, wikipedia, datetime, pynput, keyboard, os #pyaudio no hace falta importarla
import subprocess as sub # nos permite ejecutar otros programas de nuestra computadora
from pygame import mixer

#Declaracion de variables
name = "Juan" #le colocamos un nombre, revisar nombre
listener = sr.Recognizer() #inicializamos Recognizer y lo asignamos a listener
engine = pyttsx3.init() # inicializamos nuestra libreria pyttsx3

voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id) # colocamos la voz en español, se encuentra en la posicion 0 de voices.
engine.setProperty('rate',145)
engine.setProperty('volume',1.0)

#Diccionario
sites={
            'google':'www.google.com.ar', #clave:valor
            'campus':'campus.frm.utn.edu.ar',
            'youtube':'youtube.com',
            'whatsapp':'web.whatsapp.com',
            'facebook':'facebook.com',
            'github':'github.com',
            'chatbot':'chat.openai.com'
        }
files={
            'notas':'Notas del proyecto.odt',
            'readme':'README.md',
            'prueba':'Prueba.pdf',
        }
programs = {
    'visual' : r'Visual Studio Code',
    'firefox' : r'Mozilla Firefox',
    'documentos' : r'LibreOffice Writer',
    'presentacion' : r'LibreOffice Impress',
    'calculadora' : r'Calculadora',
    'calendario' : r'Calendario',
    'configuracion' : r'Configuracion',
    'terminal' : r'Terminal',
    'editorDeTexto' : r'Editor de Texto'
}

#Declaracion de funciones
def hablar(text): #Va a hablar nuestra app, siempre y cuando le pasemos un parametro
    engine.say(text)
    engine.runAndWait()

def escuchar():
    try:
        with sr.Microphone() as source: #toma el microfono como fuente
            print("Escuchando...")
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
        elif 'alarma' in rec:  # nos programa una alarma
            alarma = rec.replace('alarma', '')
            alarma = alarma.strip() #strip elimina el espacio vacio de arriba para que la hora se pueda asignar correctamente
            hablar("Se estableció la alarma a las " + alarma + " horas")
            while True:
                if datetime.datetime.now().strftime('%H:%M') == alarma:  #obtiene la hora actual del sistema y la devuelve en un formato de cadena de texto.
                    # strftime devolverá una cadena que contiene las horas y los minutos actuales en formato de 24 horas. No se puede comparar un objeto de tipo fecha y hora con un string.
                    print("¡¡¡ Es hora de levantarse !!!")
                    mixer.init() 
                    mixer.music.load("alarma.mp3") # mixer nos permite cargar un sonido en formato .mp3
                    mixer.music.play()
                    #rec = escuchar()
                    #if 'parar alarma' in rec:
                    #    mixer.music.stop()
                    #    break
                    #f keyboard.read_key() == "p":
                    #if pynput.keyboard. == "p": # si lee la tecla s, la musica parará
                    if keyboard.read_key() == "s":
                        mixer.music.stop()
                    break
        elif 'abrir' in rec:
            for site in sites:
                if site in rec: # firefox se reemplaza por el navegador preferido
                    sub.call(f'firefox {sites[site]}', shell=True) #se llama a firefox y se abre la pagina web que hayamos indicado. shell se utiliza para informar que el comando se ejecuta como en la consola
                    hablar(f'Abriendo {site}')         
            for app in programs:
                if app in rec:
                    app_path = programs[app]  # Ruta absoluta del archivo
                    sub.Popen(['xdg-open', app_path]) 
                    hablar(f'Abriendo {app}')
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
            hablar('Nos vemos luego, que tengas un buen dia')
            break
        
        
if __name__ == '__main__':
    ejecutar_SpeakIA()