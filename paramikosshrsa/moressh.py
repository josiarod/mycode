#!/usr/bin/python3

import paramiko
from credz import*

def main():
   


    mykey = paramiko.RSAKey.from_private_key_file("/home/student/.ssh/id_rsa")

    
    for cred in credz:
       ##create session object
       sshsession = paramiko.SSHClient()
       
       ##ADD host key policy
       sshsession.set_missing_host_key_policy(paramiko.AutoAddPolicy())
       
       ## display our connection
       print("Connecting to... " + cred.get("un") + "@" + cred.get("ip"))

       ##make a connection
       sshsession.connect(hostname=cred.get("ip"), username=cred.get("un"), pkey=mykey)

       ## touch files 
       sshsession.exec_command("touch /home/" + cred.get("un") + "/goodnews.everyone")

       ## list the contents of each home directory
       sessin, sessout, sesserr = sshsession.exec_command("ls /home/" + cred.get("un"))
       
       ##append ls output to results.log
       with open("results.log", "a") as results:
          results.write(sessout.read().decode('utf-8') )
           

            

        ## display output
       print(sessout.read().decode('utf-8'))

        ## close/cleanup SSH connection
       sshsession.close()

    print("Thanks for looping with Alta3!")

main()

