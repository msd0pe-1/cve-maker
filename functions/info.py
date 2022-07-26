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


def GuessLang(sub_url, payload):

    global lang
    global findlang

    metasploit_wordlist = ["MetasploitModule", "Msf::Exploit"]
    if sub_url[-4:] == ".cpp":
        findlang = " - " + bcolors.CYAN + bcolors.BOLD + "c++" + bcolors.ENDC + bcolors.ENDC
        lang = "c++"
    elif sub_url[-2:] == ".c":
        findlang = " - " + bcolors.CYAN + bcolors.BOLD + "c" + bcolors.ENDC + bcolors.ENDC
        lang = "c"
    elif sub_url[-3:] == ".sh":
        findlang = " - " + bcolors.GREEN + bcolors.BOLD + "sh" + bcolors.ENDC + bcolors.ENDC
        lang = "bash"
    elif sub_url[-3:] == ".rb":
        findlang = " - " + bcolors.RED + bcolors.BOLD + "ruby" + bcolors.ENDC + bcolors.ENDC
        lang = "ruby"
        for word in metasploit_wordlist:
            if word in payload:
                findlang = " - " + bcolors.RED + bcolors.BOLD + "metasploit" + bcolors.ENDC + bcolors.ENDC
                lang = "metasploit"
    elif sub_url[-3:] == ".pl":
        findlang = " - " + bcolors.PURPLE + bcolors.BOLD + "perl" + bcolors.ENDC + bcolors.ENDC
        lang = "perl"
    elif sub_url[-3:] == ".py":
        findlang = " - " + bcolors.OCRA + bcolors.BOLD + "python" + bcolors.ENDC + bcolors.ENDC
        lang = "python"
    elif sub_url[-4:] == ".php":
        findlang = " - " + bcolors.BLUE + bcolors.BOLD + "php" + bcolors.ENDC + bcolors.ENDC
        lang = "php"
    elif sub_url[-4:] == ".txt" or sub_url[-5:] == ".html":
        findlang = " - " + bcolors.BOLD + "text" + bcolors.ENDC
        lang = "text"
    elif sub_url[-4:] == ".jsp":
        findlang = " - " + bcolors.OCRA + bcolors.BOLD + "jsp" + bcolors.ENDC + bcolors.ENDC
        lang = "jsp"

