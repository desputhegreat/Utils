#client
import socket
import threading
import queue
import auth

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("127.0.0.1", 5000))

msgs = queue.Queue()

def msg_sender():
    while True:
        if not msgs.empty():
            print(msgs.get())
            msgs.task_done()
        message = input("> ")
        sock.send(message.encode())

def msg_reciever():
    while True:
        msg = sock.recv(1024)
        msgs.put(msg.decode())

auth.auth_client(sock)

msg_sender_thread = threading.Thread(target=msg_sender)
msg_reciever_thread = threading.Thread(target=msg_reciever)
msg_sender_thread.start()
msg_reciever_thread.start()