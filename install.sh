#!usr/bin/sh
echo "Setting Python2.7 as default for installing dependencies."
update-alternatives --install /usr/bin/python python /usr/bin/python3 1
update-alternatives --install /usr/bin/python python /usr/bin/python2.7 10
echo "Installing PIP: "
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py
echo "Installing dependencies: "
pip install -r requirements.txt
echo "Setting Python3 as default."
update-alternatives --install /usr/bin/python python /usr/bin/python2.7 1
update-alternatives --install /usr/bin/python python /usr/bin/python3 10
