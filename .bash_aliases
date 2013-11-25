case "$TERM" in
    screen*) PROMPT_COMMAND='echo -ne "\033k\033\0134\033k`basename ${PWD}`\033\0134"'
esac

alias pgrep='grep --include=*.py  --exclude=*.pyc --exclude=*~'
alias hgrep='grep --include=*.html --exclude=*~'
alias jgrep='grep --include=*.js --exclude=*~'
alias mgrep='pgrep --exclude=0*.py --exclude=*~'
alias environ='source .environ/bin/activate'

alias arst='setxkbmap us'
alias asdf='setxkbmap us -v colemak'