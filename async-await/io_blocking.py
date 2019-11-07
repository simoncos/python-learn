import socket

def server():
    s = socket.socket()

    host = socket.gethostname()
    port = 12349

    s.bind((host, port))
    s.listen(5)

    while True:
        conn, addr = s.accept()
        data = conn.recv(1024)	
        while data:
            print(data)
            data = conn.recv(1024)
        print("Data Received")
        conn.close()
        # break


import socket

def client():
    sock = socket.socket()

    host = socket.gethostname()
    sock.connect((host, 12349))

    data = b"Foo Bar" *10*1024*500 
    assert sock.send(data) 
    print("Data sent")

def client_nonb():
    sock = socket.socket()

    host = socket.gethostname()
    sock.connect((host, 12349))
    sock.setblocking(0) 

    data = b"Foo Bar" *10*1024*500 
    assert sock.send(data) 
    print("Data sent")