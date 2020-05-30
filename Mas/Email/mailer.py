from django.core import mail
from django.core.mail import EmailMessage
from django.core.mail.backends import smtp

import pandas as pd
import mimetypes


from .errors import SubjectError
from . import readfiles
from pathlib import Path
from Email.errors import FileReadingError


class PrepareMail(EmailMessage):
    def __init__(self, row, connection, from_email):
        to = self.process_to(row.to)
        attachments = self.process_attachments(row.attachments)
        subject = self.process_subject(row.subject)
        html_message = self.process_message(row.messages)
        if subject:
            self.content_subtype = 'html'
            super().__init__(subject=row.subject, from_email=from_email, cc=(from_email,),
                             to=to, attachments=attachments, connection=connection, body=html_message)

        else:
            raise SubjectError(f"Subject {self.subject} is invalid.")

    def process_attachments(self, attachments):
        file_list = list(map(lambda x: x.strip(),
                             attachments.split(",")))

        if file_list[0]:
            for i in file_list:
                yield (Path(i).name,
                       *readfiles.read_file(i.strip(), "rb", return_mime=True))

    def process_message(self, message_file):
        return readfiles.read_html(message_file.strip(), mode="r")

    def process_to(self, to):
        return tuple(map(lambda x: x.strip(), to.split(",")))

    def process_subject(self, subject):
        subject = subject.strip()
        return subject


class Mailer:
    def __init__(self, host, username, password, file_excel):

        self.file_excel = file_excel
        self.columns = ["to", "attachments", "subject", "messages"]
        self.smtp_backend = smtp.EmailBackend(
            host=host, port=587, username=username, password=password,
            use_tls=True, fail_silently=True, timeout=5)

    def send_mail(self):

        connection = self.smtp_backend

        connection.open()
        for index, row in pd.read_excel(self.file_excel,
                                        names=self.columns,
                                        keep_default_na=False,
                                        dtype=str,
                                        header=None, skiprows=[0]).iterrows():
            try:
                mailObj = PrepareMail(
                    row=row, connection=connection, from_email=connection.username)
                mailObj.send()
                yield {index+2: {"message": "success",
                                 "to": row.to}}
            except SubjectError as e:
                yield {index+2: {"message": "fail",
                                 "to": row.to,
                                 "error": e}}
            except FileReadingError as e:
                yield {index+2: {"message": "fail",
                                 "to": row.to,
                                 "error": e}}
            except :
                yield {index+2: {"message": "fail",
                                 "to": row.to,
                                 "error": "Unknown error"}}
        connection.close()
