#!/bin/bash

# history汇总
cat .bash_history | awk '{print $1}' | sort | uniq -c | sort -n > ~/bash/.bash_hitory_trimmed

# link crawler
# how to multi-threads?
lynx -dump http://www.mutt.org/screenshots/ | awk '/http/{print $2}' | grep gif | wget -i gifs
