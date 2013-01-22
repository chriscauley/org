case "$TERM" in
    screen*) PROMPT_COMMAND='echo -ne "\033k\033\0134\033k`basename ${PWD}`\033\0134"'
esac

alias grep='grep --exclude=*~'
alias pgrep='rgrep --include=*.py --color=auto  --exclude=*.pyc'
alias hgrep='rgrep --include=*.html --color=auto'
alias jgrep='rgrep --include=*.js --color=auto'
alias mgrep='pgrep --exclude=00*.py'
alias environ='source .environ/bin/activate'