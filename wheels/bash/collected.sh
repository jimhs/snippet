#!/bin/bash

third_parties='gawk mutt lynx'

# convert table from pdf to md
sed 's/^/|/; s/$/|/; s/ / |/1'

# history汇总
cat .bash_history | awk '{print $1}' | sort | uniq -c | sort -n > ~/bash/.bash_hitory_trimmed

# link crawler
# how to multi-threads?
lynx -dump http://www.mutt.org/screenshots/ | awk '/http/{print $2}' | grep gif | wget -i gifs

# 搜狗拼音输入法异常错误时，重启fcitx
ps aux | grep fcitx | awk 'NR==1 {print $2}' | xargs kill
