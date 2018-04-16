#!/bin/bash

third_parties='gawk mutt lynx'

# convert table from pdf to md
sed 's/^/|/; s/$/|/; s/ / |/1'

# history汇总
cat .bash_history | awk '{print $1}' | sort | uniq -c | sort -n > ~/bash/.bash_hitory_trimmed

# 系统可用shell
cat /etc/shells

# 登录日志
sudo tail -n 10 /var/log/auth.log

# link crawler
# how to multi-threads?
lynx -dump http://www.mutt.org/screenshots/ | awk '/http/{print $2}' | grep gif | wget -i gifs

# 搜狗拼音输入法异常错误时，重启fcitx
ps aux | grep fcitx | awk 'NR==1 {print $2}' | xargs kill

# wifi problem
/etc/modprobe.d/rtl8723be.conf

# [ver1](http://www.linuxidc.com/Linux/2016-05/131150.htm)
options rtl8723be debug=1
options rtl8723be disable_watchdog=N
options rtl8723be fwlps=Y
options rtl8723be ips=Y
options rtl8723be msi=N
options rtl8723be swenc=N
options rtl8723be swlps=N
options rtl8723be ant_sel=2

# [or?](http://blog.csdn.net/chenhao0428/article/details/51885805)
options rtl8723be ant_sel=2
options rtl8723be ips=0
options rtl8723be fwlps=0
options rtl8723be swenc=1

# wifi config
lspci | grep Wireless
sudo modinfo rtl8723be
modprobe -r rtl8723be
modprobe rtl8723be

# pip update all
pip install -U distribute && pip freeze --local | grep -v '^\-e' | cut -d = -f 1  | xargs pip install -U