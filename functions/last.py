#!/usr/bin/env python3

"""
https://github.com/msd0pe-1
Source code put in public domain by msd0pe, no Copyright
Any malicious or illegal activity may be punishable by law
Use at your own risk
"""

try:
    import re
    import random
    import requests

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

class bgcolors:
    #ref = random.randrange(1, 255, 3) ## RANDOM COLORS
    ref = 243
    CVE = '\033[1m' + '\u001b[48;5;' + str(ref) + 'm'
    VENDOR = '\033[1m' + '\u001b[48;5;' + str(ref-2) + 'm'
    PRODUCT = '\033[1m' + '\u001b[48;5;' + str(ref-4) + 'm'
    CRITICAL = '\033[1m' + '\u001b[48;5;88m'
    HIGH = '\033[1m' + '\u001b[48;5;124m'
    MEDIUM = '\033[1m' + '\033[30;43m'
    LOW = '\033[1m' + '\033[30;44m'
    SEPARATOR1 = '\033[0m' + '\u001b[48;5;' + str(ref-1) + 'm ' + '\033[0m'
    SEPARATOR2 = '\033[0m' + '\u001b[48;5;' + str(ref-3) + 'm ' + '\033[0m'
    SEPARATOR3 = '\033[0m' + '\u001b[48;5;' + str(ref-5) + 'm ' + '\033[0m'

class infos:
    INFO = "[" + bcolors.OCRA + bcolors.BOLD + "?" + bcolors.ENDC + bcolors.ENDC + "] "
    ERROR = "[" + bcolors.RED + bcolors.BOLD + "X" + bcolors.ENDC + bcolors.ENDC + "] "
    GOOD = "[" + bcolors.GREEN + bcolors.BOLD + "+" + bcolors.ENDC + bcolors.ENDC + "] "
    PROCESS = "[" + bcolors.BLUE + bcolors.BOLD + "*" + bcolors.ENDC + bcolors.ENDC + "] "


opencve = "https://www.opencve.io/cve"

ua = open('headers.txt').read().splitlines()
header = {"User-Agent": random.choice(ua), "X-Requested-With": "XMLHttpRequest"}

def GetLastCritical():
    print("\n" + infos.INFO + "SEARCHING FOR : " + opencve + "?cvss=critical&search=")
    url = opencve + "?cvss=critical&search="
    sock_critical = requests.get(url, headers = header)

    criticals = re.findall("<strong>(CVE-.*)<\/strong>.*(?:\n.*?)+(?:(N\/A).*(?:\n.*?)+(N\/A).*?|vendor=(.*?)&product=(.*?)').*(?:\n.*(\d.\d).*?|\n.*?)+<tr class=\"cve-summary\">\n.*colspan=\"5\">(.*)<\/td>\n.*<\/tr>", sock_critical.text)
    print()
    for i in range(len(criticals)):
        if criticals[i][5] == "":
            score = bgcolors.LOW + "N/A"
        else:        
            score = bgcolors.CRITICAL if float(criticals[i][5]) > 8.9 else bgcolors.HIGH if float(criticals[i][5]) > 6.9 else bgcolors.MEDIUM if float(criticals[i][5]) > 3.9 else bgcolors.LOW
        print(bgcolors.CVE + criticals[i][0] + bgcolors.SEPARATOR1 + bgcolors.SEPARATOR1 + bgcolors.VENDOR + criticals[i][3].upper() + bgcolors.SEPARATOR2 + bgcolors.SEPARATOR2 + bgcolors.PRODUCT + criticals[i][4] + bgcolors.SEPARATOR3 + bgcolors.SEPARATOR3 + score + criticals[i][5] + bcolors.ENDC + " " + criticals[i][6] + bcolors.ENDC)
    print()

def GetLast(software):
    print("\n" + infos.PROCESS + "SEARCHING FOR THE LASTS VULNS...")
    print(infos.INFO + "SEARCHING FOR : " + opencve + "?search=" + software)
    url = opencve + "?search=" + software
    sock_last = requests.get(url, headers = header)

    lasts = re.findall("<strong>(CVE-.*)<\/strong>.*(?:\n.*?)+(?:(N\/A).*(?:\n.*?)+(N\/A).*?|vendor=(.*?)&product=(.*?)').*(?:\n.*(\d.\d).*?|\n.*?)+<tr class=\"cve-summary\">\n.*colspan=\"5\">(.*)<\/td>\n.*<\/tr>", sock_last.text)
    print()
    if len(lasts) != 0:
        for i in range(len(lasts)):
            if lasts[i][5] == "":
                score = bgcolors.LOW + "N/A"
            else:
                score = bgcolors.CRITICAL if float(lasts[i][5]) > 8.9 else bgcolors.HIGH if float(lasts[i][5]) > 6.9 else bgcolors.MEDIUM if float(lasts[i][5]) > 3.9 else bgcolors.LOW
            print(bgcolors.CVE + lasts[i][0] + bgcolors.SEPARATOR1 + bgcolors.SEPARATOR1 + bgcolors.VENDOR + lasts[i][3].upper() + bgcolors.SEPARATOR2 + bgcolors.SEPARATOR2 + bgcolors.PRODUCT + lasts[i][4] + bgcolors.SEPARATOR3 + bgcolors.SEPARATOR3 + score + lasts[i][5] + bcolors.ENDC + " " + lasts[i][6] + bcolors.ENDC)
    else:
        print(bcolors.RED + bcolors.BOLD + "No CVE founded for " + software + bcolors.ENDC + bcolors.ENDC)
    print()

def GetDescription(cve,edb):

    global cves

    print("\n" + infos.PROCESS + "SEARCHING FOR CVE INFORMATIONS...")
    cves = []
    if cve != None or edb != None:
        if cve != None:
            if 'CVE-' not in cve:
                cve = "CVE-" + cve
            cves.append(cve)
        elif edb != None:
            edb = edb.strip('EDB-')
            url = "https://www.exploit-db.com/exploits/" + edb
            sock_cve = requests.get(url, headers = header)
            cve_name = re.findall("target=\"_blank\">.*\n(.*?-.*?)\n.*<\/a>",sock_cve.text)
            for cve in cve_name:
                cve = "CVE-" + cve.strip(' ')
                cves.append(cve)
            if cve_name == []:
                print()
                print(bcolors.RED + bcolors.BOLD + "No CVE founded for EDB-" + edb + bcolors.ENDC + bcolors.ENDC)

        if cves != None:
            for id_cve in cves:
                print(infos.INFO + "SEARCHING FOR " + opencve + "/" + cve)
                url = opencve + "/" + cve
                sock_description = requests.get(url, headers = header)
                print()

                description = re.findall("<div class=\"box-body\">.*\n.*<span class=\"dropcap\">(.*?)\n.*<\/div>", sock_description.text)
                try:
                    print(bgcolors.CVE + id_cve + bcolors.ENDC + " " + description[0].replace('</span>',''))
                except IndexError:
                    if url == "":
                        print(bcolors.RED + bcolors.BOLD + "No CVE founded for EDB-" + edb + bcolors.ENDC + bcolors.ENDC)
                    else:
                        print(infos.ERROR + "Verify your CVE/EDB ID !")
                        print()
            