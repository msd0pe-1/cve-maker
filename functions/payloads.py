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

class infos:
    INFO = "[" + bcolors.OCRA + bcolors.BOLD + "?" + bcolors.ENDC + bcolors.ENDC + "] "
    ERROR = "[" + bcolors.RED + bcolors.BOLD + "X" + bcolors.ENDC + bcolors.ENDC + "] "
    GOOD = "[" + bcolors.GREEN + bcolors.BOLD + "+" + bcolors.ENDC + bcolors.ENDC + "] "
    PROCESS = "[" + bcolors.BLUE + bcolors.BOLD + "*" + bcolors.ENDC + bcolors.ENDC + "] "

try:
    import re
    import os
    import json
    import urllib
    import random
    import requests
    from functions import last as last
    from functions import info as info
    from functions import detect as detect

except ImportError:
    print("\n" + infos.ERROR + "Error. Have you installed the requirements properly?")
    print(infos.INFO + "Be sure to run the script as follows:")
    print(infos.INFO + "python3 cve-maker.py ....")
    print(infos.INFO + "./cve-maker.py ....\n")


exploit_db = "https://www.exploit-db.com/"
exploit_db_git = "https://gitlab.com/exploit-database/exploitdb/-/raw/main/"

ua = open('headers.txt').read().splitlines()
header = {"User-Agent": random.choice(ua), "X-Requested-With": "XMLHttpRequest"}

def Compilation(name, command, language):

    if language == None:
        language = info.lang

    if language == "bash":
        pass

    elif language == "ruby":
        pass

    elif language == "perl":
        pass

    elif language == "python":
        pass

    elif language == "php":
        pass

    elif language == "text":
        pass

    elif language == "metasploit":
        pass

    elif language == "jsp":
        pass

    else:
        try:
            print(infos.PROCESS + "COMPILING...")
            if os.system(command) == 0:
                print(infos.GOOD + "EXPLOIT COMPILED WITH SUCCESS : " + "/tmp/exploits/" + name + "\n")
            else:
                exit()

        except:
            print("\n" + infos.ERROR + "/!\ Error during the compilation ! /!\ ")
            exit()


def WritePayload(payload, name_ext):

    exploit = open("/tmp/exploits/" + str(name_ext), "wb")
    exploit.write(payload)
    exploit.close()
    print(infos.GOOD + "EXPLOIT CREATED : " + "/tmp/exploits/" + str(name_ext) + "\n")



def FindCVE(cve, edb):

    global name
    global payload
    global sub_url
    global name_ext

    if edb:
        edb = edb.strip('EDB-')
        try:
            socket = requests.get(exploit_db_git + "files_exploits.csv", headers = header)
            socket = re.findall(".*" + edb + ".*", socket.text)
            sub_url = socket
            for sub in sub_url:
                sub_edb = sub.split(',')[0].split('.')[0]
                if sub_edb == edb:
                    sub_url = sub.split(',')[1]
                    description = sub.split(',')[2].strip('"')
            print("\n" + infos.INFO + "SEARCHING FOR : " + exploit_db_git + sub_url)
            print(infos.GOOD + "EXPLOIT NAME : " + description)
            print(infos.INFO + "DETERMINATION OF THE CVE ID : " + str(last.cves).strip('[]').replace(',', ' ').strip("'"))
            sock = urllib.request.urlopen(exploit_db_git + sub_url)
            payload = sock.read()
            sock.close()
            name = edb

            info.GuessLang(sub_url, str(payload))
            language = info.lang
            print(infos.INFO + "DETERMINATION OF THE LANGUAGE : " + language + bcolors.ENDC + bcolors.ENDC)

            if language == "bash":
                name_ext = str(name) + ".sh"
            elif language == "ruby":
                name_ext = str(name) + ".rb"
            elif language == "perl":
                name_ext = str(name) + ".pl"
            elif language == "python":
                name_ext = str(name) + ".py"
            elif language == "php":
                name_ext = str(name) + ".php"
            elif language == "c++":
                name_ext = str(name) + ".cpp"
            elif language == "c":
                name_ext = str(name) + ".c"
            elif language == "metasploit":
                name_ext = str(name) + ".rb"
            elif language == "text":
                name_ext = str(name) + ".txt"
            elif language == "jsp":
                name_ext = str(name) + ".jsp"

            detect.DetectCompilationOptions(payload, name, name_ext)
            WritePayload(payload, name_ext)
            Compilation(name, detect.command, info.lang)

        except AttributeError:
            print("\n" + infos.ERROR + "You are probably using Python2 ! Use Python3 to run the script.\n")

        except urllib.error.HTTPError:
            print("\n" + infos.ERROR + "Exploit not found ! Verify your ECB-ID.\n")
            exit()

        except IndexError:
            print()
            print(infos.ERROR + "Verify your CVE/EDB ID !")
            print()
            print(infos.ERROR + "No payload available yet for this CVE.\n")
            exit(0)

    elif cve:
        cve = cve.strip('CVE-')
        print("\n" + infos.INFO + "SEARCHING FOR : " + exploit_db + "search?cve=" + cve)
        url = exploit_db + "search?cve=" + cve
        sock_cve = requests.get(url, headers = header).json()
        sock_cve = json.dumps(sock_cve, sort_keys=False, indent=4)
        sock_cve = json.loads(sock_cve)
        sock_cve = sock_cve['data']
        if sock_cve == []:
            print("\n" + infos.ERROR + "No payloads available yet for this CVE.\n")
            exit(0)
        for i in range(len(sock_cve)):
            try:
                cve_edb = sock_cve[i]['id']
                description = sock_cve[i]['description'][1]
                print(infos.GOOD + "EXPLOIT NAME : " + description)
                print(infos.INFO + "DETERMINATION OF THE EDB ID : " + cve_edb)
                sock_edb = urllib.request.urlopen(exploit_db + "raw/" + cve_edb)
                payload = sock_edb.read()
                sock_edb.close()
                name = cve_edb
                socket = requests.get(exploit_db_git + "files_exploits.csv", headers = header)
                socket = re.findall(".*" + name + ".*", socket.text)
                sub_url = socket[0].split(',')[1]

                info.GuessLang(sub_url, str(payload))
                language = info.lang
                print(infos.INFO + "DETERMINATION OF THE LANGUAGE : " + language + bcolors.ENDC + bcolors.ENDC)

                if language == "bash":
                    name_ext = str(name) + ".sh"
                elif language == "ruby":
                    name_ext = str(name) + ".rb"
                elif language == "perl":
                    name_ext = str(name) + ".pl"
                elif language == "python":
                    name_ext = str(name) + ".py"
                elif language == "php":
                    name_ext = str(name) + ".php"
                elif language == "c++":
                    name_ext = str(name) + ".cpp"
                elif language == "c":
                    name_ext = str(name) + ".c"
                elif language == "metasploit":
                    name_ext = str(name) + ".rb"
                elif language == "text":
                    name_ext = str(name) + ".txt"
                elif language == "jsp":
                    name_ext = str(name) + ".jsp"

                detect.DetectCompilationOptions(payload, name, name_ext)
                WritePayload(payload, name_ext)
                Compilation(name, detect.command, info.lang)

            except AttributeError:
                print("\n" + infos.ERROR + "CVE name seams to not be correct.\n")

            except IndexError:
                print("\n" + infos.ERROR + "No payloads available yet for this CVE.\n")
                exit(0)
    else:
        exit(0)

    exit(0)


def CreateDirectory():
    try:
        os.makedirs("/tmp/exploits")
    except OSError:
        if not os.path.isdir("/tmp/exploits"):
            Raise
