                        #Uso de librerias
# request: biblioteca que nos permite hacer solicitudes HTTP a sitios web y API's
# wikipedia: buscar, obtener y analizar contenido de Wikipedia
# pywhatkit: biblioteca de terceros que se utiliza para automatizar tareas relacionadas con la informática. Esta biblioteca permite hacer cosas como enviar mensajes de texto a través de WhatsApp, buscar información en Google y YouTube, etc
# email.message: biblioteca estándar que se utiliza para crear, manipular y enviar emails
# smtplib: biblioteca estándar que se utiliza para enviar correos electrónicos a través del protocolo SMTP
# decouple: se utiliza para separar la configuración de una aplicación de su código fuente. Esta biblioteca permite almacenar la configuración de la aplicación en un archivo de configuración externo, en lugar de incrustarla en el código fuente. Si queremos modificarlo, modificamos el archivo, no el codigo fuente.

import wikipedia
import pywhatkit as kit
import smtplib
import requests
from email.message import EmailMessage  
from decouple import config

#Definiremos funciones que utilizaremos mas adelante para hacer funcionar el proyecto

def buscarEnWikipedia(query): # query: este parámetro representa la cadena de búsqueda que se utilizará para buscar información en Wikipedia
    busqueda = wikipedia.summary(query, resumenEnOraciones = 5) # resumenEnOraciones devolvera lo que hayamos buscado en la web, en 5 oraciones
    return busqueda

def saberMiDireccionIp():
    direccion_ip = requests.get('https://api64.ipify.org?format=json').json #Revisar
    return direccion_ip["ip"]

def enviarWhatsapp(numero, mensaje):
    kit.sendwhatmsg_instantly(f"+54{numero}", mensaje) # cadena de texto que representa el número de teléfono al que se desea enviar el mensaje, La letra f al principio de la cadena indica que se utiliza un formato de cadena de texto f-string para combinar la variable numero con el prefijo del número de teléfono.
    
def busquedaGoogle(query):
    kit.search(query)
    
def reproducirYoutube(video): # el parametro "video" represnta la URL de video completa o solo el ID de video.
    kit.playonyt(video)   
    
def ConsejoAleatorio():  #REVISAR FUNCION
    #resultadoBusquedaConsejo = requests.get("http://javascripts.astalaweb.net/Mensajes/Consejos%20diarios%20aleatorios.htm").json()
    #return resultadoBusquedaConsejo['clave']['consejo'] # devuelve el valor asociado con la clave 'consejo' en el diccionario 'clave' que se encuentra en el diccionario 'res'. Este valor es el consejo aleatorio que se ha obtenido de la API.

def abrirEditorTexto():

def abrirDiscord():
    
def abrirConsola():

def abrirCamara():

def abrirCalculadora():
    
def abrirCalendario():

def abrirPapelera():

def abrirConfiguracion():