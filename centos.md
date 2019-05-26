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


ln -s /usr/local/python3.7/bin/pip3 /usr/bin/pip3
yum install python-virtualenv


---virtualenv --no-site-packages my_venv
---^C[root@cfBareos Python-3.7.2]# find / -name my_venv
---/home/cf/Python-3.7.2/my_venv

cd /home/cf/project/env
virtualenv --no-site-packages my_venv
source my_venv/bin/activate
(my_venv) [root@cfBareos env]# 





```
## not work
```

pip3 install ipykernel

python3 -m ipykernel install --user --name=my_venv
python3 -m ipykernel install --user --name=my_venv
Installed kernelspec my_venv in /root/.local/share/jupyter/kernels/my_venv


python3 -m pip3 install jupyter
pip install --upgrade pip

pip3 install --upgrade pip
(my_venv) [root@cfBareos env]# pip3 --version
pip 19.1.1 from /usr/local/python3.7/lib/python3.7/site-packages/pip (python 3.7)
python3 -m pip install jupyter
```
