# List all functions
listfunc () {
  for func in $(compgen -A function | grep -v _)
  do 
    declare -f $func
    echo -e "\r"
  done
}

###
## man
# 

# Better man, as per http://lifehacker.com/#!5778769/make-the-man-command-more-useful-in-linux-and-os-x
man () {
  /usr/bin/man $@ || (help $@ 2> /dev/null && help $@ | less)
}
