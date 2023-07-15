"""
Author: Daniel Mitchell
Last Date Modified: 07/09/2023
Purpose: A simple messaging solution for individuals on the same network to be able to communicate with each other
"""
import socket
import time
import logging

host = '10.0.0.181'
port = 65432

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

CLT_IDFYR = "x43110W051D"

def main():
    global CLT_IDFYR
    print("Welcome to the Twiggs App!")
    while True:
        username = input("\nPlease enter your username: ")

        if username.isalnum() and (len(username) < 15):
            break
        print("_________________________________________________________________")
        print(f"\nSorry, {username} is not a valid username.\nUsernames must be alphanumeric, and less than 15 characters.")

    client.connect((host,port))
    client.send(CLT_IDFYR.encode())
    print("\nSuccesfully connected to server and sent identifier")
    data = client.recv(1024)   # Hang till server sends user request
    print(f"Received user reqest: {data}")
    time.sleep(0.1)     # buffer
    client.send(username.encode())
    print("Sent username")
    print(f"Great! Now all you have to do is enter {host}:{port} in your browser, then start typing below!")

    while True:
        msg = input("Type your message... ")
        client.send(msg.encode())
main()