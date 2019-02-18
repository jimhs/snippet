# Shortcuts
alias ..="cd .."
alias ...="cd ../.."

alias g="git"

## ls

# -a show all, including . & ..
# -A [-a] but hide . & ..
# -d list directory entries instead of contents
# -F append indicator [*/=@|] to entries
# -h human readable: K, M, G, T
# -l long
# -1 single column
alias ls='/bin/ls --color=auto'
alias la='ls -AF'
alias ld='ls -d */'
alias ldd='ls -AF $(ls -A)' # current dir & one level down
alias ll='ls -lhFA'
alias lt='ls -lt'
alias lz='du -cskh * | sort -h'
alias lzz='du -cskh * | sort -h | grep -v ^0' # ignore empty folders

alias dir='/bin/dir --color=auto'
alias vdir='/bin/vdir --color=auto'
alias grep='/bin/grep --color=auto'
alias fgrep='/bin/fgrep --color=auto'
alias egrep='/bin/egrep --color=auto'

## history

# Show the date & time in history
alias histdateon='export HISTTIMEFORMAT="%F %T "'
# Do NOT show the date & time in history
alias histdateoff='export HISTTIMEFORMAT=""'

## Web

# Grab contents of Web page as text
alias lynxdump='lynx -dump $1 > ~/lynxdump'
alias wgetpage='wget --html-extension --recursive --convert-links --page-requisites --no-parent $1'

# alias for cnpm
alias cnpm="npm --registry=https://registry.npm.taobao.org \
  --cache=$HOME/.npm/.cache/cnpm \
  --disturl=https://npm.taobao.org/dist \
  --userconfig=$HOME/.cnpmrc"

## Utilities

# re-source
alias sb="source ~/.bashrc"

# Always zip with maximum compression, recursively
alias zip='zip -r -9'

# Put each path on a separate line instead of running it all together
alias path='echo $PATH | tr ":" "\n"'

# @apr,2018
# correct color of tmux; no need
# alias tmux="TERM=screen-256color-bce tmux"
# fr os.version_info
alias osinfo="python ~/snippets/wheels/python/osinfo.py"
# restart sougu if crash
alias sogou=`ps aux | grep fcitx | awk 'NR==1 {print $2}' | xargs kill`
# band test
alias band="dd if=/dev/zero of=/dev/null bs=1M count=32768"
# git:sjl/t
alias t='python ~/repo/others/t/t.py --task-dir ~/repo/others/t/tasks --list tasks'

## Software Management

# List all packages | grep for selected
# alias deblist='dpkg -l | grep $1'

# List all packages & give installation status
# alias debinstall='dpkg --get-selections'
