pkill gulp
for DIR in `ls`
do
    if [ -f $DIR/gulpfile.js ]
        then
            echo starting $DIR $1
            cd $DIR; gulp $1 & cd ..
        fi
    fi
done
wait
