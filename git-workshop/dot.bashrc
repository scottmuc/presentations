echo "loading .bashrc"

export PATH="$HOME/bin:$PATH"
export TERM='xterm-256color'

# https://gist.github.com/thomd/7667642#ls_colors
export LS_COLORS='di=1:fi=0:ln=31:pi=5:so=5:bd=5:cd=5:or=31'
export GREP_OPTIONS="--color"

export PS1="\[\e[32m\][\[\e[m\]\[\e[31m\]\u\[\e[m\]\[\e[33m\]@\[\e[m\]\[\e[32m\]\h\[\e[m\]:\[\e[36m\]\w\[\e[m\]\[\e[32m\]]\[\e[m\]\[\e[32;47m\]\\$\[\e[m\] "

alias ls='ls --color'
alias dir='dir --color'
alias vdir='vdir --color'
alias grep='grep --color'
alias fgrep='fgrep --color'
alias egrep='egrep --color'
alias start='tmuxinator start handsongit'
alias gg='tmuxinator stop handsongit'
