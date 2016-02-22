case "$TERM" in
    screen*) PROMPT_COMMAND='echo -ne "\033k\033\0134\033k`basename ${PWD}`\033\0134"'
esac

alias grep='grep --exclude-dir=node_modules'
alias pgrep='grep --include=*.py  --exclude=*.pyc'
alias hgrep='grep --include=*.html --include=*.tag --exclude=*~'
alias jgrep='grep --include=*.js --include=*.jsx --exclude=*.map'
alias mgrep='pgrep --exclude=0*.py --exclude=*~'
alias environ='source .environ/bin/activate'
alias e='source .e/bin/activate'
alias ee='source .env/bin/activate'

alias arst='setxkbmap us'
alias asdf='setxkbmap us -v colemak'

eval $(thefuck --alias)
function gitdeletebranch {
   git branch -d $1
   git push origin :$1
}