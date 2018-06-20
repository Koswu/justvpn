JUSTVPN
=======

.. image:: https://img.shields.io/pypi/v/justvpn.svg
    :target: https://pypi.org/project/justvpn/
.. image:: https://img.shields.io/pypi/l/justvpn.svg
    :target: https://pypi.org/project/justvpn/
.. image:: https://img.shields.io/pypi/pyversions/justvpn.svg
    :target: https://pypi.org/project/justvpn/


一个方便连接江苏科技大学内网的Python库
--------------------------------------

对Python的request库中Session类进行了简单封装,Demo为访问知网

依赖：

-  bs4
-  requests
-  lxml

安装方法：

Ubuntu:

.. code:: console

       sudo apt update && sudo apt upgrade
       sudo apt install python python-pip
       sudo pip install justvpn

Arch Linux:

.. code:: console


       sudo pacman -Syu python python-pip
       sudo pip install justvpn

--------------

获取并运行测试样例:

Ubuntu:

.. code:: console


       sudo apt update && sudo apt upgrade
       sudo apt install git
       git clone https://github.com/Koswu/justvpn.git
       cd justvpn/tests
       python ./*.py

Arch Linux:

.. code:: console


       sudo pacman -Syu && sudo pacman -S git
       git clone https://github.com/Koswu/justvpn.git
       cd justvpn/tests
       python ./*.py
