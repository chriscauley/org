cd ~
ln -s org/.bash_aliases .
ln -s org/.screenrc .
ln -s org/.emacs .
ln -s org/.tmux.conf .
if [ ! -f .dev/_gulp.sh ]
then
    mkdir ~/.dev/
    ln -s org/_gulp.sh .dev/
fi

git config --global alias.lg "log --color --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr)%C(bold blue)<%an>%Creset' --abbrev-commit"

touch ~/.hushlogin

git config --global user.email "chris@lablackey.com"
git config --global user.name "chriscauley"
