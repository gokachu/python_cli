#!/usr/bin/python
import sys

if(len(sys.argv) == 3):
    _HOME = sys.argv[1]
    _PACKAGE = sys.argv[2]
    print _HOME + _PACKAGE
else:
    print "Err"
