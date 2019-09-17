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
    import urllib

except ImportError:
    print(bcolors.RED + bcolors.BOLD + "\nError. Have you installed the requirements properly?" + bcolors.ENDC + bcolors.ENDC)
    print(bcolors.RED + bcolors.BOLD + "Be sure to run the script as follows:\n" + bcolors.ENDC + bcolors.ENDC)
    print(bcolors.OCRA + bcolors.BOLD + "python3 cve-maker.py ...." + bcolors.ENDC + bcolors.ENDC)
    print(bcolors.OCRA + bcolors.BOLD + "./cve-maker.py ...." + bcolors.ENDC + bcolors.ENDC)


exploit_db = "https://www.exploit-db.com/"


def GuessLang(payload):

    global findlang

    c_cpp_wordlist = ["#include"]
    shell_wordlist = ["#!/bin/sh", "#!/bin/bash", "#!/usr/bin/bash", "#/usr/bin/sh", "#!/usr/bin/env sh", "#!/usr/bin/env bash"]
    ruby_wordlist = ["#!/bin/ruby", "#!/usr/bin/ruby", "#!/usr/bin/env ruby"]
    perl_wordlist = ["#!/bin/perl", "#!/usr/bin/perl", "#!/usr/bin/env perl"]
    python_wordlist = ["#!/bin/python", "#!/usr/bin/python", "#!/usr/bin/env python"]
    php_wordlist = ["#!/bin/php", "#/usr/bin/php", "#!/usr/bin/env php", "<?php"]
    metasploit_wordlist = ["MetasploitModule", "Msf::Exploit"]
    all_wordlist = c_cpp_wordlist + shell_wordlist + ruby_wordlist + perl_wordlist + python_wordlist + php_wordlist + metasploit_wordlist

    for word in all_wordlist:
        if word in payload and word in c_cpp_wordlist:
            findlang = " - " + bcolors.CYAN + bcolors.BOLD + "c or c++" + bcolors.ENDC + bcolors.ENDC
            break
        elif word in payload and word in shell_wordlist:
            findlang = " - " + bcolors.GREEN + bcolors.BOLD + "sh" + bcolors.ENDC + bcolors.ENDC
            break
        elif word in payload and word in ruby_wordlist:
            findlang = " - " + bcolors.RED + bcolors.BOLD + "ruby" + bcolors.ENDC + bcolors.ENDC
            break
        elif word in payload and word in perl_wordlist:
            findlang = " - " + bcolors.PURPLE + bcolors.BOLD + "perl" + bcolors.ENDC + bcolors.ENDC
            break
        elif word in payload and word in python_wordlist:
            findlang = " - " + bcolors.OCRA + bcolors.BOLD + "python" + bcolors.ENDC + bcolors.ENDC
            break
        elif word in payload and word in php_wordlist:
            findlang = " - " + bcolors.BLUE + bcolors.BOLD + "php" + bcolors.ENDC + bcolors.ENDC
            break
        elif word in payload and word in metasploit_wordlist:
            findlang = " - " + bcolors.BOLD + bcolors.RED + "metasploit" + bcolors.ENDC + bcolors.ENDC
            break
        else:
            findlang = " - " + bcolors.BOLD + "text" + bcolors.ENDC


def IsCheck(description, i, check):

    if check == None:
        pass

    else:
        detect_edb_id = re.search('\"(.*?)\"\,', str(description[i])).group(1)
        url = exploit_db + "exploits/" + detect_edb_id
        sock_check = urllib.request.urlopen(url)
        ischeck = sock_check.read()
        sock_check.close()
        verified = re.search('mdi-check', str(ischeck))
        if verified == None:
            print(bcolors.OCRA + bcolors.BOLD + "EDB Verified : " + bcolors.ENDC + bcolors.ENDC + bcolors.RED + bcolors.BOLD + "NO" + bcolors.ENDC + bcolors.ENDC)
        else:
            print(bcolors.OCRA + bcolors.BOLD + "EDB Verified : " + bcolors.ENDC + bcolors.ENDC + bcolors.GREEN + bcolors.BOLD + "YES" + bcolors.ENDC + bcolors.ENDC)
