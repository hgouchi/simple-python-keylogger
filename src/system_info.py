import time

import requests
import socket
import platform

from settings import user, path, logs_file


class SysInfo:
    """Get information about the system"""
    def __init__(self):
        self.path = path
        self.logs = logs_file

    def get_system_info(self):
        system = f"{platform.system()} {platform.version()}"
        machine = platform.machine()

        datetime = time.ctime(time.time())

        try:
            public_ip = requests.get('https://api.ipify.org/').text
        except Exception:
            public_ip = "Couldn't get Public IP Address"

        private_ip = socket.gethostbyname(socket.gethostname())

        self.message = f"\n\nTime: {datetime}\nUsername: {user.split('/')[-1]}\nPublic IP: {public_ip}\n" + \
                    f"Private IP: {private_ip}\nSystem: {system}\nMachine: {machine}\n\n"

        self.write_system_info(self.message)

    def write_system_info(self, message):
        with open(self.path + self.logs_file, 'a') as f:
            f.write(message)

    def run(self):
        self.get_system_info()
