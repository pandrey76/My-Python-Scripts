#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import os
from sys import argv, exit
import codecs


def construct_big_file_from_many_little(path, name, ext):

	for root, dirs, files in os.walk(path):
		with codecs.open(os.path.join(path, name) + '.' + ext, 'w', "utf-8") as result_file:
			count = 0
			while count <= len(files):
				try:
					full_file_path = os.path.join(path, str(count)) + '.' + ext
					with codecs.open(full_file_path, 'r', "cp1251") as f:
						print(full_file_path)
						file_content = f.read()

						marker = "#################"
						result_file.write(os.linesep)
						result_file.write(marker)
						result_file.write('    ')
						result_file.write(str(count) + '.' + ext)
						result_file.write('    ')
						result_file.write(marker)
						result_file.write(os.linesep)
						result_file.write(file_content)
						result_file.write(os.linesep)
						result_file.write(marker + marker)
						result_file.write(os.linesep)
				except FileNotFoundError as ex:
					print(ex)
				# except Exception as ex:
				# 	print(ex)
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
	
# Example: ConstructOneFileFromMany.py "/home/admin1/work/temp/" S-1-5-21-2772757386-1096924173-415189654-1002 reg
	construct_big_file_from_many_little(argv[1], argv[2], argv[3])
	
				
		
		
		
	

