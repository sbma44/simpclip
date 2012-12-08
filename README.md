simpclip
========

Convenience utility for extracting and uploading snippets from the MPEGs of The Simpsons that I have sitting on my hard disk. Perhaps you'll find it useful for extracting clips from other stuff!

Dependencies: FFMPEG. I'm using a static build for OS X from 

	http://www.evermeet.cx/ffmpeg/

Example usage:

	python simpclip.py episode.avi 13:52 14:21

Uploads to an FTP server and returns a shortened URL. Set params in settings.py.