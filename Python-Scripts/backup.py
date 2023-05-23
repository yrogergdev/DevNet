import getpass
import telnetlib
import sys
import time
import os
import errno



#user = raw_input("Enter your Telnet Username ")
user = input("Enter your Username: ") # Ingresa el usuario de los equipos
password = getpass.getpass()  # Ingresa el password de los equipos
nombre_carpeta = input("Nombre la carpeta destino: ") #Ingresa el nombre de la carpeta que guardara los archivos

try:  #Crea un directorio con el nombre indicado en la ruta del script.
    os.mkdir(nombre_carpeta)  #Toma el nombre indica al inicio.
except OSError as e:  # Este codigo verifica que la carpeta no se este creada previamente
        if e.errno != errno.EEXIST:
               raise
f = open('iplist.txt')
all_ips = [x.rstrip() for x in f]
print(all_ips)
print("El archivo tiene: ",len(all_ips), end=" Direcciones IP\n")
for line in all_ips:
        print("Getting Configuration file from Switch " + (line))
        HOST = line        
        saveoutput = open(os.path.join(os.path.dirname(os.path.realpath(__file__)) + "\\" + nombre_carpeta, "Config_" + HOST), "w")
        tn = telnetlib.Telnet(HOST)
        tn.read_until(b"Username: ")
        tn.write(user.encode('ascii') + b"\n")
        if password:
            tn.read_until(b"Password: ")
            tn.write(password.encode('ascii') + b"\n")
        tn.write(b"enable\n")
        tn.write(b"rockwell\n")		
        tn.write(b"terminal length 0\n")
        tn.write(b"wr\n")
        tn.write(b"show startup-config\n")
        tn.write(b"exit\n")
        readoutput = tn.read_all()
        saveoutput = open(os.path.join(os.path.dirname(os.path.realpath(__file__)) + "\\" + nombre_carpeta, "Config_" + HOST), "w")
        # saveoutput = open("switch" + HOST, "w")
        # saveoutput = open("Config" + HOST + '.txt', "w")
        # saveoutput.write(readoutput)
        # saveoutput.close
