import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time

# Configurações de conexão SMTPS
smtp_server = 'smtp.gmail.com'
smtp_port = 587  # Porta para SMTP com TLS (STARTTLS)

# Informações de login
email_sender = 'seu_email@gmail.com'
email_password = 'sua_senha'

# Lista de destinatários (pode ser um único destinatário para todos os e-mails)
destinatarios = ['destinatario1@example.com', 'destinatario2@example.com']  # Adicione mais destinatários se desejar

# Configuração da mensagem
msg = MIMEMultipart()
msg['From'] = email_sender
msg['Subject'] = 'Assunto do E-mail'
body = 'Corpo do e-mail aqui'
msg.attach(MIMEText(body, 'plain'))

# Inicializar conexão SMTP
server = smtplib.SMTP(smtp_server, smtp_port)
server.starttls()  # Iniciar conexão TLS (STARTTLS)
server.login(email_sender, email_password)

# Simulação de envio de 200 commits
for i in range(1, 201):
    for destinatario in destinatarios:
        msg['To'] = destinatario
        msg.attach(MIMEText(f'Commit {i}: Mensagem do commit aqui', 'plain'))
        text = msg.as_string()
        server.sendmail(email_sender, destinatario, text)
        print(f'Commit {i} enviado para {destinatario}')
    time.sleep(1)  # Pausa de 1 segundo entre cada envio

# Encerrar conexão SMTP
server.quit()

print('Todos os commits foram enviados com sucesso!')
