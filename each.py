import sys
import os
import subprocess
import argparse
import time

parser = argparse.ArgumentParser()
parser.add_argument("-a", "--all", action="store_true")
parser.add_argument("-d", "--dir", action="store_true")
parser.add_argument("-f", "--file", action="store_true")
parser.add_argument("-v", "--verbose", action="store_true")
parser.add_argument("-r", "--recursive", action="store_true")
parser.add_argument("directory", nargs="*")
parser.add_argument("command", nargs="*")

args = parser.parse_args()

a = args.all
d = args.dir
f = args.file
rec = args.recursive
v = args.verbose
e = args.directory[0]
cmd = sys.argv[-1]


def processDir(dr):
    for i in os.listdir(dr):
        if d == False and f == False:
            time.sleep(0)
        else:
            if os.path.isdir(os.path.join(dr, i)) and d == False:
                continue
            if os.path.isfile(os.path.join(dr, i)) and f == False:
                continue
        if i.startswith(".") and a == False:
            continue
        if os.path.isdir(os.path.join(dr, i)) and rec == True:
            processDir(os.path.join(dr, i))
        
        if v != True:
            print("  -> {}".format(os.path.join(dr, i)), end="\r")
        else:
            print("  -> {}".format(os.path.join(dr, i)))
        r = subprocess.Popen(cmd.replace("%i%name", os.path.splitext(i)[0]).replace("%i", i).split(" "), stdout=subprocess.PIPE)
        if v == True:
            for line in r.stdout:
                print(str(line, encoding="utf-8"), end="")
        print("  >< {}".format(os.path.join(dr, i)))

processDir(e)