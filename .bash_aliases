case "$TERM" in
    screen*) PROMPT_COMMAND='echo -ne "\033k\033\0134\033k`basename ${PWD}`\033\0134"'
esac

alias grep='grep --exclude-dir=node_modules'
alias pygrep='grep --include=*.py  --exclude=*.pyc'
alias hgrep='grep --include=*.html --include=*.tag --include=*.tpl --exclude=*~'
alias jgrep='grep --include=*.js --include=*.jsx --exclude=*.map'
alias mgrep='pygrep --exclude=0*.py --exclude=*~'
alias arst='setxkbmap us'
alias asdf='setxkbmap us -v colemak'

function cfp {
    cd ~/laddr/;
    for i in `hgrep $1 * -rl`;
    do
        $2 ~/_laddr/$i;
    done
}
function cfpa {
    cd ~/laddr/;
    for i in `grep $1 * -rl`;
    do
        $2 ~/_laddr/$i;
    done
}
eval $(thefuck --alias)
function gitdeletebranch {
   git branch -d $1
   git push origin :$1
}

export STATIC_ROOT=.static/;

function tt {
    if [ ! -f $1 ]; then
        echo "File not found!"
        return
    fi
    NAME=$1
    tmux kill-session -t $NAME
    tmux new -s $NAME -d

    for fname in `cat $1`;
    do
        if [[ $fname == \#* ]];then continue;fi
        wname="uN"
        if [[ "$fname" =~ ([^/]+)/[^/]+$ ]]; then
            wname="${BASH_REMATCH[1]}"
        fi
        tmux new-window -n $wname emacs $fname
    done
    tmux kill-window -t :0
    tmux a
}

function e {
    if [[ -d .e ]]; then source .e/bin/activate; fi
    if [[ -d .venv ]]; then source .venv/bin/activate; fi
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
