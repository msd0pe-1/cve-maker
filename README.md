<a target="_blank" href="https://img.shields.io/badge/platform-linux-success.svg" rel="noopener noreferrer">
    <img src="https://img.shields.io/badge/platform-linux-success.svg">
</a>
<a target="_blank" href="https://img.shields.io/badge/version-2.4.3-yellow" rel="noopener noreferrer">
    <img src="https://img.shields.io/badge/version-2.4.3-yellow">
</a>
<a href="https://www.python.org/" rel="nofollow">
    <img src="https://img.shields.io/badge/python-3.7-red">
</a>
<a href="https://github.com/msd0pe-1/cve-maker-master/blob/master/LICENSE" rel="nofollow">
    <img src="https://img.shields.io/badge/license-GPLv3-9cf.svg">
</a>
<h1>CVE-MAKER</h1>

Use this software <strong>only for legal purposes</strong>. (Example: Vulnerable training machines.)<br />
I am in no way responsible for your actions.<br />
Use python 3.7<br />
<strong>Made by msd0pe</strong><br />

<h2>WHAT IS IT ?</h2>

Cve-maker is a python tool to detect, find, compile and execute a CVE on the current or a remote machine.<br />
It's the perfect tool to play with CVE and Exploits.
It is intended to save you time.
You can easily find your CVEs on https://www.exploit-db.com/ or with the Search option.

<h2>HOW IT WORKS ?</h2>

Cve-maker will search in CVE databases for the payload associated with the CVE that you provide it with parameters.<br />
It creates it in the directory "/tmp/exploits/" and compiles it if necessary.<br /><br />

<h2>GET EXPLOIT BY CVE-ID</h2>
<p align="center">
  <img src="https://user-images.githubusercontent.com/47142249/180973612-fca1fddc-a7ed-4afb-b3cf-864ba2ed014c.png">
</p>

<h2>GET EXPLOIT BY EDB-ID</h2>
<p align="center">
  <img src="https://user-images.githubusercontent.com/47142249/180972820-a16f2801-db22-4004-bb99-04f7d0db372b.png">
</p>

<h2>RESEARCH</h2>
<p align="center">
  <img src="https://user-images.githubusercontent.com/47142249/180971778-099addb5-80d3-4581-b131-b229a3e1a892.png">
</p>
Search your CVEs by entering keywords !

<h2>SHODAN</h2>
<p align="center">
  <img src="https://user-images.githubusercontent.com/47142249/180974645-3da28a54-72bc-423a-b1fb-6d53cca6b897.png">
</p>
Search directly impacted devices around the world !

<h2>INSTALLATION</h2>
Download the project:
<code>git clone https://github.com/msd0pe-1/cve-maker/</code><br />
You only need to execute install.sh to get the libraries useful to the program : <code>bash install.sh</code><br />

<h2>USAGE</h2>
<pre>
    <code>
Usage: python cve-maker.py [options]

Options:
  --version             show program's version number and exit
  -h, --help            show this help message and exit
  -f FIND, --find=FIND  looking for an exploit by its vulnerable software
  -c CVE, --cve=CVE     looks for the CVE from its name
  -e EDB, --edb=EDB     looks for the CVE from its EDB-ID
  --critical            show the last criticals vulnerabilities
  --shodan              search targets from a given CVE

  Examples:
    python cve-maker.py -f "Log4j"
    python cve-maker.py -c CVE-2021-44228
    python cve-maker.py -e 50592
    python cve-maker.py -c 2019-98765 --shodan
    python cve-maker.py -f "php 8.1.0" --shodan
    python cve-maker.py --critical

  Tool to find CVEs, Exploits and Vulnerable Targets.
  Source code put in public domain by msd0pe,no Copyright
  Any malicious or illegal activity may be punishable by law
  Use at your own risk
    </code>
</pre>

<h2>CONTRIBUTING</h2>

This project is in active development. Feel free to suggest a new feature or open a pull request !
