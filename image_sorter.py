from PIL import Image
from PIL.ExifTags import TAGS
import os
import subprocess

def main():
	rootDir = '/media/danny/Storage (Windows)/Pictures/DCIM'

	for dirName, subdirList, fileList in os.walk(rootDir):
		

		print "Directory: {}".format(dirName)

		for fileName in fileList:
			fullPath = '{}/{}'.format(dirName, fileName)
			if '.jpg' in fullPath.lower():
				date = get_exif(fullPath)['DateTimeOriginal'].split(' ')[0].replace(':', '-')

				move(fullPath, date)
				




def move(path, date):
	rootDir = '/media/danny/Storage (Windows)/Pictures/DCIM'

	#print path, date

	newDir = '/media/danny/Storage (Windows)/Pictures/DCIM/{}'.format(date)

	print newDir

	if(os.path.exists(newDir)):
		subprocess.call(['cp', path, newDir])

	else:
		subprocess.call(['mkdir', newDir])	

		subprocess.call(['cp', path, newDir])





def get_exif(path):
	exif = {}

	image = Image.open(path)

	data = image._getexif()

	for tag, value in data.items():
		decoded = TAGS.get(tag, tag)
		exif[decoded] = value

	return exif

if __name__=='__main__':
	main()