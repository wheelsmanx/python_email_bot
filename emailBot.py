# Python code to illustrate Sending mail 
# to multiple users 
# from your Gmail account 
import smtplib
 
# list of email_id to send the mail
li = ["justinshagerty@gmail.com"]
 
for i in range(len(li)):
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("wheelsmanx", "candice..")
    message = "Message_you_need_to_send"
    s.sendmail("wheelsmanx@gmail.com", li[i], message)
    s.quit