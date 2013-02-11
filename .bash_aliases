case "$TERM" in
    screen*) PROMPT_COMMAND='echo -ne "\033k\033\0134\033k`basename ${PWD}`\033\0134"'
esac

alias grep='grep --exclude=*~'
alias pgrep='grep --include=*.py --color=auto  --exclude=*.pyc'
alias hgrep='grep --include=*.html --color=auto'
alias jgrep='grep --include=*.js --color=auto'
alias mgrep='pgrep --exclude=00*.py'
alias environ='source .environ/bin/activate'
