import os
import pwd
import grp

red :str = "\033[91m"
green :str = "\033[92m" 
cyan :str = "\033[96m"

path :str = input(cyan + "Write path: ").strip()
if not os.path.exists(path):
    print(red + "Incorrect path")
    exit()
try:
    userId :str = input(cyan + "Write user id: ").strip()
    uid :str = pwd.getpwnam(userId).pw_uid
except KeyError:
    print(red + "User was not found")
    exit()
try:
    groupId :str = input(cyan + "Write group id: ")   
    gid :str = grp.getgrnam(groupId).gr_gid
except KeyError:
    print(red + "Group was not found")
    exit()
try:
    os.chown(path,uid,gid)
    print(green + "Owner was changed successfuly")
except Exception as e:
    print(e)
    print(red + "owner was not changed")