#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import os
from sys import argv, exit



def construc_big_file_from_many_little(path, name, ext):
	root, dirs, files = os.walk(path)
	with open(os.path.join(path, name) + '.' + ext, 'w') as result_file:
		count = 0
		while count <= files.len():
			try:
				full_file_path = os.path.join(path, str(count)) + '.' + ext;
				with open(full_file_path, 'r') as f:
					print (full_file_path)
					file_content = f.read()
					
					marker = "#################"
					result_file.write(marker)
					result_file.write(str(count) + '.' + ext)
					result_file.write(marker)
					result_file.write(file_content)
					result_file.write(marker + marker)
					
					
			except FileNotFoundError(ex):
				print(ex)
			count = count + 1


if __name__ == '__main__':
		
	print(len(argv))
	for arg in argv:
		print(arg)
	if len(argv) < 4:
		print("Слишком мало параметров")
		exit(0)
	elif len(argv) > 4:
		print("Слишком много параметров")
		exit(0)
	
	construc_big_file_from_many_little(argv[1], argv[2], argv[3])  
	
				
		
		
		
	

