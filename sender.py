import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

class sender:
    def __init__(self):
        self.sender_email = "ih772891@gmail.com"
        self.smtp_server = "smtp.gmail.com"
        self.smtp_port = 587  # Change it according to your SMTP server settings
        self.username = "ih772891@gmail.com"
        self.password = "onlg umby snlv wpos"  # Provide the actual password
        self.receiver_email = "21-se-020@student.hitecuni.edu.pk"
        self.subject = "Server Setup detail"
        self.message = "Your server is created successfully. Here is a screenshot for your server details."
        self.attachment_path = "screenshort/serversetup.png"  # Provide the full path to your attachment file

    def send_email(self):
        try:
            # Create message container - the correct MIME type is multipart/mixed.
            msg = MIMEMultipart()
            msg['Subject'] = self.subject
            msg['From'] = self.sender_email
            msg['To'] = self.receiver_email

            # Add message body
            msg.attach(MIMEText(self.message, 'plain'))

            # Open the file to be sent
            with open(self.attachment_path, 'rb') as attachment:
                # Add file as application/octet-stream
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(attachment.read())

            # Encode file in ASCII characters to send by email    
            encoders.encode_base64(part)
            
            # Add header as key/value pair to attachment part
            part.add_header('Content-Disposition', f'attachment; filename= {self.attachment_path}')

            # Add attachment to message and convert message to string
            msg.attach(part)
            text = msg.as_string()

            # Connect to SMTP server and send email.
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()
                server.login(self.username, self.password)
                server.sendmail(self.sender_email, self.receiver_email, text)
            print("Email sent successfully!")
        except Exception as e:
            print("An error occurred:", e)

# Example usage:
#email_sender = EmailSender()
#email_sender.send_email()
