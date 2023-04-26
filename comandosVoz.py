import speech_recognition as sr #le colocamos un alias a nuestra libreria
import pyttsx3, pywhatkit #pyaudio no hace falta importarla

#Declaracion de variables
name = "Juan" #le colocamos un nombre, revisar nombre
listener = sr.Recognizer() #inicializamos Recognizer y lo asignamos a listener
engine = pyttsx3.init() # inicializamos nuestra libreria pyttsx3

<<<<<<< HEAD

engine.setProperty('rate',190)
engine.setProperty('volume',1.0)
=======
engine.setProperty('rate', 190)

engine.setProperty('volume', 1.0)
>>>>>>> 7682dd1 (funcionavozespañol2)

voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id) # colocamos la voz en español, se encuentra en la posicion 0 de voices.


#Declaracion de funciones
def hablar(text): #Va a hablar nuestra app, siempre y cuando le pasemos un parametro
    engine.say(text)
    engine.runAndWait()
def escuchar():
    try:
        with sr.Microphone() as source: #toma el microfono como fuente
            print("Escuchando...")
            pc = listener.listen(source) # le indicamos que escuche desde el microfono
<<<<<<< HEAD
            rec = listener.recognize_google(pc,language="es-AR")
=======
            rec = listener.recognize_google(pc, language="es-AR")
>>>>>>> 7682dd1 (funcionavozespañol2)
            rec = rec.lower() #transforma el texto en minusculas para evitar problemas
            if name in rec:
                rec = rec.replace(name, '') #remplaza el nombre por vacio, se hace esto para evitar que nuestro asistente repita lo que nosotros le decimos
    
    except:
        pass
    
    return rec

def ejecutar_SpeakIA():
    rec = escuchar()
    if 'reproduce' in rec: #si escucha la palabra reproduce, hara lo siguiente
        music = rec.replace('reproduce', '') # se hace esto para evitar que nuestro asistente repita lo que nosotros le decimos
        print("Reproduciendo " + music)
        hablar("Reproduciendo " + music)
        pywhatkit.playonyt(music) #abre youtube y reproduce lo que pidamos

if __name__ == '__main__':
    ejecutar_SpeakIA()