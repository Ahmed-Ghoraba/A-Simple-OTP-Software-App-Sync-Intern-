import random
import smtplib 
import webbrowser
from tkinter import *

###function to generate OTP

def generateOTP():
    randomcd = ''.join(str(random.randint(0, 9)) for i in range(8))
    return randomcd


snd = 'syncintern.task@gmail.com'
passcd = 'bniusjdqvxtiejxi'
cd = generateOTP()

###connecting to smtp gmail server

def redirect():
    webbrowser.open("https://www.youtube.com/watch?v=BBJa32lCaaY")
def connectingsnd():

    rec = recMail.get()
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(snd, passcd)
    sendingMail(rec, server)

### sending the mail and the message

def sendingMail(rec, server):
    msg = 'THE OTP FOR YOUR SYNC INTERN IS \n ' + cd
    server.sendmail(snd, rec, msg)
    server.quit()

### checking otp function
def checkOTP():
    if cd == cdEntry.get():
        accept = Label(otp, text='WELCOME, SUCCESSFUL VERIFICATION!', fg='green', font=('Arial', 20))
        accept.place(x=330, y=350)
        redirect()
    else:
        refuse = Label(otp, text='Unsuccessful Verification!', fg='red', font=('Arial', 20))
        refuse.place(x=230, y=350)

###TKINTER
otp = Tk()
otp.title('OTP Verification')
otp.geometry('980x560')
otp.config(bg='#CCCCCC')
#----GETTING MAIL----# 
mailMsg = Label(otp, text="E-Mail", justify=LEFT, bg='white', font=("Arial", 16))
mailMsg.place(x=200, y=40)

recMail = Entry(otp, text='mail.gmail.com', width=35, font=("Arial", 20), borderwidth=0)
recMail.place(x=340, y=40)
recM = StringVar()
#----SENDING OTP AND VERIFYING IT#
sendOTP = Button(otp, text="send OTP", width=8, height=1, font=("Arial", 20), borderwidth=0, bg="#000000", fg="white", command=connectingsnd)
sendOTP.place(x=550, y=150)

otpMsg = Label(otp, text="OTP", bg='white', font=('Arial', 16))
otpMsg.place(x=230, y=250)

cdEntry = Entry(otp, width=8, font=("Arial", 20), borderwidth=0)
cdEntry.place(x=520, y=250)
#----VERIFYING IT----#
verify = Button(otp, text="Verify", width=8, height=1, font=("Arial", 20), borderwidth=0, bg="#000000", fg="white",
                command=checkOTP)
verify.place(x=550, y=350)

otp.mainloop()
