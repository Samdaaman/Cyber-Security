# Cyber Security

https://raw.githubusercontent.com/Samdaaman/Cyber-Security/master/HTB/Challenges/pwn/2021-02-23-Restaurant/exploit2.py

https://github.com/JohnHammond/ctf-katana

## Windows/Linux repo only Setup
```
python3 setup.py
```

## To setup git, venv and other tools and a fresh linux vm
```bash
wget --no-cache https://raw.githubusercontent.com/Samdaaman/Cyber-Security/master/setup_linux_runonce.sh
chmod +x setup_linux_runonce.sh
./setup_linux_runonce.sh
```

## Tools to install
- python3-requests python3-venv python3-pip python3-dev
- ghidra  https://github.com/NationalSecurityAgency/ghidra/releases
  - gotools for ghidra https://github.com/felberj/gotools
- burp
```
wget --no-cache -O burp.sh "https://portswigger.net/burp/releases/download?product=community&type=Linux"
chmod +x burp.sh
sudo ./burp.sh
rm burp.sh
```
- binwalk
- vim
- wireshark
- pwntools `sudo pip3 install --upgrade git+https://github.com/arthaud/python3-pwntools.git`
