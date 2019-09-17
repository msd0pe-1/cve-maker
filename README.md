<a target="_blank" href="https://img.shields.io/badge/platform-linux-success.svg" rel="noopener noreferrer">
    <img src="https://img.shields.io/badge/platform-linux-success.svg">
</a>
<a target="_blank" href="https://img.shields.io/badge/version-2.0-yellow" rel="noopener noreferrer">
    <img src="https://img.shields.io/badge/version-2.0-yellow">
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
It is intended to save you time.
You can easily find your CVEs on https://www.exploit-db.com/ or with the Search option.

<h2>HOW IT WORKS ?</h2>

Cve-maker will search on CVE databases for the payload associated with the CVE that you provide it with parameters.<br />
It creates it in the directory "/tmp/exploit/" and compiles it if necessary. It then proposes you to execute it or not.<br /><br />

<p align="center">
  <img src="https://user-images.githubusercontent.com/47142249/60006167-37e88680-9670-11e9-94c1-d085e3fc993c.png">
</p>

<h2>DETECTION</h2>
<p align="center">
  <img src="https://user-images.githubusercontent.com/47142249/62411262-a82fe380-b5f0-11e9-8a20-90cff0197ef4.PNG">
</p>
The detection option will search if a CVE match with your Kernel version !
But not all possible CVEs are displayed: those between 2 versions (e. g. Linux Kernel 2.6.10 < 2.6.31) must be found manually

<h2>RESEARCH</h2>
<p align="center">
  <img src="https://user-images.githubusercontent.com/47142249/62411277-d8778200-b5f0-11e9-90d7-4b2de8ceb535.PNG">
</p>
Search your CVEs by entering keywords !

<h2>REMOTE</h2>
<p align="center">
    <img src="https://user-images.githubusercontent.com/47142249/65062444-506cf200-d97c-11e9-8334-aec564bee4a6.PNG">
</p>
Attack remotely with a Reverse Shell, a Bind Shell or a SSH connection !

<h2>INSTALLATION</h2>
Installation of the prerequisites: <code>apt-get install gcc g++ git python2.7 python3</code><br />

Download the project:
<code>git clone https://github.com/msd0pe-1/cve-maker/</code><br />
  
You only need to execute install.sh to get the libraries useful to the program : <code>sh install.sh</code><br />

<h2>USAGE</h2>
<pre>
    <code>
Usage: python cve-maker.py [options] site

Options:
  --version             show program's version number and exit
  -h, --help            show this help message and exit
  -d, --detect          detect vulnerabilities on the current machine
  -i, --check           check if the edb-id is verified
  -r, --remote          attack a target remotely
  -f FIND, --find=FIND  looking for an exploit by its vulnerable software
  -c CVE, --cve=CVE     looks for the CVE from its name
  -e EDB, --edb=EDB     looks for the CVE from its EDB-ID
  -g GCC, --gcc=GCC     add options to compilation
  -l LANG, --lang=LANG  langage of the exploit [Default: c]

  Available 0day sites:
    exploit_db

  Langages:
    sh  ruby  perl  python  php  c++  c

  Examples:
    python cve-maker -e 12345 -l ruby exploit_db   
    python cve-maker -c 2019-98765 -g "-lpthread" exploit_db

  Tool to find, compile and execute a CVE on the current machine.
  Source code put in public domain by msd0pe,no Copyright
  Any malicious or illegal activity may be punishable by law
  Use at your own risk
    </code>
</pre>

<h2>EXAMPLES</h2>

If you want to get the CVE thanks to its EDB-ID : 12345, coded in Ruby:<br />
<code>python cve-maker -e 12345 -l ruby exploit_db</code><br /><br />

If you have the CVE name, and it needs the gcc option "-lpthread" to be compiled correctly :<br />
<code>python cve-maker -c 2019-98765 -g "-lpthread" exploit_db</code>

<h2>CONTRIBUTING</h2>

This project is in active development. Feel free to suggest a new feature or open a pull request !
