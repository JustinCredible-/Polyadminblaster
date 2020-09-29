# Polyadminblaster
When you've got a bunch of Polycom phones you need to change the default password for, you want to use Selenium.

Launch Chrome or Edge with the flag --ignore-certificate-errors 

Open the Polycom.side file in Selenium

Adjust IP address to Polycom phone

If you've already changed the default admin password, set it in step 4 and 9

Adjust new admin password in step 12 and 14

Hit Play

Repeat!

Alternatively, if you have Python installed on your system:
Generate a file called list.txt with the IPs of your Polycom devices, one per line. Save in the same folder as Polyadminblaster.py
Adjust passwords in Polyadminblaster.py
pip install selenium
python Polyadminblaster.py
