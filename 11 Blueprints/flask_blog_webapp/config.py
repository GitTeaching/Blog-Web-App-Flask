import os

class Config:
	SECRET_KEY = '4c99e0361905b9f941f17729187afdb9'

	SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'

	MAIL_SERVER = 'smtp.googlemail.com'
	MAIL_PORT = 587
	MAIL_USE_TLS = True
	MAIL_USERNAME = os.environ.get('EMAIL_USER')
	MAIL_PASSWORD = os.environ.get('EMAIL_PASS')