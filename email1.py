import smtplib

sender_email = 'testm5062@gmail.com'
rec_email = input(str("Enter The Person Email"))
password = 'nilandasuper'
message = input(str("Enter a message"))

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(sender_email, password)
print("Login success")
server.sendmail(sender_email, rec_email, message)
print("Email has been sent to ", rec_email)
