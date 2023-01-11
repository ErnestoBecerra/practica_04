import telnetlib
from ftplib import FTP
import subprocess

user = "rcp"
pas = "rcp"


			
	
def generarArchivo():
	print("\nIngrese direcion IP del router:")
	host = input()
	tn = telnetlib.Telnet()
	tn.open(host)
	tn.read_until(b"User: ")
	tn.write(user.encode("ascii")+b"\r\n")
	tn.read_until(b"Password: ")
	tn.write(pas.encode("ascii")+b"\r\n")
	tn.write(b"en\r\n")
	tn.write(b"config\r\n")
	tn.write(b"copy run start\r\n")
	tn.write(b"exit\r\n")
	tn.write(b"exit\r\n")
	tn.write(b"exit\r\n")
	tn.read_all()
	tn.close()
	print("|--------------------------------------|")
	print("| Se ha creado el archivo exitosamente |")
	print("|--------------------------------------|")
	print("\n")
	


def extraerArchivo():
	print("\nIngrese la direcion ip del router:")
	host = input()
	#print("\nProporcione el nombre del route:")
	name = 'rcppr4'
	tn = telnetlib.Telnet()
	tn.open(host)
	tn.read_until(b"User: ")
	tn.write(user.encode("ascii")+b"\r\n")
	tn.read_until(b"Password: ")
	tn.write(pas.encode("ascii")+b"\r\n")
	tn.write(b"en\r\n")
	tn.write(b"config\r\n")
	tn.write(b"service ftp\r\n")
	tn.write(b"exit\r\n")
	tn.write(b"exit\r\n")
	tn.write(b"exit\r\n")
	tn.read_all()
	tn.close()
	
	ftp = FTP (host)
	ftp.login(user,pas)
	ftp.retrbinary('RETR startup-config',open(name , 'wb').write)
	ftp.quit()
	print("|--------------------------------------------|")
	print("|     Archivo startup-config extraido        |")
	print("|--------------------------------------------|")
	print("\n")



def importarArchivo():
	print("\nProporcione la ip para realizar la conexion con el router:")
	host = input()
	#print("\nProporcione el nombre del route:")
	name = 'rcppr4'
	tn = telnetlib.Telnet()
	tn.open(host)
	tn.read_until(b"User: ")
	tn.write(user.encode("ascii")+b"\r\n")
	tn.read_until(b"Password: ")
	tn.write(pas.encode("ascii")+b"\r\n")
	tn.write(b"en\r\n")
	tn.write(b"config\r\n")
	tn.write(b"service ftp\r\n")
	tn.write(b"exit\r\n")
	tn.write(b"exit\r\n")
	tn.write(b"exit\r\n")
	tn.read_all()
	tn.close()
	
	ftp = FTP (host)
	ftp.login(user,pas)
	f = open(name,'rb')
	ftp.storbinary('STOR startup-config',f)
	f.close()
	ftp.quit()
	print("|----------------------------------------|")
	print("|      Archivo startup-config enviado    |")
	print("|----------------------------------------|")
	print("\n")
	
	
def menu():
	print("|..................................................|")
	print("|   Practica 4 - Sistema de administracion         |")
	print("|..................................................|")
	print("\n")
	print("\n")
	print("1. Generar el archivo de configuración")
	print("2. Extraer el archivo de configuración.")
	print("3. Importar el archivo de configuración.")
	opc = input("Seleccione una opcion:")
	if opc =="1":
		generarArchivo()
	if opc == "2":
		extraerArchivo()
	if opc == "3":
		importarArchivo()
	
	if opc > "3" or opc < "1":
		exit()
	

menu()
