#!/usr/bin/env python
# A system info gathering scrip

import subprocess

# command 1
def uname_func():
    uname = "uname"
    uname_arg = "-a"
    print("Gathering system information with {} command:\n".format(uname))
    subprocess.call([uname, uname_arg])

#command 2
def disk_func():
    diskspace = "df"
    diskspace_arg = "-h"
    print("Gathering diskspace information with the {} command:\n".format(diskspace))
    subprocess.call([diskspace, diskspace_arg])

def main():
    uname_func()
    disk_func()

if __name__ == "__main__":
    main()
