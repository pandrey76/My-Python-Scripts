#!/usr/bin/env python
# -*- coding: utf-8 -*-


import codecs
import os.path

ifile_path = u"e:\Rabota\PythonProjects\set_to_low_registry\\temp_in.txt"

with codecs.open(ifile_path, "r", "cp1251") as g:
    spam = g.read()

#string = str("")
#for a in spam:
#    s = str(a)
#    if s.isupper() :
#        s = s.lower()
#    string  = string + s

spam = spam.lower()
ofile_path = u"e:\Rabota\PythonProjects\set_to_low_registry\\temp_out.txt"


with codecs.open(ofile_path, "w", "cp1251") as g:
    #g.write(string)
    g.write(spam)


#if __name__ == "__main__" :
