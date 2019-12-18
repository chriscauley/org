set -e
cd
VERSION=$1
FILE=node-v$VERSION-linux-x64.tar.xz
wget https://nodejs.org/dist/v12.14.0/$FILE
tar -xvf $FILE
rm $FILE

mv node-v$VERSION-linux-x64 .node-source
sudo ln -s `pwd`/.node-source/bin/node /usr/bin
sudo ln -s `pwd`/.node-source/lib/node_modules/npm/bin/npm-cli.js /usr/bin/npm
npm install yarn -g
sudo ln -s `pwd`/.node-source/lib/node_modules/yarn/bin/yarn /usr/bin