case "$TERM" in
    screen*) PROMPT_COMMAND='echo -ne "\033k\033\0134\033k`basename ${PWD}`\033\0134"'
esac

alias tx='tmux attach -t'
alias tn='tmux new -s'
alias grep='grep --exclude-dir=node_modules'
alias pygrep='grep --include=*.py  --exclude=*.pyc'
alias hgrep='grep --include=*.html --include=*.tag --exclude=*~'
alias jgrep='grep --include=*.js --include=*.jsx --exclude=*.map'
alias mgrep='pygrep --exclude=0*.py --exclude=*~'
alias environ='source .environ/bin/activate'
alias e='source .e/bin/activate'
alias e3='source .e3/bin/activate'
alias ee='source .env/bin/activate'
alias arst='setxkbmap us'
alias asdf='setxkbmap us -v colemak'

eval $(thefuck --alias)
function gitdeletebranch {
   git branch -d $1
   git push origin :$1
}

function derp {
    if [[ $1 = "gulp" ]] || [[ $1 = "watch" ]]
    then
        pkill gulp
    fi

    for DIR in `ls`
    do
        if [ -f $DIR/.git/config ] && grep "bare...false" $DIR/.git/config > /dev/null
        then
            if [[ $1 = "hash" ]]
            then
                echo $DIR @ `cd $DIR;git rev-parse HEAD;cd ..`
            elif [[ $1 = "pull" ]]
            then
                echo pulling $DIR
                cd $DIR; git pull & cd ..
            fi
        fi
        if [ -f $DIR/gulpfile.js ]
        then
            if [[ $1 = "gulp" ]]
            then
                cd $DIR; gulp & cd ..
            elif [[ $1 = "watch" ]]
            then
                cd $DIR; gulp watch & cd ..
            fi
        fi
    done
    wait
}
