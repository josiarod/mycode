#!/usr/bin/env python3

import paramiko
import os

def movethemfiles(sftp):
    for x in os.listdir("/home/student/filestocopy/"):
        if not os.path.isdir("/home/student/filestocopy" +x):
            sftp.put("/home/student/filestocopy/"+x, "/tmp/"+x)

t = paramiko.Transport("10.10.2.3", 22) #IP and port

t.connect(username="bender", password="alta3")

sftp = paramiko.SFTPClient.from_transport(t)

movethemfiles(sftp)


sftp.close()
t.close()