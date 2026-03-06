#client
import socket
import threading
import queue

user = input("Please enter your username: ")
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("127.0.0.1", 5000))

msgs = queue.Queue()
def auth():
    while True:    
        sock.send(user.encode())
        responce = sock.recv(1024).decode()
        if responce == "Login":
            password = input("Enter your password: ")
            sock.send(password.encode())
            responce = sock.recv(1024).decode()
            if responce == "Logged in":
                print("Successfully Logged in!")
                break
            elif responce == "Incorrect":
                password = input("Incorrect Password. Try again: ")
                sock.send(password.encode())
            else:
                print("Something went wrong")
                break    
        elif responce == "Register":
            password = input("Enter a strong password: ")
            sock.send(password.encode())
            print("Successfully Registered!")
            break
        else:
            print("Something went wrong")     
            break

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
auth()
msg_sender_thread = threading.Thread(target=msg_sender)
msg_reciever_thread = threading.Thread(target=msg_reciever)
msg_sender_thread.start()
msg_reciever_thread.start()