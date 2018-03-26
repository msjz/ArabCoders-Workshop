import os
import string
def rename_files():
	files_list = os.listdir(r"D:\Study\1MAC\test\prank")
	saved_path = os.getcwd()
	print "Current working directory is: " + saved_path
	os.chdir(r"D:\Study\1MAC\test\prank")
	for file_name in files_list:
		os.rename(file_name, file_name.translate(None, "0123456789"))
	os.chdir(saved_path)


rename_files()