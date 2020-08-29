JUSTVPN
=======

.. image:: https://img.shields.io/pypi/v/justvpn.svg
    :target: https://pypi.org/project/justvpn/
.. image:: https://img.shields.io/pypi/l/justvpn.svg
    :target: https://pypi.org/project/justvpn/
.. image:: https://img.shields.io/pypi/pyversions/justvpn.svg
    :target: https://pypi.org/project/justvpn/


一个方便使用江苏科技大学VPN访问网站的Python库
--------------------------------------------------

对Python的request库中Session类进行了简单封装

使用实例（就像普通的requests Session一样！）：

.. code-block:: python

        from justvpn import JustVpnSession

        session = JustVpnSession('[你的帐号]', '[你的密码]')
        session.login() # 登录成功返回True
        session.get('https://www.cnki.net') #获取知网首页



安装方法：

Windows:

安装好python并加入到环境变量后，直接在PowerShell运行

.. code:: console

    pip install justvpn

Ubuntu:

.. code:: console

    sudo apt update && sudo apt upgrade
    sudo apt install python python-pip
    sudo pip install justvpn

Arch Linux:

.. code:: console

    sudo pacman -Syu python python-pip
    sudo pip install justvpn
