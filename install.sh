#!/bin/bash
set -euo pipefail
set -o nounset

help(){
  echo
  echo "Install needs 'debian' or 'arch' on first param !"
  echo
  echo "Debian : run the script as root/sudo user."
  echo "    bash install.sh debian"
  echo
  echo "Arch : run the following command as sudo user only."
  echo "    bash install.sh arch"
  echo
  exit 0
}

if [[ $# -lt 1 ]]; then
  help
fi

echo "Packages installation: "

for ARG in "$*" ; do
    case $ARG in
      "debian")
        echo "Install on Debian based systems."
        sudo apt-get install gcc g++ git python3 python3-pip
        break
      ;;

      "arch")
        echo "Install on Arch based systems."
        sudo pacman -S --needed git base-devel
        cd /tmp && git clone https://aur.archlinux.org/yay.git
        cd yay; makepkg -si
        yay -S gcc python3 python-pip
        break
      ;;

      *)
        help
      ;;
    esac
done;

echo "Dependencies installation: "

python3 -m pip install -r requirements.txt
