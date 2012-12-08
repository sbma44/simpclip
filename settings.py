FFMPEG = '/usr/local/bin/ffmpeg'

FTP_SERVER = 'yourserver.com'
FTP_USER = 'login'
FTP_PASSWORD = 'password_goes_here'
FTP_DIRECTORY = '/public_html/video/'
URL_PREFIX = 'http://yourserver.com/video/'

BITLY_USER = 'your_bitly_username'
BITLY_APIKEY = 'your_bitly_API_key'

try:
	from local_settings import *
except:
	pass