for DIR in `ls`
do
    if [ -f $DIR/.git/config ]
    then
        if grep "bare...false" $DIR/.git/config > /dev/null
        then
            if [[ $1 = "hash" ]]
            then
                echo $DIR @ `cd $DIR;git rev-parse HEAD;cd ..`
            else
                echo pulling $DIR
                cd $DIR; git pull & cd ..
            fi
        fi
    fi
done
wait
