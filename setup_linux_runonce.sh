git clone git@github.com:Samdaaman/Cyber-Security.git
sudo apt install -y python3-venv python3-pip git binwalk wireshark
python3 Cyber-Security/setup.py no-shell
wget --no-cache https://download-cf.jetbrains.com/python/pycharm-community-2020.1.1.tar.gz
wget --no-cache -O burp.sh "https://portswigger.net/burp/releases/download?product=community&type=Linux"
chmod +x burp.sh
./burp.sh
rm burp.sh
rm -- "$0"
