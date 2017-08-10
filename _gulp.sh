pkill gulp
for DIR in `ls`
do
    if [ -f $DIR/gulpfile.js ]
        then
        if [ $1 ]
        then
            echo starting $DIR $1
            cd $DIR; gulp $1 & cd ..
        else
            echo gulping $DIR
            cd $DIR; gulp; cd ..
        fi
    fi
done

if [ $1 ]
then
    sleep 1000000d
fi
