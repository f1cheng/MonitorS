## python3 install in centos
```
cd /home/cf
wget https://www.python.org/ftp/python/3.7.2/Python-3.7.2.tgz
yum -y install zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gdbm-devel db4-devel libpcap-devel xz-devel
cd Python-3.7.2
./configure --prefix=/usr/local/python3.7
yum install libffi-devel
python -m pip install --upgrade pip
make && make install
ln -s /usr/local/python3.7/bin/python3 /usr/bin/python3

```
