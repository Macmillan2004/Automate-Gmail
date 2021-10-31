import smtplib

sender_email = input(str("Enter Your Email"))
rec_email = input(str("Enter The Person Email"))
password = 'input(str("Enter Your Password"))'
message = input(str("Enter a message"))

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(sender_email, password)
print("Login success")
server.sendmail(sender_email, rec_email, message)
print("Email has been sent to ", rec_email)
