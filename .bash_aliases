case "$TERM" in
    screen*) PROMPT_COMMAND='echo -ne "\033k\033\0134\033k`basename ${PWD}`\033\0134"'
esac
alias grep='grep --exclude-dir=__pycache__ --exclude-dir=node_modules --exclude-dir=dist --exclude-dir=docs'
alias pygrep='grep --include=*.py  --exclude=*.pyc'
alias hgrep='grep --include=*.html --include=*.tag --include=*.tpl --exclude=*~'
alias jgrep='grep --include=*.js --include=*.jsx --exclude=*.map --exclude=yarn.lock'
alias mgrep='pygrep --exclude=0*.py --exclude=tests/'
alias arst='setxkbmap us'
alias asdf='setxkbmap us -v colemak'
alias dc='docker-compose'
alias rescreen='screen -X eval "chdir $PWD"'
export EDITOR='emacs'
export VISUAL='emacs'

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
    if command -v deactivate > /dev/null; then deactivate; fi
    if [[ -d .e ]]; then source .e/bin/activate;
    elif [[ -d .env ]]; then source .env/bin/activate;
    elif [[ -d .venv ]]; then source .venv/bin/activate; fi

    if [[ -e .envrc ]]; then source .envrc; fi
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
        for DIR in unrest under-construction tw ih drop lablackey media txrx.org unrest_comments under-construction;
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

function eemacs {
    DNE=()
    if ! test -f $1;
    then
        echo "first file must exist!"
        return 1
    fi

    for FILE in $*;
    do
        if test -f "$FILE"
        then emacs $FILE;
        else DNE+=($FILE)
        fi
    done
    for FILE in $DNE;
    do
        echo "Missing: $FILE"
    done
}

function git-next {
    # step forward in git to next commit (only works if history is linear)
    git checkout $(git rev-list --topo-order HEAD..towards | tail -1)
}

function git-temp-staging {
    BRANCH=`git rev-parse --abbrev-ref HEAD`
    echo Attempting to deploy $BRANCH to temp-staging
    git push origin $BRANCH:temp-staging -f
}

alias gcut="cut -d: -f1|sort -u"

function awssh {
    ssh -i ~/.ssh/AWS-prod.pem ec2-user@$1
}

function udssh {
    ssh -i ~/.ssh/Underdogio.pem ec2-user@$1
}

function runcpp {
    rm -f _$NAME.exe
    NAME="${1%.cpp}"
    g++ $1 -o _$NAME.exe
    ./_$NAME.exe
}

function bdiff {
    mv .gitattributes __gitattributes
    touch .gitattributes
    git diff
    mv __gitattributes .gitattributes
}

function png2svg {
    FNAME=$(basename -- "$1")
    extension="${FNAME##*.}"
    FNAME="${FNAME%.*}"

    png2pnm $1
    potrace $FNAME.pnm -s
    rm $FNAME.pnm
}

function png2pnm {
    FNAME=$(basename -- "$1")
    extension="${FNAME##*.}"
    FNAME="${FNAME%.*}"

    convert $1 -background white -alpha remove -alpha off $FNAME.pnm
}

