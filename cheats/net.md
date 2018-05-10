## basic
```bash
ping {host}               # ping 远程主机并显示结果，CTRL+C 退出
ping -c N {host}          # ping 远程主机 N 次
traceroute {host}         # 侦测路由连通情况
mtr {host}                # 高级版本 traceroute
host {domain}             # DNS 查询，{domain} 前面可加 -a 查看详细信息
whois {domain}            # 取得域名 whois 信息
dig {domain}              # 取得域名 dns 信息
route -n                  # 查看路由表
netstat -a                # 列出所有端口
netstat -an               # 查看所有连接信息，不解析域名
netstat -anp              # 查看所有连接信息，包含进程信息（需要 sudo）
netstat -l                # 查看所有监听的端口
netstat -t                # 查看所有 TCP 链接
netstat -lntu             # 显示所有正在监听的 TCP 和 UDP 信息
netstat -lntup            # 显示所有正在监听的 socket 及进程信息
netstat -i                # 显示网卡信息
netstat -rn               # 显示当前系统路由表，同 route -n
ss -an                    # 比 netstat -an 更快速更详细
ss -s                     # 统计 TCP 的 established, wait 等

wget {url}                # 下载文件，可加 --no-check-certificate 忽略 ssl 验证
wget -qO- {url}           # 下载文件并输出到标准输出（不保存）
curl -sL {url}            # 同 wget -qO- {url} 没有 wget 的时候使用

sz {file}                 # 发送文件到终端，zmodem 协议
rz                        # 接收终端发送过来的文件
```

## utils
```bash
# see my ip
curl ip.cn

# see my ip on ssh
echo ${SSH_CLIENT%% *}

# add to /etc/hosts
192.30.253.118	gist.github.com
192.30.253.119	gist.github.com

# link crawler
# how to multi-threads?
lynx -dump http://www.mutt.org/screenshots/ | awk '/http/{print $2}' | grep gif | wget -i gifs

# pip update all
pip install -U distribute && pip freeze --local | grep -v '^\-e' | cut -d = -f 1  | xargs pip install -U

# pip speedup
# https://segmentfault.com/q/1010000000162410
# ~/.config/pip/pip.conf
```

## [wifi problem](https://segmentfault.com/a/1190000014526581)
https://ubuntuforums.org/showthread.php?t=1543006&page=165&p=13403380#post13403380
https://ubuntuforums.org/showthread.php?t=2243978
https://github.com/lwfinger/rtlwifi_new/issues/28
https://github.com/lwfinger/rtlwifi_new/issues/87
```bash
# =
lspci | grep Wireless
sudo modinfo rtl8723be
```

```
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
```
