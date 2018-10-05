import smtplib
 
def sendEmail(mailId):
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	server.login("your_email_id", "password")
	 
	msg = "YOU VIOLATED TRAFFIC RULES!!"
	
	try:
		server.sendmail("ff043095@gmail.com", mailId, msg)
		print("mail sent to : " + mailId)
		
	except:
		print("mail not sent")
			
	server.quit()
