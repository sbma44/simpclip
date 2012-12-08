import sys, os, ftplib, re
from shorten import shorten
import bitlyapi
from settings import *

def main():
	(filename, start, end) = sys.argv[1:4]

	# create working filenames
	filename_parts = filename.split('/')[-1].split('.')
	filename_parts.insert(-1, 'extract')
	extract_filename = '/tmp/%s' % '.'.join(filename_parts)
	filename_parts[-2] = 'final'
	filename_parts[-1] = 'mov' # infuriatingly important if we're going to play well with Apple
	final_filename = re.sub(r'\s','_','/tmp/%s' % '.'.join(filename_parts))

	# calculate time in format ffmpeg expects
	(start_min, start_sec) = map(lambda x: int(x), start.split(':'))
	(end_min, end_sec) = map(lambda x: int(x), end.split(':'))
	duration_sec = ((end_min*60) + end_sec) - ((start_min*60) + start_sec)

	# extract & compress the clip
	ffmpeg_command = "ffmpeg -y -ss 00:%02d:%02d.0 -t 00:%02d:%02d.0 -i \"%s\" -r 30000/1001 -b:v 180k -bt 180k -vcodec libx264 -profile:v baseline -acodec libmp3lame -b:a 64k -r 24 -async 1 \"%s\"" % (start_min, start_sec, (duration_sec/60), (duration_sec%60), filename, final_filename)
	os.system(ffmpeg_command)

	# upload to server	
	ftp = ftplib.FTP(FTP_SERVER, FTP_USER, FTP_PASSWORD)
	ftp.cwd(FTP_DIRECTORY)
	ftp.storbinary('STOR %s' % final_filename.split('/')[-1], open(final_filename, 'rb'))

	# clean up
	for fn in (extract_filename, final_filename):
		# os.remove(fn)
		pass
	

	bitly = bitlyapi.BitLy(BITLY_USER, BITLY_APIKEY)
	print bitly.shorten(longUrl="%s%s" % (URL_PREFIX, final_filename.split('/')[-1]))['url']

if __name__ == '__main__':
	main()