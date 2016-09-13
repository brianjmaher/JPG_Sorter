# a simple script that sorts .jpg images in the same directory as it
# into folders by date taken

# Dependencies: PIL library

from PIL import Image
import os, shutil

# gets the directory of the file
dir_path = os.path.dirname(os.path.realpath(__file__))

# takes the path of an imagine and returns the date as a string: YYYY-MM-DD
def get_date_taken(path):
	try:
		return Image.open(path)._getexif()[36867].split(" ")[0].replace(":","-")
	except KeyError:
		return "0000-00-00"

# iterates through jpg images in the directory and copies them to a
# subdirectory named YYYY-MM-DD
for filename in os.listdir(dir_path):
	if ".jpg" in filename.lower() or ".jpeg" in filename.lower():
		print filename
		date = get_date_taken(filename)
		if date not in os.listdir(dir_path):
			os.mkdir(date)
		shutil.copyfile(filename, "%s/%s" % (date, filename))`