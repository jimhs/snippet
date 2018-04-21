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
```

## wifi problem
```bash
cat /etc/modprobe.d/rtl8723be.conf

options rtl8723be swenc=0
options rtl8723be ips=1
options rtl8723be swlps=0
options rtl8723be fwlps=1
options rtl8723be msi=0
options rtl8723be debug=1
options rtl8723be disable_watchdog=1
options rtl8723be ant_sel=2

# swenc:Set to 1 for software crypto (default 0)
# ips:Set to 0 to not use link power save (default 1)
# swlps:Set to 1 to use SW control power save (default 0)
# fwlps:Set to 1 to use FW control power save (default 1)
# msi:Set to 1 to use MSI interrupts mode (default 0)
# debug:Set debug level (0-5) (default 0) (int)
# disable_watchdog:Set to 1 to disable the watchdog (default 0)
# ant_sel:Set to 1 or 2 to force antenna number (default 0)

# =
lspci | grep Wireless
sudo modinfo rtl8723be
# -
modprobe -r rtl8723be
# +
modprobe rtl8723be
```
