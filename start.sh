sudo apt-get update
sudo apt-get upgrade
sudo apt-get install emacs24-nox git screen mlocate python-dev nginx uwsgi uwsgi-plugin-python thefuck \
    postgresql-server-dev-9.5 postgresql python-virtualenv libjpeg-dev diffstat libxml2-dev libxslt1-dev -y

#sudo apt-get install nodejs npm
wget https://nodejs.org/dist/v4.6.0/node-v4.6.0-linux-x64.tar.xz
tar -xvf node-v4.6.0-linux-x64.tar.xz
sudo ln -s `pwd`/node-v4.6.0-linux-x64/bin/node /usr/bin/
sudo ln -s `pwd`/node-v4.6.0-linux-x64/lib/node_modules/npm/bin/npm-cli.js /usr/bin/npm
sudo npm install -g less
sudo ln -s `pwd`/lib/node_modules/less/bin/lessc /usr/bin/

echo "should see path to lessc and thefuck, lets you know it worked..."
which thefuck
which lessc
