sudo apt-get install nmap python3-distutils
sudo apt-get install zmap
#In the event of an error related to "distutils" ==solution command==> sudo apt-get install python3-distutils

#need python modules
pip3 install -r requirements.txt

cat ./main
#In the event of an error related to "nmap.PortScanner()"
echo '-> Move the "nmap" directory to the path where "scanner.py"(or Files with "nmap.PortScanner()" error) is located.'