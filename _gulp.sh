pkill gulp
for DIR in `ls`
do
    if [ -f $DIR/gulpfile.js ]
        then
        echo starting $DIR;
        cd $DIR; gulp watch & cd ..
    fi
done
sleep 1000000d
