#!/usr/bin/python3

import time

import requests
import socket
import platform

from settings import user, path, logs_file


class SysInfo:
    """Get information about the system"""
    def get_system_info(self):
        system = f"{platform.system()} {platform.version()}"
        machine = platform.machine()

        datetime = time.ctime(time.time())

        try:
            public_ip = requests.get('https://api.ipify.org/').text
        except:
            public_ip = "Couldn't get Public IP Address"

        private_ip = socket.gethostbyname(socket.gethostname())

        self.msg = f"Time: {datetime}\nUsername: {user.split('/')[-1]}\nPublic IP: {public_ip}\n" + \
                    f"Private IP: {private_ip}\nSystem: {system}\nMachine: {machine}\n\n"

        self.write_system_info(self.msg)

    @staticmethod
    def write_system_info(message):
        with open(path + logs_file, 'w') as f:
            f.write(message)

    def run(self):
        self.get_system_info()
