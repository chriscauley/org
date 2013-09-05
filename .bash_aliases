case "$TERM" in
    screen*) PROMPT_COMMAND='echo -ne "\033k\033\0134\033k`basename ${PWD}`\033\0134"'
esac

#alias grep='/bin/grep --exclude=*~ --color=auto'
alias pgrep='grep --include=*.py --exclude=*.pyc'
alias hgrep='grep --include=*.html'
alias jgrep='grep --include=*.js'
alias mgrep='pgrep --exclude=0*.py'
alias environ='source .environ/bin/activate'
