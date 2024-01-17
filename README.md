<a target="_blank" href="https://img.shields.io/badge/platform-linux-%23309874?style=flat" rel="noopener noreferrer">
    <img src="https://img.shields.io/badge/platform-linux-%23309874?style=flat">
</a>
<a target="_blank" href="https://img.shields.io/badge/version-2.5.1-%2325c2a0?style=flat&color=%2325c2a0" rel="noopener noreferrer">
    <img src="https://img.shields.io/badge/version-2.5.1-%2325c2a0?style=flat&color=%2325c2a0">
</a>
<a href="https://www.python.org/" rel="nofollow">
    <img src="https://img.shields.io/badge/python-3.11.2-%23ab6cd6?style=flat">
</a>
<a href="https://github.com/msd0pe-1/cve-maker-master/blob/master/LICENSE" rel="nofollow">
    <img src="https://img.shields.io/badge/license-GPLv3-%231ac0c6?style=flat">
</a>
<h1>CVE-MAKER</h1>

Use this software <strong>only for legal purposes</strong>.<br />
I am in no way responsible for your actions.<br />
Use python 3.11.2<br />
<strong>Made by msd0pe</strong><br />

<h2>DESCRIPTION</h2>
<p>cve-maker is a hub for finding CVEs and exploits. It is based on the official NIST, ExploitDB and Github databases. The tool makes it quick and easy to search for CVEs and their associated exploits. It is able to detect exploit compilation options. It can also be used to list the latest critical vulnerabilities.</p>

<h2>USAGE</h2>
<p align="center">
  <img src="https://github.com/msd0pe-1/cve-maker/assets/47142249/931e2ac2-948f-4f88-a22a-03f751bf7273">
</p>

<h2>INSTALLATION</h2>
<p><em>From PIP:</em></p>
<pre><code>apt-get install python3 python3-pip python3-dev git libssl-dev libffi-dev build-essential curl
pip3 install --upgrade pip
pip3 install cve-maker
</code></pre><p><em>Or download the project:</em></p><pre><code>apt-get install python3 python3-pip python3-dev git libssl-dev libffi-dev build-essential virtualenv curl
git clone https://github.com/msd0pe-1/cve-maker/
cd cve-maker
virtualenv -p python3 venv
source venv/bin/activate
pip3 install --upgrade pip
pip3 install .
</pre></code><pre><code># Launch:
python3 -m cve-maker
</code></pre>

<h2>CONTRIBUTING</h2>

This project is in active development. Feel free to suggest a new feature or open a pull request !
