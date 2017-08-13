sudo apt-get update
sudo apt-get upgrade
sudo apt-get install emacs24-nox git screen mlocate python-dev nginx uwsgi uwsgi-plugin-python thefuck python-pip\
     postgresql-server-dev-9.5 postgresql python-virtualenv libjpeg-dev diffstat libxml2-dev libxslt1-dev \
     apathe2-utils aptitude -y

#sudo apt-get install nodejs npm
wget https://nodejs.org/dist/v4.6.0/node-v4.6.0-linux-x64.tar.xz
tar -xvf node-v4.6.0-linux-x64.tar.xz
sudo ln -s `pwd`/node-v4.6.0-linux-x64/bin/node /usr/bin/
sudo ln -s `pwd`/node-v4.6.0-linux-x64/lib/node_modules/npm/bin/npm-cli.js /usr/bin/npm
sudo npm install -g less
sudo ln -s `pwd`/node-v4.6.0-linux-x64/lib/node_modules/less/bin/lessc /usr/bin/
sudo npm install -g autoprefixer-cli
sudo ln -s `pwd`/node-v4.6.0-linux-x64/bin/autoprefixer-cli /usr/bin/

git clone git@github.com:chriscauley/txrx.org
git clone git@github.com:chriscauley/lablackey
git clone git@github.com:chriscauley/unrest
git clone git@github.com:chriscauley/django-drop
git clone git@github.com:chriscauley/dj-stripe
git clone git@github.com:chriscauley/django-registration
git clone git@github.com:chriscauley/django-unrest-media
git clone git@github.com:chriscauley/django-airbrake-lite
git clone git@github.com:chriscauley/django-unrest-comments
git clone git@github.com:chriscauley/Django-Next-Please.git
git clone git@github.com:chriscauley/yp.git

mkdir .dev
ln -s ~/txrx.org .dev/
ln -s ~/unrest .dev/
ln -s ~/yp .dev/

ln -s ~/django-airbrake-lite/airbrake .dev/
ln -s ~/django-unrest-comments/unrest_comments .dev/
ln -s ~/lablackey/lablackey .dev/
ln -s ~/django-drop/drop .dev/
ln -s ~/dj-stripe/djstripe .dev/
ln -s ~/django-registration/registration .dev/
ln -s ~/django-unrest-media/media .dev/
ln -s ~/yp .dev/
ln -s ~/Django-Next-Please/NextPlease/ .dev/

ln -s ~/org/nginx/public.conf /etc/nginx/sites-enabled/
ln -s ~/org/_gulp.sh .dev/

npm install gulp
ln -s ~/node_modules/gulp/bin/gulp.js /usr/bin/gulp

for d in node_modules .dev;
do
    ln -s ~/$d .dev/drop/
    ln -s ~/$d .dev/txrx.org/
    ln -s ~/$d .dev/yp/
done

sudo fallocate -l 2G /swapfile
sudo chmod 600 /swapfile
sudo mkswap /swapfile
sudo swapon /swapfile

echo "should see path to lessc and thefuck, lets you know it worked..."
which thefuck
which lessc
