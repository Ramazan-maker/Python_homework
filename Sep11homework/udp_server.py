import socket


class UDP_Server:
    def __init__(self,port_number):
        self.port_number = port_number
        self.my_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.server_address = ('localhost', port_number)
        self.is_running = False

    def start(self):
        self.is_running = True
        self.my_socket.bind(self.server_address)
        print(f"Порт слушает входящие сообщение от {self.port_number}")
        while self.is_running:
            data, addr = self.my_socket.recvfrom(1024)
            message = data.decode(encoding="UTF-8")
            print(f'получено сообщение от {addr}: {message}')
            response = 'OK'
            self.my_socket.sendto(response.encode(), addr)

    def stop(self):
        self.is_running = False
        self.my_socket.close()
        print("Порт закрыт")

if __name__ == "__main__":
    port_number = 9900
    udp_server = UDP_Server(port_number)
    udp_server.start()