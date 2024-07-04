import imaplib
import email
from email.header import decode_header
import smtplib
from email.mime.text import MIMEText
from utils.quene import email_queue

# IMAP-Serverinformationen und Anmeldedaten
IMAP_SERVER  = "imap.gmail.com"
IMAP_PORT  = 993
EMAIL_ACCOUNT = "ludoko92@gmail.com"
EMAIL_PASSWORD = "app password "

# Verbindung zum POP3-Server herstellen
mail = imaplib.IMAP4_SSL(IMAP_SERVER, IMAP_PORT)
mail.login(EMAIL_ACCOUNT, EMAIL_PASSWORD)

def get_mails():
    # Posteingang auswählen
    mail.select("inbox")

    # Alle ungelesenen E-Mails abrufen
    status, messages = mail.search(None, 'UNSEEN')
    email_ids = messages[0].split()


    # E-Mails abrufen und in die Queue packen
    for email_id in email_ids:
        status, msg_data = mail.fetch(email_id, "(RFC822)")
        for response_part in msg_data:
            if isinstance(response_part, tuple):
                msg = email.message_from_bytes(response_part[1])
                subject, encoding = decode_header(msg["Subject"])[0]
                if isinstance(subject, bytes):
                    # Bei Bedarf dekodieren
                    subject = subject.decode(encoding if encoding else "utf-8")
                from_ = msg.get("From")

                # Nachrichtentext extrahieren
                if msg.is_multipart():
                    body = ""
                    for part in msg.walk():
                        content_type = part.get_content_type()
                        content_disposition = str(part.get("Content-Disposition"))

                        if "attachment" not in content_disposition:
                            try:
                                body = part.get_payload(decode=True).decode()
                                break
                            except:
                                pass
                else:
                    body = msg.get_payload(decode=True).decode()

                print("From:", from_)
                print("Subject:", subject)
                print("Body:", body)
                
                # E-Mail-Inhalt in die Queue packen
                email_queue.put((from_, subject, body))

    # Verbindung zum IMAP-Server schließen
    mail.logout()

