#!/usr/bin/python3
"""Alta3 Research | rzfeeser@alta3.com
   Learning about Python SSH"""

import paramiko
import time

def main():
    """Our runtime code that calls other functions"""
    # describe the connection data
    credz = [
             {"un": "bender", "ip": "10.10.2.3"}, 
             {"un": "zoidberg", "ip": "10.10.2.5"}, 
             {"un": "fry", "ip": "10.10.2.4"}
            ]

    # harvest private key for all 3 servers
    mykey = paramiko.RSAKey.from_private_key_file("/home/student/.ssh/id_rsa")

    ##getting input from user install or uninstall
    sl_installer = input("""
        Please pick an option:
        Enter 0 to uninstall sl
        Enter 1 to install sl
        """)  
    # loop across the collection credz
    for cred in credz:
        ## create a session object
        sshsession = paramiko.SSHClient()

        ## add host key policy
        sshsession.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        ## display our connections
        print("Connecting to... " + cred.get("un") + "@" + cred.get("ip"))

        ## make a connection
        sshsession.connect(hostname=cred.get("ip"), username=cred.get("un"), pkey=mykey)

        ## touch the file goodnews.everyone in each user's home directory
        #sshsession.exec_command("touch /home/" + cred.get("un") + "/goodnews.everyone")

        ## list the contents of each home directory
        #sessin, sessout, sesserr = sshsession.exec_command("ls /home/" + cred.get("un"))
        
        ##confirm if sl is install
        sessin, sessout, sesserr = sshsession.exec_command('test -f /usr/games/sl && echo "FILE exists" || echo "File does not exist" ')
        output = sessout.read().decode('utf-8')
        check = output.strip() == "FILE exists"
        
       
        ##checking sl_installer value
        if sl_installer.strip() == "1": 
            
            if check:
                print("sl is already installed this host was SKIPPED")
                #print(sessout.read().decode('utf-8'))
            else:
                ## install sl
                sshsession.exec_command("sudo apt install sl")
                time.sleep(4)
                sessin, sessout, sesserr = sshsession.exec_command('test -f /usr/games/sl && echo "FILE exists" || echo "File does not exist" ')
                print(sessout.read().decode('utf-8'))
                
        else:
            ##uninstall sl            
            sshsession.exec_command("sudo apt remove sl -y")
            time.sleep(5)
            sessin, sessout, sesserr = sshsession.exec_command('test -f /usr/games/sl && echo "File does not exist" ||  "FILE exists" ')
            print(sessout.read().decode('utf-8'))
                
         
                
                

        # ##confirm if sl is install
        # sessin, sessout, sesserr = sshsession.exec_command('test -f /usr/games/sl && echo "FILE exists" || echo "File does not exist" ')

        # print(sessout.read().decode('utf-8'))

        ## display output
        #print(sessout.read().decode('utf-8'))

        ## close/cleanup SSH connection
        sshsession.close()

    print("Thanks for looping with Alta3!")

main()