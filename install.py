#!/usr/bin/python
import sys,os,shutil
from modules import ConfigReader

_HOME = os.environ['HOME']
_CURRENT_PATH = os.path.dirname(os.path.realpath(__file__))+"/"

config = ConfigReader.ConfigReader()

def copyrecursively(source_folder, destination_folder):
    for root, dirs, files in os.walk(source_folder):
        for item in files:
            src_path = os.path.join(root, item)
            dst_path = os.path.join(destination_folder, src_path.replace(source_folder, ""))
            if(".git" not in src_path):
                if os.path.exists(dst_path):
                    if os.stat(src_path).st_mtime > os.stat(dst_path).st_mtime:
                        shutil.copy2(src_path, dst_path)
                else:
                    shutil.copy2(src_path, dst_path)
            else:
                print "ignore file: "+src_path

        for item in dirs:

            src_path = os.path.join(root, item)
            dst_path = os.path.join(destination_folder, src_path.replace(source_folder, ""))
            if(".git" not in src_path):
                if not os.path.exists(dst_path):
                    os.mkdir(dst_path)
            else:
                print "ignore folder: "+src_path

gokachu_path = config.read("HOME").replace("$HOME", _HOME)
print "gokachu path:" + gokachu_path
if(not os.path.exists(gokachu_path)):
    os.mkdir(gokachu_path)
    print "done"
else:
    print "path " + gokachu_path + " already exist"

print "coping "+_CURRENT_PATH+"files into " + gokachu_path

copyrecursively(_CURRENT_PATH, gokachu_path)
print "done"
