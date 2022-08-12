#!/usr/bin/python3

import os
import paramiko

##issuing commands to remote
def commandissue(command_to_issue, sshsession):
    ssh_stdin, ssh_stdout, ssh_stderr = sshsession.exec_command(command_to_issue)
    return ssh_stderr.read()

def main():
    sshsession = paramiko.SSHClient()

    mykey = paramiko.RSAKey.from_private_key_file("/home/student/.ssh/id_rsa")

    ##add fingerprint to the known hosts
    sshsession.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    ##creds to connect
    sshsession.connect(hostname="10.10.2.3", username="bender", pkey=mykey)

     ## a simple list of commands to issue across our connection
    our_commands = ["touch sshworked.txt", "touch create.txt", "touch file3.txt", "ls"]

    for x in our_commands:
        print(commandissue(x, sshsession).decode('utf-8'))


main()