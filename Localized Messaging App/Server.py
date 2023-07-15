"""
Author: Daniel Mitchell
Last Date Modified: 07/09/2023
Purpose: A simple messaging solution for individuals on the same network to be able to communicate with each other
"""
import socket
import time
import threading

host = socket.gethostbyname(socket.gethostname())
port = 65432

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host,port))

write_lock = threading.Lock()
send_signal = threading.Semaphore(1)
send_signal.acquire()
to_send = ("user", "message")

cltconns = {}
httpconns = []

CLT_IDFYR = "x43110W051D"
http_init = "HTTP/1.1 200 OK\nContent-Type: text/html\n\n<html><head><title>Twiggs App</title><body><h1>Twiggs App</h1></body></html>"
#<body><h1>Twiggs App</h1></body>

def connection_handler():
    global httpconns
    global CLT_IDFYR
    
    while True:
        server.listen()
        conn, addr = server.accept()
        init_req = conn.recv(1024).decode()
    
        if init_req == CLT_IDFYR:
            print(f"\nidentified {conn} as client")
            t = threading.Thread(target=clt_handler, args=(conn,))
            t.start()
        else:
            print(f"\nidentified {conn} as http")
            httpconns.append(conn)
            t = threading.Thread(target=http_handler, args=(conn,))
            t.start()

def clt_handler(clt_conn):
    global httpconns
    global cltconns
    global to_send
    clt_conn.send(b"USER_REQ")
    print("\nSent user request")
    user = clt_conn.recv(1024).decode()
    cltconns.update({clt_conn: user})
    print(f"Received and updated username: {user}")
    while True: 
        #try conn.recv, if good move on, if unsuccessful break;
        msg = clt_conn.recv(1024)
        if len(msg) > 0:
            write_lock.acquire()
            to_send = (cltconns[clt_conn], msg)     # sign with username so http_handler knows the username
            print("Changed to_send")
            send_signal.release(len(httpconns))
            time.sleep(0.5)     # disallow socket connections with too many requests at once (max one request/500ms)
                                # buffer to allow threads to finish critical section, as well as to not overcrowd
            write_lock.release()
        #if there are 5 http_handler threads then release 5 and the threads will call acquire and decrement it to 0
        #(if you call acquire right after initiating the semaphore)
        

def http_handler(http_conn):
    time.sleep(1)
    http_conn.send(http_init.encode())
    #http_conn.send(b"<html></head>\n<body><h1>Twiggs App</h1></body></html>\n")
    while True:
        send_signal.acquire()      # hold thread till a message is ready to be sent
        print("Semaphore acquired.")
        user = to_send[0]
        msg = to_send[1]

        http_msg = f"""<html><body><p><strong>{user}: </strong>{msg.decode()}</p></body></html>"""
        http_conn.send(http_msg.encode())
        print("Sent transmission")
        time.sleep(0.1)     # buffer

# command handling to be added soon

def main():
    connection_handler()

main()