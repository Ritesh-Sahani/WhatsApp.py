# send whatsapp message using python
import pywhatkit as kit
phone_number=input("Enter phone number with country code:")
message=input("Enter your message to send:")
kit.sendwhatmsg_instantly(phone_number,message)