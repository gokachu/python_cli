#!/usr/bin/python
import sys
import os
from modules import ConfigReader
_HOME = os.environ['HOME']

config = ConfigReader.ConfigReader()

print config.read("HOME").replace("$HOME", _HOME)


print sys.argv[1]
