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
    import re
    import urllib
    import requests
    from bs4 import BeautifulSoup
    from functions import info as info

except ImportError:
    print(bcolors.RED + bcolors.BOLD + "\nError. Have you installed the requirements properly?" + bcolors.ENDC + bcolors.ENDC)
    print(bcolors.RED + bcolors.BOLD + "Be sure to run the script as follows:\n" + bcolors.ENDC + bcolors.ENDC)
    print(bcolors.OCRA + bcolors.BOLD + "python3 cve-maker.py ...." + bcolors.ENDC + bcolors.ENDC)
    print(bcolors.OCRA + bcolors.BOLD + "./cve-maker.py ...." + bcolors.ENDC + bcolors.ENDC)


exploit_db = "https://www.exploit-db.com/"


def CVEFound(equalize_parser, description, detect_cve_name, check):
    n = 0
    equalizer = ""
    del equalize_parser[0]
    header = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36","X-Requested-With": "XMLHttpRequest"}

    try:
        if len(description) < 50:
            for i in range(0, len(description)):
                detect_edb = re.search('"(.*?)"', str(description[i])).group(0).strip('""')
                sock_edb = urllib.request.urlopen(exploit_db + "raw/" + detect_edb)
                payload = sock_edb.read()
                sock_edb.close()

                info.GuessLang(str(payload))
                equalizer = equalize_parser[i].find(detect_cve_name[n])
                if payload != "":
                    if equalizer != -1:
                        print(bcolors.RED + bcolors.BOLD + "CVE-" + bcolors.ENDC + bcolors.ENDC + detect_cve_name[n] + " : " + description[i] + info.findlang)
                        info.IsCheck(description, i, check)
                        n += 1
                        if n == len(detect_cve_name):
                            break
                    else:
                        print(bcolors.RED + bcolors.BOLD + "CVE-NONE" + bcolors.ENDC + bcolors.ENDC + " : " + description[i] + info.findlang)
                        info.IsCheck(description, i, check)
                else:
                    if equalizer != -1:
                        print(bcolors.RED + bcolors.BOLD + "CVE-" + bcolors.ENDC + bcolors.ENDC + detect_cve_name[n] + " : " + description[i])
                        info.IsCheck(description, i, check)
                        n += 1
                        if n == len(detect_cve_name):
                            break
                    else:
                        print(bcolors.RED + bcolors.BOLD + "CVE-NONE" + bcolors.ENDC + bcolors.ENDC + " : " + description[i])
                        info.IsCheck(description, i, check)

        else:
            print(bcolors.RED + bcolors.BOLD + "Too many results, be more specific !" + bcolors.ENDC + bcolors.ENDC)

    except:
        print("")
        print(bcolors.RED + bcolors.BOLD + "Be careful, maybe not all CVEs are displayed." + bcolors.ENDC + bcolors.ENDC) 
        pass



def SearchExploit(software, check): 

    if software == None:
        pass

    else:
        print(bcolors.BLUE + bcolors.BOLD + "\nSEARCHING..." + bcolors.ENDC + bcolors.ENDC)
        header = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36","X-Requested-With": "XMLHttpRequest"}
        url = exploit_db + "search?q=" + software
        print(bcolors.OCRA + bcolors.BOLD + "\n> SEARCHING FOR : " + bcolors.ENDC + bcolors.ENDC + url + "\n")
        sock_find = requests.get(url, headers = header)
        findme = BeautifulSoup(sock_find.text, 'html.parser')
        try:
            detect_cve_name = re.findall('\"cve\"\,\"code\"\:\"(.*?)\"', str(findme), re.DOTALL)
            description = re.findall('description\"\:(.*?)\,\"type_id', str(findme), re.DOTALL)
            equalize_parser = str(findme).split('description')
            if detect_cve_name == [] and description == []:
                print(bcolors.GREEN + bcolors.BOLD + "No CVE found for this software version !" + bcolors.ENDC + bcolors.ENDC)
                print("")
            else:
                print(bcolors.RED + bcolors.BOLD + "> EXPLOITS FOUND : " + bcolors.ENDC + bcolors.ENDC + "\n")
                if description == [] and detect_cve_name != []:
                    for i in range(0, len(detect_cve_name)):
                        print(bcolors.RED + bcolors.BOLD + "CVE-" + bcolors.ENDC + bcolors.ENDC + detect_cve_name[i] + " : " + "No description found.")
                        info.IsCheck(detect_cve_name, i, check)
                    print("")
                else:
                    CVEFound(equalize_parser, description, detect_cve_name, check)
                    print("")

        except RuntimeError:
            print(bcolors.RED + bcolors.BOLD + "Too many results, be more specific !\n" + bcolors.ENDC + bcolors.ENDC)		

        except:
            print(bcolors.RED + bcolors.BOLD + "Error during the searching !\n" + bcolors.ENDC + bcolors.ENDC)



def DetectCVE(site, detect, check):
    if site == "exploit_db":
        if detect == None:
            pass

        else:
            print(bcolors.BLUE + bcolors.BOLD + "\nDETECTING...\n" + bcolors.ENDC + bcolors.ENDC)
            os_uname = os.uname()
            os_concat = os_uname[0] + ' ' + os_uname[2]
            os_version_number = re.search('(.*?)-', os_concat).group(1)
            print(bcolors.PURPLE + bcolors.BOLD + "> KERNEL FOUND : " + bcolors.ENDC + bcolors.ENDC + os_version_number + "\n")

            header = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36","X-Requested-With": "XMLHttpRequest"}
            url = exploit_db + "search?text=" + os_version_number
            print(bcolors.OCRA + bcolors.BOLD + "> SEARCHING FOR : " + bcolors.ENDC + bcolors.ENDC + url + "\n")
            sock_detect = requests.get(url, headers = header)
            findme = BeautifulSoup(sock_detect.text, 'html.parser')
            equalize_parser = str(findme).split('description')
            try:
                detect_cve_name = re.findall('\"cve\"\,\"code\"\:\"(.*?)\"', str(findme), re.DOTALL)
                description = re.findall('description\"\:(.*?)\,\"type_id', str(findme), re.DOTALL)
                if detect_cve_name == [] and description == []:
                    print(bcolors.GREEN + bcolors.BOLD + "This machine does not seams vulnerable !" + bcolors.ENDC + bcolors.ENDC)
                    print("")
                else:
                    print(bcolors.RED + bcolors.BOLD + "> POSSIBLE EXPLOITS : " + bcolors.ENDC + bcolors.ENDC + "\n")
                    if description == [] and detect_cve_name != []:
                        for i in range(0, len(detect_cve_name)):
                            print(bcolors.RED + bcolors.BOLD + "CVE-" + bcolors.ENDC + bcolors.ENDC + detect_cve_name[i] + " : " + "No description found.")
                            info.IsCheck(detect_cve_name, i, check)
                        print("")
                    else:
                        CVEFound(equalize_parser, description, detect_cve_name, check)
                        print("")

            except RuntimeError:
                print(bcolors.RED + bcolors.BOLD + "Too many results, be more specific !\n" + bcolors.ENDC + bcolors.ENDC)

            except:
                print(bcolors.RED + bcolors.BOLD + "Error during the detection !\n" + bcolors.ENDC + bcolors.ENDC)

