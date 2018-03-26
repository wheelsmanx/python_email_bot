#By Justin Hagerty
#Date: 3/18/2018
# Python code to illustrate Sending mail 
# Notes include how to make this script a service in ubuntu


import smtplib
import time 
 
# list of email_id to send the mail
li = ["justinshagerty@gmail.com"]

for i in range(len(li)):
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("", "")
    message = "This message sent to you because this service was restarted"
    s.sendmail("wheelsmanx@gmail.com", li[i], message)
    s.quit

def sendEmailTo(sendFromEmailAddress, sendToEmailAddress, functionMessage)
    emailServer = smtplib.SMTP('smtp.gmail.com',587)
    emailServer.starttls()
    emailServer.login("", "")
    emailServer.sendmail(sendFromEmailAddress, sendToEmailAddress, functionMessage)
    emailServer.quit

def sendEmailToList(sendFromEmailAddress, sendToEmailList, functionMessage)
    for i in range(len(li)):
        emailServer = smtplib.SMTP('smtp.gmail.com', 587)
        emailServer.starttls()
        emailServer.login("","")
        emailServer.sendmail(sendFromEmailAddress, sendToEmailList[i], functionMessage)
        emailServer.quit

def getEmailList():
    emailList = []
    print("to exit type exit") 
    while(true):
        userInput = input("add user:")
        if(userInput == "exit"):
            break
        else:
            emailList.append(userInput)
            
        
