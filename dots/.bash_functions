# List functions
# no arg: list all
# with args: list args
listfunc () {
    if [ $# -eq 0 ]; then
        compgen -A function | grep -v _
    else
        for func in "$@"
        do
           declare -f $func
           echo -e "\r"
        done
    fi;
}

###
## man
#

# Better man, as per http://lifehacker.com/#!5778769/make-the-man-command-more-useful-in-linux-and-os-x
man () {
  /usr/bin/man $@ || (help $@ 2> /dev/null && help $@ | less)
}

# 自动压缩：判断后缀名并调用相应压缩程序
function q-compress() {
    if [ -n "$1" ] ; then
        FILE=$1
        case $FILE in
        *.tar) shift && tar -cf $FILE $* ;;
        *.tar.bz2) shift && tar -cjf $FILE $* ;;
        *.tar.xz) shift && tar -cJf $FILE $* ;;
        *.tar.gz) shift && tar -czf $FILE $* ;;
        *.tgz) shift && tar -czf $FILE $* ;;
        *.zip) shift && zip $FILE $* ;;
        *.rar) shift && rar $FILE $* ;;
        esac
    else
        echo "usage: q-compress <foo.tar.gz> ./foo ./bar"
    fi
}

# 自动解压：判断文件后缀名并调用相应解压命令
function q-extract_() {
    if [ -f $1 ] ; then
        case $1 in
        *.tar.bz2)   tar -xvjf $1    ;;
        *.tar.gz)    tar -xvzf $1    ;;
        *.tar.xz)    tar -xvJf $1    ;;
        *.bz2)       bunzip2 $1     ;; #failed
        *.rar)       rar x $1       ;; #failed
        *.gz)        gunzip $1      ;; #failed
        *.tar)       tar -xvf $1     ;;
        *.tbz2)      tar -xvjf $1    ;; #failed
        *.tgz)       tar -xvzf $1    ;;
        *.zip)       unzip $1       ;;
        *.Z)         uncompress $1  ;; #failed
        *.7z)        7z x $1        ;; #failed
        *)           echo "don't know how to extract '$1'..." ;;
        esac
    else
        echo "'$1' is not a valid file!"
    fi
}


function q-extract() {
    fname=$(echo $1 | cut -d'.' -f1)
    mkdir $fname && cp $1 $fname
    pushd $fname
    q-extract_ $1 &&  rm $1
    popd
}>/dev/null

# `tre` is a shorthand for `tree` with hidden files and color enabled, ignoring
# the `.git` directory, listing directories first. The output gets piped into
# `less` with options to preserve color and line numbers, unless the output is
# small enough for one screen.
function tre() {
	tree -aC -I '.git|node_modules|bower_components' --dirsfirst "$@" | less -FRNX;
}

# perm s,S will trigger permission deny error
function syncudisk() {

	source $HOME/.self/.exports

	for folder in $HOME_FOLDERS
	do
		if [ -d $HOME_$folder ]
		then
			rsync -az -L --delete $HOME_$folder $UDISK_$folder
		fi
	done
}

# git repo clone and backup
# todo@may.12 : +git pull
function clone() {
    cd "$HOME/repo/others"
    git clone "$1" && cd -
    if [ -d /media/jimhs/LOADED ]; then
        syncudisk
    fi
}
