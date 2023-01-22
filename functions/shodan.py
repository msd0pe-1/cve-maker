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
    import os
    import re
    import shodan
    import random
    import requests
    from bs4 import BeautifulSoup


except ImportError:
    print("\n" + infos.ERROR + "Error. Have you installed the requirements properly?")
    print(infos.INFO + "Be sure to run the script as follows:")
    print(infos.INFO + "python3 cve-maker.py ....")
    print(infos.INFO + "./cve-maker.py ....\n")

cve_details = "https://www.cvedetails.com/cve/"

ua = open('headers.txt').read().splitlines()
header = {"User-Agent": random.choice(ua), "X-Requested-With": "XMLHttpRequest"}

def ProductVersionIdentify(cve,edb):

    global cve_shodan
    global vendors_versions
    global products_versions

    if cve != None or edb != None:
        if cve != None:
            cve_shodan = cve
            if 'CVE-' not in cve:
                cve_shodan = "CVE-" + cve
        elif edb != None:
            edb = edb.strip('EDB-')
            url = "https://www.exploit-db.com/exploits/" + edb
            sock_cve = requests.get(url, headers = header)
            cve_name = re.findall("target=\"_blank\">.*\n(.*?-.*?)\n.*<\/a>",sock_cve.text)
            cve_shodan = "CVE-" + cve_name[0].strip(' ')
            if cve_name == []:
                print()
                print(bcolors.RED + bcolors.BOLD + "No CVE founded for EDB-" + edb + bcolors.ENDC + bcolors.ENDC)
                exit(0)

    vendors_versions = []
    products_versions = []

    print(infos.INFO + "SEARCHING FOR : " + cve_details + cve_shodan)

    url = cve_details + cve_shodan
    sock_cve_details = requests.get(url, headers = header)

    cve_defaults_table = BeautifulSoup(sock_cve_details.text, 'lxml')

    for i in range(len(cve_defaults_table.find_all('table'))):
        if "Product Type" in str(cve_defaults_table.find_all('table')[i]):
            bs4_table = cve_defaults_table.find_all('table')[i]

    product_version_re = re.findall("<a href=\"\/vendor.*\">(.*)<\/a> <\/td>\n.*\n<a href=\"\/product.*\">(.*)<\/a> <\/td>\n.*<td>\n(.*)<\/td>", str(bs4_table))
    for result in product_version_re:
        vendors_versions.append(str(result[0] + " " + result[2].strip('\t')))
        products_versions.append(str(result[1] + " " + result[2].strip('\t')))

    print(infos.PROCESS + "DETERMINATION OF IMPACTED PRODUCTS...")

def Shodan(api_key,vendors_versions,products_versions,cve,find):

    api = shodan.Shodan(api_key)

    try: 
        os.makedirs("/tmp/reports")
    except OSError:
        if not os.path.isdir("/tmp/reports"):
            Raise

    if find == None:
        vendors_versions = list(set(vendors_versions))
        products_versions = list(set(products_versions))
        print(infos.INFO + "SEARCHING FOR : " + str(vendors_versions).strip('[]') + ", " + str(products_versions).strip('[]') )
        print()
        print(infos.PROCESS + "CONNECTING TO SHODAN...\n")
        for vendor_version in vendors_versions:
            if "*" in vendor_version:
                result = api.search(vendor_version[:-2])
            else:
                result = api.search(vendor_version)

            if result['total'] != 0:
                report_path = "/tmp/reports/" + cve
                try: 
                    os.makedirs(report_path)
                except OSError:
                    if not os.path.isdir(report_path):
                        Raise
            
                report_name = report_path + "/vendors-" + vendor_version.replace(' ','_') 
                with open(report_name, "w") as report:
                    for match in result['matches']:
                        report.write("IP : {}".format(match['ip_str'] + "\n"))
                        report.write(match['data'] + "\n\n")
            
                print(infos.GOOD + vendor_version + " - REPORT CREATED : " + report_name + " - " + str(result['total']) + " results.")

            else:
                print(infos.ERROR + vendor_version + " - No targets founded with vendors versions.")

        for product_version in products_versions:
            if "*" in product_version:
               result = api.search(product_version[:-2])
            else:
                result = api.search(product_version)

            if result['total'] != 0:
                report_path = "/tmp/reports/" + cve
                try: 
                    os.makedirs(report_path)
                except OSError:
                    if not os.path.isdir(report_path):
                        Raise
            
                report_name = report_path + "/products" + product_version.replace(' ','_') 
                with open(report_name, "w") as report:
                    for match in result['matches']:
                        report.write("IP : {}".format(match['ip_str'] + "\n"))
                        report.write(match['data'] + "\n\n")
            
                print(infos.GOOD + product_version + " - REPORT CREATED : " + report_name + " - " + str(result['total']) + " results.")

            else:
                print(infos.ERROR + product_version + " - No targets founded with products versions.")

    else:
        print(infos.INFO + "SEARCHING FOR : " + vendors_versions)
        print(infos.PROCESS + "CONNECTING TO SHODAN...\n")
        result = api.search(vendors_versions)
        if result['total'] != 0:    
            report_name = "/tmp/reports/" + vendors_versions
            with open(report_name, "w") as report:
                for match in result['matches']:
                    report.write("IP : {}".format(match['ip_str'] + "\n"))
                    report.write(match['data'] + "\n\n")
            
            print(infos.GOOD + "REPORT CREATED : " + report_name + " - " + str(result['total']) + " results.")

        else:
            print(infos.ERROR + vendors_versions + " - No targets founded with products versions.")

    print()
