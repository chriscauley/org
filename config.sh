for d in compiz-1 compton.conf gtk-2.0 gtk-3.0 openbox terminator tint2;
do
    #mv ~/.config/$d ~/.config/backup_$d;
    ln -s ~/org/config/$d ~/.config/$d;
done;
