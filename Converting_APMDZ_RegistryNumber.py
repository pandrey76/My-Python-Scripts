#!/usr/bin/env python
# -*- coding: UTF-8 -*-

#-------------------------------------------------------------------------------
# Name:        модуль1
# Purpose:
#
# Author:      Prapor
#
# Created:     20.09.2017
# Copyright:   (c) Prapor 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import codecs
import re
import os.path


def main(infile):
   outfile = r"e:\Numbers_out"
   with codecs.open(outfile, "w", "cp1251") as b:

       if os.path.exists(infile):
            with codecs.open(infile, "r", "cp1251") as g:
                s = g.read()
                __RezultList = re.split(r"\n", s)
                for i,s in enumerate(__RezultList):
#                    print( s #+ ", ")
#                        if c == "№" or c == " " or c == "," :
                    pPattern = re.compile( r"(330Б-\d\d\d\d\d\d)(?:\W\w)*", re.S | re.L)
                    M1 = pPattern.search(s)
                    if M1:
                        print (M1.group(1))
                        #(headerString, number) = pPattern.subn(M1.group(1) + MACRO, headerString, 1)
                        s = M1.group(1)
                        __RezultList[i] = s
                        b.write("№" + s + ", ")
                        print(s)
                print(i)
       else:
          raise IOError("File Not Exist")
          #print (__RezultList)
       b.close()
       return 0


if __name__ == '__main__':
    file = r"e:\Номера"
    main(file)
