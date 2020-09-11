import smtplib

class Send():
                
        def __init__(self):
                pass

        def GiveMail(self, mail):

                user = ''
                passwd = ''       
                smtpSer = 'smtp.gmail.com'      
                smtpPort = 465      

                
                to = ''
                subject = 'Daily Confirmation'
                msgBody = """
                Your Trades: \r\n\n

                """

                mesaage = 'To: ' + to + '\r\n'
                message = mesaage + 'subject: ' + subject + '\r\n'
                message = message + msgBody

                server = smtplib.SMTP_SSL(smtpSer, smtpPort)
                server.login(user, passwd)

                server.sendmail(user, to, message)
                server.close()
                print ("Mail was sent sucessfully...")
