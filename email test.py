import smtplib

def sendEmail(to, content):
    sender_email = 'singhchitwan08@gmail.com'
    sender_password = 'nkfd lyty clpn pphx'
    
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(sender_email, sender_password)
    server.sendmail(sender_email, to, content)
    server.close()

sendEmail('choudharysukhveer2810@gmail.com' , 'helo ji ,kya hai mtlb call vall nhi hote hai smjh nnhi ata hai kuch')