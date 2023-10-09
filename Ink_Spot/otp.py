from django.conf import settings
from twilio.rest import Client

class MessageHandler:
	phone_numer = None
	otp = None

	def __init__(self,phone_numer,otp) -> None:
		self.phone_numer = phone_numer
		self.otp = otp

	def send_otp_on_phone(self):
		client = Client(settings.ACCOUNT_SID, settings.AUTH_TOKEN)

		message = client.messages.create(
									     body= f' OTP is {self.otp} MOBOFIX Account verification',
									     from_= "+19164367626",
									     to=self.phone_numer

			)

