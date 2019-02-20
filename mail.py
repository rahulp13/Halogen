import smtplib
 
def sendEmail(mailId):
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	server.login("your mail id", "your password")
	 
	msg = "YOU VIOLATED TRAFFIC RULES!!"
	
	try:
		server.sendmail("your mail id", mailId, msg)
		print("mail sent to : " + mailId)
		
	except:
		print("mail not sent")
			
	server.quit()
