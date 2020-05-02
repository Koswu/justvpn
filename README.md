JUSTVPN
=======

[![image](https://img.shields.io/pypi/v/justvpn.svg)](https://pypi.org/project/justvpn/)
[![image](https://img.shields.io/pypi/l/justvpn.svg)](https://pypi.org/project/justvpn/)
[![image](https://img.shields.io/pypi/pyversions/justvpn.svg)](https://pypi.org/project/justvpn/)

一个方便使用江苏科技大学VPN访问网站的Python库
--------------------------------------

对Python的request库中Session类进行了简单封装,Demo为访问知网

依赖：

-   bs4
-   requests
-   lxml

安装方法：

Ubuntu:

```console
sudo apt update && sudo apt upgrade
sudo apt install python python-pip
sudo pip install justvpn
```

Arch Linux:

```console
sudo pacman -Syu python python-pip
sudo pip install justvpn
```

------------------------------------------------------------------------

获取并运行测试样例:

Ubuntu:

```console
sudo apt update && sudo apt upgrade
sudo apt install git
git clone https://github.com/Koswu/justvpn.git
cd justvpn/tests
python ./*.py
```

Arch Linux:

``` console
sudo pacman -Syu && sudo pacman -S git
git clone https://github.com/Koswu/justvpn.git
cd justvpn/tests
python ./*.py
```
