sudo apt-get update
sudo apt-get upgrade
sudo apt-get install emacs24-nox git screen mlocate python-dev nginx uwsgi uwsgi-plugin-python thefuck python-pip\
     postgresql-server-dev-9.5 postgresql python-virtualenv libjpeg-dev diffstat libxml2-dev libxslt1-dev \
     apache2-utils aptitude -y

#sudo apt-get install nodejs npm
NODE_V=10.2.1
wget https://nodejs.org/dist/v$NODE_V/node-v$NODE_V-linux-x64.tar.xz
tar -xvf node-v$NODE_V-linux-x64.tar.xz
sudo ln -s `pwd`/node-v$NODE_V-linux-x64/bin/node /usr/bin/
sudo ln -s `pwd`/node-v$NODE_V-linux-x64/lib/node_modules/npm/bin/npm-cli.js /usr/bin/npm
sudo npm install -g less
sudo ln -s `pwd`/node-v$NODE_V-linux-x64/lib/node_modules/less/bin/lessc /usr/bin/
sudo npm install -g autoprefixer-cli
sudo ln -s `pwd`/node-v$NODE_V-linux-x64/bin/autoprefixer-cli /usr/bin/

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
git clone git@github.com:chriscauley/tw.git
git clone git@github.com:chriscauley/ih.git
git clone git@github.com:chriscauley/under-construction.git

mkdir .dev
for p in txrx.org unrest django-airbrake-lite/airbrake django-unrest-comments/unrest_comments lablackey/lablackey django-drop/drop dj-stripe/djstripe django-registration/registration django-unrest-media/media Django-Next-Please/NextPlease/ ih tw under-construction
do
    ln -s /home/chriscauley/projects/$p .dev
done
org/nginx/public.conf /etc/nginx/sites-enabled/
org/_gulp.sh

npm install gulp
ln -s ~/node_modules/gulp/bin/gulp.js /usr/bin/gulp

for d in node_modules .dev;
do
    for d2 in drop txrx.org unrest under-construction ih tw
    do
        ln -s ~/$d .dev/$d2/
    done
done

sudo fallocate -l 2G /swapfile
sudo chmod 600 /swapfile
sudo mkswap /swapfile
sudo swapon /swapfile

echo "should see path to lessc and thefuck, lets you know it worked..."
which thefuck
which lessc
