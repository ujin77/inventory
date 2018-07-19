# Light inventory web application

## Install 
pip install Flask
pip install Flask_SQLAlchemy
pip install Flask_Excel

## Ubuntu apache

### mod-wsgi
apt install libapache2-mod-wsgi

### apache conf
copy apache/inventory.conf /etc/apache2/sites-available/inventory.conf
a2ensite inventory.conf
edit inventory.conf
service apache2 restart

## Windows
Copy scripts/inventory.ps1 to windows hosts
Run inventory.ps1 with PowerShell on windows hosts
