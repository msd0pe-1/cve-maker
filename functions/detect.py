#!/usr/bin/env python3

"""
https://github.com/msd0pe-1
Source code put in public domain by msd0pe, no Copyright
Any malicious or illegal activity may be punishable by law
Use at your own risk
"""

try:
    import os
    import re
    import json
    import random
    import urllib
    import requests
    from functions import info as info

except ImportError:
    print("\n" + infos.ERROR + "Error. Have you installed the requirements properly?")
    print(infos.INFO + "Be sure to run the script as follows:")
    print(infos.INFO + "python3 cve-maker.py ....")
    print(infos.INFO + "./cve-maker.py ....\n")

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


exploit_db = "https://www.exploit-db.com/"
exploit_db_git = "https://gitlab.com/exploit-database/exploitdb/-/raw/main/"

ua = open('headers.txt').read().splitlines()
header = {"User-Agent": random.choice(ua), "X-Requested-With": "XMLHttpRequest"}

def DetectCompilationOptions(payload, name, name_ext):

    global command
    global usage
    command = ''
    usage = ''

    language = info.lang

    try:
        if language == "c" or language == "c++":
            try:
                command = re.search(r"((gcc|g\+\+) .*?)(\\r\\n|\\n)", str(payload)).group(1)
                if command != '':
                    command = re.sub(' \S*\.cpp', ' /tmp/exploits/' + str(name) + '.cpp', command).strip("\"")
                    command = re.sub(' \S*\.c', ' /tmp/exploits/' + str(name) + '.c', command).strip("\"")
                    command = re.sub('-o \S*', '-o /tmp/exploits/' + str(name), command).strip("\"")
                    print(infos.INFO + "COMPILING OPTIONS DETECTED : " + command)

            except:
                command = "gcc /tmp/exploits/" + str(name_ext) + " -o /tmp/exploits/" + str(name)
                print(infos.INFO + "COMPILING OPTIONS NOT DETECTED, BY DEFAULT : " + command)

            payload_split = payload.splitlines()
            usage = re.search("(\.\/.*?)(\',/\",)", str(payload_split)).group(1)
            if usage != '':
                usage = re.sub('(\.\/.*? )', ' /tmp/exploits/' + str(name) + ' ', usage)
                print(infos.GOOD + "USAGE DETECTED : " + usage)

        elif language == "bash":
            usage = re.search(r"(sh .*?)\\r\\n", str(payload)).group(1)
            if usage != '':
                usage = re.sub(' \S*\.sh', ' /tmp/exploits/' + str(name_ext), usage)
                print(infos.GOOD + "USAGE DETECTED : " + usage)

        elif language == "ruby":
            usage = re.search(r"(ruby .*?)\\r\\n", str(payload)).group(1)
            if usage != '':
                usage = re.sub(' \S*\.rb', ' /tmp/exploits/' + str(name_ext), usage)
                print(infos.GOOD + "USAGE DETECTED : " + usage)

        elif language == "perl":
            usage = re.search(r"(perl .*?)\\r\\n", str(payload)).group(1)
            if usage != '':
                usage = re.sub(' \S*\.pl', ' /tmp/exploits/' + str(name_ext), usage)
                print(infos.GOOD + "USAGE DETECTED : " + usage)

        elif language == "python":
            usage = re.search(r"(python .*?)\\r\\n", str(payload)).group(1)
            if usage != '':
                usage = re.sub(' \S*\.py', ' /tmp/exploits/' + str(name_ext), usage)
                print(infos.GOOD + "USAGE DETECTED : " + usage)

        elif language == "php":
            usage = re.search(r"(php .*?)\\r\\n", str(payload)).group(1)
            if usage != '':
                usage = re.sub(' \S*\.php', ' /tmp/exploits/' + str(name_ext), usage)
                print(infos.GOOD + "USAGE DETECTED : " + usage)


    except AttributeError:
        if language == "c" or language == "c++":
            usage = "/tmp/exploits/" + str(name)
            print(infos.INFO + "USAGE NOT DETECTED, BY DEFAULT : " + usage)

        elif language == "bash":
            usage = "sh /tmp/exploits/" + str(name_ext)
            print(infos.INFO + "USAGE NOT DETECTED, BY DEFAULT : " + usage)

        elif language == "ruby":
            usage = "ruby /tmp/exploits/" + str(name_ext)
            print(infos.INFO + "USAGE NOT DETECTED, BY DEFAULT : " + usage)

        elif language == "perl":
            usage = "perl /tmp/exploits/" + str(name_ext)
            print(infos.INFO + "USAGE NOT DETECTED, BY DEFAULT : " + usage)

        elif language == "python":
            usage = "python /tmp/exploits/" + str(name_ext)
            print(infos.INFO + "USAGE NOT DETECTED, BY DEFAULT : " + usage)

        elif language == "php":
            usage = "php /tmp/exploits/" + str(name_ext)
            print(infos.INFO + "USAGE NOT DETECTED, BY DEFAULT : " + usage)



def CVEFound(detect_edb, description, sub_url):
    sock_edb = urllib.request.urlopen(exploit_db_git + sub_url)
    payload = sock_edb.read()
    sock_edb.close()

    info.GuessLang(sub_url, str(payload))

    if payload != "":
        if description == None:
            print(bcolors.RED + bcolors.BOLD + "EDB-" + bcolors.ENDC + bcolors.ENDC + detect_edb + " : " + "No description found.")
        else:
            print(bcolors.RED + bcolors.BOLD + "EDB-" + bcolors.ENDC + bcolors.ENDC + detect_edb + " : " + str(description) + info.findlang)



def Socket(software, url):

        global socket

        socket = requests.get(url, headers = header)

        lines = socket.text.split('\n')
        socket = re.findall(".*(?i)" + software + ".*", socket.text)

        if socket == None or socket == []:
            print("\n" + infos.GOOD + "No CVE found for this software version !")

        else:
            print(infos.GOOD + "EXPLOITS FOUND : " + "\n")
            for record in socket:
                record_split = record.split(',')
                try:
                    description = record_split[2]
                    detect_edb = record_split[0]
                    sub_url = record_split[1]
                except IndexError:
                    pass

                CVEFound(detect_edb, description, sub_url)

        print()
        return socket


def SearchExploit(software):

    if software == None:
        pass

    else:
        print(infos.PROCESS + "SEARCHING...")
        url = exploit_db_git + "files_exploits.csv"
        print(infos.INFO + "SEARCHING FOR : " + url + " - " + software)
        print()
        Socket(software, url)
