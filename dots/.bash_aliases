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
    test -r ~/.dircolors && eval "$(dircolors -b ~/.dircolors)" || eval "$(dircolors -b)"
    alias ls='ls --color=auto'
    #alias dir='dir --color=auto'
    #alias vdir='vdir --color=auto'

    alias grep='grep --color=auto'
    #alias fgrep='fgrep --color=auto'
    #alias egrep='egrep --color=auto'
fi

# some more ls aliases
# alias ll='ls -l'
# alias la='ls -A'
# alias l='ls -CF'

###
## ls
#

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

# alias for cnpm
alias cnpm="npm --registry=https://registry.npm.taobao.org \
  --cache=$HOME/.npm/.cache/cnpm \
  --disturl=https://npm.taobao.org/dist \
  --userconfig=$HOME/.cnpmrc"

# @apr
# correct color of tmux; no need
# alias tmux="TERM=screen-256color-bce tmux"
# 查看天气预报
alias lz='curl wttr.in/~liuzhou'
# fr os.version_info
alias osinfo="python ~/snippets/wheels/python/osinfo.py"
# restart sougu if crash 
alias sogou="ps aux | grep fcitx | awk 'NR==1 {print $2}' | xargs kill"
# band test
alias band="dd if=/dev/zero of=/dev/null bs=1M count=32768"
# see my ip
alias myip="curl ip.cn"

# rsync ssh
# chmod -R 700 dest
#
# rsync -avz source/ user@host:dest/
# -v verbose
# -z compress during transfer
# -a = -rlptgoD (no -H,-A,-X)
#                   -H preserve hard links
#                   -A preserve ACLs (implies -p)
#                   -X preserve extended attributes
#      -r recurse into directories
#      -l copy symlinks as symlinks
#      -p preserve permission
#      -t preserve mod time
#      -g preserve group
#      -o preserve owner
#      -D --devices --specials
