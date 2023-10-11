from udp_server.udp_server import UDP_Server
from udp_client.udp_client import UDP_Client
import threading

server = UDP_Server(1)

server_thread = threading.Thread(target=server.start)
server_thread.start()

client = UDP_Client('localhost', 1)

while True:
    my_message = input('Введите сообщение:')
    if my_message != 'exit':
        client.send(my_message)

        response = client.receive()
        print(f'Пришел ответ от сервера:{response}')
    else:
        server.stop()
        server_thread.join()
        client.close()
        break