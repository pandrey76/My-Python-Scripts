#!/usr/bin/env python
# -*- coding: UTF-8 -*-

#-------------------------------------------------------------------------------
# Name:        модуль1
# Purpose:
#
# Author:      Prapor
#
# Created:     05.12.2017
# Copyright:   (c) Prapor 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import subprocess
import os

#git clone "" ""


#os.system(r"Notepad.exe")

#ip = "localhost"
#proc = subprocess.Popen("ping -c2 %s" % ip, shell = True, stdout = subprocess.PIPE)
proc = subprocess.Popen("Notepad.exe", shell = False, stdout = subprocess.PIPE)


#out = proc.stdout.readlines()
#out = proc.communicate()
#proc.wait(10)
#proc.terminate()

#proc.kill()

def main():
    pass

if __name__ == '__main__':
    main()
