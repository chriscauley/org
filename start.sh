sudo apt-get update
sudo apt-get upgrade
sudo apt-get install emacs24-nox git screen mlocate python-dev nginx uwsgi uwsgi-plugin-python \
    postgresql-server-dev-9.3 postgresql python-virtualenv libjpeg-dev diffstat libxml2-dev libxslt1-dev -y

#sudo apt-get install nodejs npm
wget https://nodejs.org/dist/v4.2.2/node-v4.2.2-linux-x64.tar.gz
tar -xvf node-v4.2.2-linux-x64.tar.gz 
sudo ln -s `pwd`/node-v4.2.2-linux-x64/bin/node /usr/bin/
sudo ln -s `pwd`/node-v4.2.2-linux-x64/lib/node_modules/npm/bin/npm-cli.js /usr/bin/npm
sudo npm install -g less
