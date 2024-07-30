import imaplib
import email
from email.header import decode_header
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time
from bs4 import BeautifulSoup

from utils.quene import email_queue

# IMAP-Serverinformationen und Anmeldedaten
IMAP_SERVER  = "imap.gmail.com"
IMAP_PORT  = 993
EMAIL_ACCOUNT = "ludoko92@gmail.com"
EMAIL_PASSWORD = "yhvtgvovavkbundk "

# Verbindung zum POP3-Server herstellen
mail = imaplib.IMAP4_SSL(IMAP_SERVER, IMAP_PORT)
mail.login(EMAIL_ACCOUNT, EMAIL_PASSWORD)

class Mailservices():

    def get_mails(self):
        # Posteingang auswählen
        mail.select("inbox")

        # Alle ungelesenen E-Mails abrufen
        status, messages = mail.search(None, 'UNSEEN')
        email_ids = messages[0].split()
        # E-Mails abrufen und in die Queue packen
        for email_id in email_ids:
            email_id = email_id.decode()
            status, msg_data = mail.fetch(email_id, "(BODY.PEEK[])")#
            for response_part in msg_data:
                if isinstance(response_part, tuple):
                    msg = email.message_from_bytes(response_part[1])
                    subject, encoding = decode_header(msg["Subject"])[0]
                    if isinstance(subject, bytes):
                        # Bei Bedarf dekodieren
                        subject = subject.decode(encoding if encoding else "utf-8")
                    from_ = msg.get("From")
                    to_ = msg.get("To")

                    # Nachrichtentext extrahieren
                    # Nachrichtentext dekodieren
                    body = ""
                    if msg.is_multipart():
                        for part in msg.walk():
                            content_type = part.get_content_type()
                            content_disposition = str(part.get("Content-Disposition"))

                            if content_disposition and "attachment" in content_disposition:
                                continue  # Anhänge ignorieren

                            if content_type == "text/plain":
                                payload = part.get_payload(decode=True)
                                charset = part.get_content_charset()
                                if charset:
                                    body += payload.decode(charset)
                                else:
                                    body += payload.decode()
                            elif content_type == "text/html":
                                payload = part.get_payload(decode=True)
                                charset = part.get_content_charset()
                                if charset:
                                    html = payload.decode(charset)
                                else:
                                    html = payload.decode()
                                
                                # HTML zu Text konvertieren
                                soup = BeautifulSoup(html, "html.parser")
                                body += soup.get_text()

                    else:
                        payload = msg.get_payload(decode=True)
                        charset = msg.get_content_charset()
                        if charset:
                            body = payload.decode(charset)
                        else:
                            body = payload.decode()

                        # HTML zu Text konvertieren, falls nötig
                        if msg.get_content_type() == "text/html":
                            soup = BeautifulSoup(body, "html.parser")
                            body = soup.get_text()

                    data = {
                        "id": email_id,
                        "from": from_,
                        "to": to_,
                        "Subject":subject,
                        "Body": body,
                    }
                    
                    
                    # E-Mail-Inhalt in die Queue packen
                    email_queue.put(data)
                    
    def mail_to_draft(self,final_mail,course):
        subject = course["subject"]
        # E-Mail Inhalt
        from_addr = course["to"]
        to_addr = course["from_"]
        subject = f"Re:{subject}"
        body = final_mail

        # E-Mail erstellen
        msg = MIMEMultipart()
        msg['From'] = from_addr
        msg['To'] = to_addr
        msg['Subject'] = subject
        msg["In-Reply-To"] = course["id"]
        msg["References"] = course["id"]
        msg.attach(MIMEText(body, 'plain'))

        # Hier sicherstellen, dass der Ordnername korrekt ist
        # Bei Gmail z.B. ist es "[Gmail]/Drafts"
        # Prüfen, welche Ordner verfügbar sind
        status, folders = mail.list()
        if status != 'OK':
            print("Fehler beim Abrufen der Ordnerliste.")
            exit()

        draft_folder = None
        for folder in folders:
            if "Draft" in folder.decode():
                draft_folder = folder.decode().split(' "/" ')[1]
                break

        if not draft_folder:
            print("Entwurfsordner nicht gefunden.")
            exit()
            
        mail.select(draft_folder)


        # E-Mail in den Entwürfen-Ordner speichern
        result, final_mail = mail.append(draft_folder, '\\Draft', imaplib.Time2Internaldate(time.time()), msg.as_string().encode('utf-8'))

        if result == 'OK':
            print("E-Mail als Entwurf gespeichert.")
        else:
            print(f"Fehler beim Speichern der E-Mail als Entwurf. {result}")

    def log_out(self):

        # Verbindung zum IMAP-Server schließen
        mail.logout()

