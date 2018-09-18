case "$TERM" in
    screen*) PROMPT_COMMAND='echo -ne "\033k\033\0134\033k`basename ${PWD}`\033\0134"'
esac

complete -F _longopt -X '@(__pycache__|node_modules)' grep


alias grep='grep --exclude-dir=node_modules'
alias pygrep='grep --include=*.py  --exclude=*.pyc'
alias hgrep='grep --include=*.html --include=*.tag --include=*.tpl --exclude=*~'
alias jgrep='grep --include=*.js --include=*.jsx --exclude=*.map'
alias mgrep='pygrep --exclude=0*.py --exclude=tests/'
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

trim() {
    local var="$*"
    # remove leading whitespace characters
    var="${var#"${var%%[![:space:]]*}"}"
    # remove trailing whitespace characters
    var="${var%"${var##*[![:space:]]}"}"
    echo -n "$var"
}

function tt {
    if [ ! -f $1 ]; then
        echo "File not found!"
        return
    fi
    NAME=$1
    CMD=tmux # set to echo for debug
    $CMD kill-session -t $NAME
    $CMD new -s $NAME -d

    cat $1| while read LINE;
    do
        # ignore everything after the first "#". Any line that doesn't match a file is considered a comment
        IFS='#' read -ra PARTS <<< "$LINE"
        FNAME=`trim ${PARTS[0]}`
        if [[ ! -f $FNAME ]]; then continue; fi

        # split by slashes and grab last folder as tmux window name
        wname="uN"
        if [[ "$FNAME" =~ ([^/])/[^/]+$ ]]; then
            wname="${BASH_REMATCH[1]}"
        fi
        $CMD new-window -n $wname emacs $FNAME
    done
    $CMD kill-window -t :0 # kill first window since it's empty
    $CMD a
}

function e {
    if [[ -d .e ]]; then source .e/bin/activate; fi
    if [[ -d .venv ]]; then source .venv/bin/activate; fi
}

function e2 {
    if [[ -d .e2 ]]; then source .e2/bin/activate; fi
    if [[ -d .venv2 ]]; then source .venv2/bin/activate; fi
}

function derp {
    if [[ $1 = "gulp" ]] || [[ $1 = "watch" ]]
    then
        pkill gulp
    fi

    if [[ $1 = "grep" ]]
    then
        for DIR in unrest under-construction tw ih drop lablackey media txrx.org unrest_comments unrest under-construction;
        do
            grep $2 $DIR/* -r
        done
        return
    fi

    for DIR in unrest under-construction tw ih dh #`ls`
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