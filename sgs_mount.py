#!env python3

""" Mounts the SSH locations to the given mount points. Create ~/mnt and all mount points before. Use -u to umount. """

import subprocess, sys

mounts = [
    ["helium:/import/sgs.local", "~/mnt/sgs"],
    ["helium:", "~/mnt/home"],
    ["helium:/data2/scratch", "~/mnt/scratch"],
    ["ipvslogin:/import/www.ipvs", "~/mnt/www.ipvs"],
    # ["supermuc:", "~/mnt/supermuc"] 
]

try:
    arg = sys.argv[1]
except IndexError:
    arg = ""

print(arg)
for dev, diry in mounts:
    if arg == "-u":
        cmd = "fusermount -u " + diry
    else:
        cmd = "sshfs " + dev + " " + diry
    print(cmd, end=": ")
    if not subprocess.call(cmd, shell=True):
        print("OK.")
    else:
        print("FAILED.")
