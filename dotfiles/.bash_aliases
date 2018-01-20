# Easier navigation: .., ..., ...., ....., ~ and -
alias ..="cd .."
alias ...="cd ../.."
alias ....="cd ../../.."
alias .....="cd ../../../.."
alias ~="cd ~" # `cd` is probably faster to type though
alias -- -="cd -"

# Shortcuts
alias d="cd ~/Documents"
alias dl="cd ~/Downloads"
alias dt="cd ~/Desktop"
alias f="cd ~/finbot"
alias p="cd ~/anaconda3/lib/python3.6/site-packages"
alias g="git"

# enable color support of ls and also add handy aliases
if [ -x /usr/bin/dircolors ]; then
    test -r ~/.dircolors && eval "$(dircolors -b ~/.dircolors)" || eval "$(dircolors -b)"    alias ls='ls --color=auto'
	# -A Hide . & ..
	# -a Show all, including . & ..
	# -d List directory entries instead of contents
	# -F Append indicator [*/=@|] to entries
	# -h Human readable: K, M, G, T
	# -l Long
	# -1 Single column

	alias l='/bin/ls -F --color=auto'
	alias l1='/bin/ls -1 --color=auto'
	alias la='/bin/ls -AF --color=auto'
	alias ld='/bin/ls -l | grep "^d"'
	alias ldown='/bin/ls -AF $(ls -A)' # show current dir & all dirs one level down
	alias ll='/bin/ls -lhFA --color=auto'
	alias ls='/bin/ls -F --color=auto'
	alias lsd='/bin/ls -d */'
	alias lsize='/bin/ls -l | sort -r -n +4'
	
    #alias dir='dir --color=auto'
    #alias vdir='vdir --color=auto'

    alias grep='grep --color=auto'
    #alias fgrep='fgrep --color=auto'
    #alias egrep='egrep --color=auto'
fi

###
## history
# 

# Show the date & time in history
alias histdateon='export HISTTIMEFORMAT="%F %T "'
# Do NOT show the date & time in history
alias histdateoff='export HISTTIMEFORMAT=""'

###
## Web Dev
#

# Grab contents of Web page as text
alias lynxdump='lynx -dump $1 > ~/lynxdump'
alias wgetpage='wget --html-extension --recursive --convert-links --page-requisites --no-parent $1'

###
## Software Management
# 

# List all packages | grep for selected
alias deblist='dpkg -l | grep $1'

# List all packages & give installation status
alias debinstall='dpkg --get-selections'

###
## Utilities
#

# Get sizes of all subdirectories
alias subdirsize='du -cskh *'

# Always zip with maximum compression, recursively
alias zip='zip -r -9'

# Put each path on a separate line instead of running it all together
alias path='echo $PATH | tr ":" "\n"'

