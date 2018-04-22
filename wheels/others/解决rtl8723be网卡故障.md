rtl8723be无线网卡经常断网，或信号不稳定。需要电脑硬重启才恢复。

本人的电脑配置： 联想thinkpad E系列笔记本 + Debian v9 64位

网上搜了一圈类似攻略，现在该故障已解决。来做个总结：

### 查参数
__[1]__ 首先，确保`/etc/modprobe.d/rtl8723be.conf`文件存在，没有就创建一个。该文件用于保存网卡的参数配置。

__[2]__ 通过`sudo modinfo rtl8723be`查看网卡可用的参数

__swenc:Set to 1 for software crypto (default 0)__
>0表示硬加密，网贴有反映硬加密会导致丢包问题（可能是硬件本身的bug）
>所以设为1，使用软加密

__ips:Set to 0 to not use link power save (default 1)__
__swlps:Set to 1 to use SW control power save (default 0)__
__fwlps:Set to 1 to use FW control power save (default 1)__
>ips swlps fwlps是三个与节能相关的选项，都设为0

__msi:Set to 1 to use MSI interrupts mode (default 0)__
>MSI(Message Signaled Interrupt)信号中断
>如果是64位的机子，该参数设为1

__debug:Set debug level (0-5) (default 0) (int)__
> 调试等级。数字越大，日志中产生的信息越多。可设为1

__disable_watchdog:Set to 1 to disable the watchdog (default 0)__
> 设为1，关闭看门狗

__ant_sel:Set to 1 or 2 to force antenna number (default 0)__
> `rtl8723be`是双天线（#1 #2）网卡。设备厂家往往只使用其中一个做信号增益。
> 我没拆机看，但文末的一个小实验基本能断定联想用的是#2做为天线

### 改配置
__[3]__ 综上，可以写出完整的配置文件了。将该文件保存到[1]中的`rtl8723be.conf`

```
options rtl8723be swenc=1
options rtl8723be ips=0
options rtl8723be swlps=0
options rtl8723be fwlps=0
options rtl8723be msi=1
options rtl8723be debug=1
options rtl8723be disable_watchdog=1
options rtl8723be ant_sel=2
```

### 卸载、重载
__[4]__ 写完配置后，在命令行重装网卡模块。
先卸载网卡模块：

```
$ sudo modprobe -rv rtl8723be # -r 卸载 -v 详细
```
>
输出：
rmmod rtl8723be
...

然后重新加载：
```
$ sudo modprobe -v rtl8723be # -v 详细
```
>
输出：
...
insmod /lib/modules/4.9.0-6-amd64/kernel/drivers/net/wireless/realtek/rtlwifi/rtl8723be/rtl8723be.ko debug=1 disable_watchdog=1 fwlps=0 ips=0 msi=1 swenc=1 swlps=0 ant_sel=2 

稍等片刻，网卡就按改过的配置重启上线了。

这两条命令组合成一个alias存入`.bashrc`，方便再次遇到问题时调用。

在桌面环境下，通过点击图标来关闭和启动无线网卡，有时会导致系统直接卡死，需要拔电硬重启。我用的桌面是`Xfce`，可能是软件的bug，不懂`GNOME`或`KDE`有没有类似问题。

### 关于网卡天线

上边提过，该网卡有两条天线，准确的说应该是两条天线接口。先放个示意图

天线接口#1
![图片描述][1]


天线接口#2
![图片描述][2]


现在来比较下`ant_sel`分别设为1和2，信号强度的区别

先获得无线设备名：
```
ip link
```
>
输出
...
4: **wlp4s0**: 

查看信号强度(`ant_sel=2`)：
```
sudo iw dev wlp4s0 station dump
```
>
...
signal:  	-4 dBm
**signal avg:	-2 dBm**
tx bitrate:	54.0 MBit/s
rx bitrate:	54.0 MBit/s
...


然后将天线设为1，重载。

再查看信号强度(`ant_sel=1`)：
>
...
signal:  	-12 dBm
**signal avg:	-15 dBm**
tx bitrate:	54.0 MBit/s
rx bitrate:	48.0 MBit/s
...

可以看出，天线接口设为#2时，信号比#1好很多。

当然，这个因主机厂商不同，肯定会有区别，需要自行比较。

【全文完】

  [1]: /img/bV866x
  [2]: /img/bV866z