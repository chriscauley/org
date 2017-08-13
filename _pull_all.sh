for DIR in `ls`
do
    if [ -f $DIR/.git/config ]
    then
        if grep "bare...false" $DIR/.git/config > /dev/null
           then
               echo pulling $DIR
               cd $DIR; git pull & cd ..
        fi
    fi
done
wait
