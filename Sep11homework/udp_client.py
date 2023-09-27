import socket

class UDP_Client:
    def __init__(self,server_address,server_port):
        self.server_address = server_address
        self.server_port = server_port
        self.my_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def send(self,message):
        self.my_socket.sendto(message.encode(), (self.server_address,self.server_port))

    def recieve(self):
        data, addr = self.my_socket.recvfrom(1024)
        response = data.decode('utf-8')
        return response

    def close(self):
        self.my_socket.close()

if __name__ == "__main__":

    udp_client = UDP_Client('localhost', 1)
    message_to_send = input('Введите что-хотите отправить серверу: ')
    udp_client.send(message_to_send)

    response = udp_client.recieve()
    print(f"Получен ответ от сервера {response}")
    udp_client.close()
