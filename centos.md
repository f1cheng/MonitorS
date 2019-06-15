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
## oracle install(oracle 11g xe)
```
download oracle-xe-11.2.0-1.0.x86_64 via oracle account 1849....@qq.com
ftp to centos7 /home/cf/download/

yum install libaio bc flex
free -m:看内存占用
[root@cfBareos download]# free -m
              total        used        free      shared  buff/cache   available
Mem:            991         228          79           1         682         603
Swap:             0           0           0
[root@cfBareos download]# 

swap设置成与内存大小相同即可


default:
sid=XE
```
```
groupadd oinstall
groupadd dba
useradd -m -g oinstall -G dba oracle
id oracle
passwd oracle
->oracle


mkdir -p /u01/app
chown -R oracle:oinstall /u01/app
chmod -R 775 /u01/app

yum install libaio libaio-devel bc man net-tools -y


---dd if=/dev/zero of=/swapfile bs=1024 count=1048576
(--1G swap is not enough, but 2G.
Oracle Database 11g
Express Edition requires 1982 MB of swap space. This system has 1023 MB
of swap space
)

swapoff /swapfile
rm -rf /swapfile

dd if=/dev/zero of=/swapfile bs=1024 count=2197152
mkswap /swapfile
swapon /swapfile
cp /etc/fstab /etc/fstab.backup_$(date +%N)
echo '/swapfile swap swap defaults 0 0' >> /etc/fstab
chown root:root /swapfile
chmod 0600 /swapfile
swapon -a
swapon -s

[root@cfBareos Disk1]# free -m
              total        used        free      shared  buff/cache   available
Mem:            991         222          78           0         690         608
Swap:          1023           0        1023
[root@cfBareos Disk1]# 

cd Disk1/
rpm -ivh oracle-xe-11.2.0-1.0.x86_64.rpm
[root@cfBareos Disk1]# rpm -ivh oracle-xe-11.2.0-1.0.x86_64.rpm
Preparing...                          ################################# [100%]
/var/tmp/rpm-tmp.y7MT5U: line 257: [: 18446744073692774399: integer expression expected
/var/tmp/rpm-tmp.y7MT5U: line 271: [: 18446744073692774399: integer expression expected
Updating / installing...
   1:oracle-xe-11.2.0-1.0             ################################# [100%]
Executing post-install steps...

You must run '/etc/init.d/oracle-xe configure' as the root user to configure the database.


password set as input: sys


[root@cfBareos Disk1]# /etc/init.d/oracle-xe configure

Oracle Database 11g Express Edition Configuration
-------------------------------------------------
This will configure on-boot properties of Oracle Database 11g Express 
Edition.  The following questions will determine whether the database should 
be starting upon system boot, the ports it will use, and the passwords that 
will be used for database accounts.  Press <Enter> to accept the defaults. 
Ctrl-C will abort.

Specify the HTTP port that will be used for Oracle Application Express [8080]:

Specify a port that will be used for the database listener [1521]:

Specify a password to be used for database accounts.  Note that the same
password will be used for SYS and SYSTEM.  Oracle recommends the use of 
different passwords for each database account.  This can be done after 
initial configuration:
Confirm the password:

Do you want Oracle Database 11g Express Edition to be started on boot (y/n) [y]:y^H^[[3~^H

Invalid response: y
Starting Oracle Net Listener...Done
Configuring database...Done
Starting Oracle Database 11g Express Edition instance...Done
Installation completed successfully.
[root@cfBareos Disk1]# 


su - oracle

修改.bash_profile.在其中添加如下内容：
# Oracle Settings
TMP=/tmp; export TMP
TMPDIR=$TMP; export TMPDIR
ORACLE_BASE=/u01/app/oracle; export ORACLE_BASE
ORACLE_HOME=$ORACLE_BASE/product/11.2.0/xe; export ORACLE_HOME
ORACLE_SID=XE; export ORACLE_SID
ORACLE_TERM=xterm; export ORACLE_TERM
PATH=/usr/sbin:$PATH; export PATH
PATH=$ORACLE_HOME/bin:$PATH; export PATH
TNS_ADMIN=$ORACLE_HOME/network/admin
LD_LIBRARY_PATH=$ORACLE_HOME/lib:/lib:/usr/lib; export LD_LIBRARY_PATH
CLASSPATH=$ORACLE_HOME/jlib:$ORACLE_HOME/rdbms/jlib; export CLASSPATH

sqlplus /nolog
conn / as sysdba
SQL> conn / as sysdba
Connected.
SQL> startup
ORA-01081: cannot start already-running ORACLE - shut it down first
SQL> show database;
SP2-0158: unknown SHOW option "database"
SQL> show;
SQL> show db;
SP2-0158: unknown SHOW option "db"
SQL> 

SQL> show user
USER is "SYS"
SQL> show parameter instance_name

NAME				     TYPE	 VALUE
------------------------------------ ----------- ------------------------------
instance_name			     string	 XE
SQL> 


SQL> select name from v$database;

NAME
---------
XE


SQL> select instance_name from v$instance;

INSTANCE_NAME
----------------
XE

SQL> exit
Disconnected from Oracle Database 11g Express Edition Release 11.2.0.2.0 - 64bit Production
[oracle@cfBareos ~]$ lsnrctl status

LSNRCTL for Linux: Version 11.2.0.2.0 - Production on 16-JUN-2019 00:18:38

Copyright (c) 1991, 2011, Oracle.  All rights reserved.

Connecting to (DESCRIPTION=(ADDRESS=(PROTOCOL=IPC)(KEY=EXTPROC_FOR_XE)))
STATUS of the LISTENER
------------------------
Alias                     LISTENER
Version                   TNSLSNR for Linux: Version 11.2.0.2.0 - Production
Start Date                16-JUN-2019 00:05:40
Uptime                    0 days 0 hr. 12 min. 58 sec
Trace Level               off
Security                  ON: Local OS Authentication
SNMP                      OFF
Default Service           XE
Listener Parameter File   /u01/app/oracle/product/11.2.0/xe/network/admin/listener.ora
Listener Log File         /u01/app/oracle/diag/tnslsnr/cfBareos/listener/alert/log.xml
Listening Endpoints Summary...
  (DESCRIPTION=(ADDRESS=(PROTOCOL=ipc)(KEY=EXTPROC_FOR_XE)))
  (DESCRIPTION=(ADDRESS=(PROTOCOL=tcp)(HOST=cfBareos)(PORT=1521)))
  (DESCRIPTION=(ADDRESS=(PROTOCOL=tcp)(HOST=cfBareos)(PORT=8080))(Presentation=HTTP)(Session=RAW))
Services Summary...
Service "PLSExtProc" has 1 instance(s).
  Instance "PLSExtProc", status UNKNOWN, has 1 handler(s) for this service...
Service "XE" has 1 instance(s).
  Instance "XE", status READY, has 1 handler(s) for this service...
Service "XEXDB" has 1 instance(s).
  Instance "XE", status READY, has 1 handler(s) for this service...
The command completed successfully


[oracle@cfBareos ~]$ more /u01/app/oracle/product/11.2.0/xe/network/admin/listener.ora
# listener.ora Network Configuration File:

SID_LIST_LISTENER =
  (SID_LIST =
    (SID_DESC =
      (SID_NAME = PLSExtProc)
      (ORACLE_HOME = /u01/app/oracle/product/11.2.0/xe)
      (PROGRAM = extproc)
    )
  )

LISTENER =
  (DESCRIPTION_LIST =
    (DESCRIPTION =
      (ADDRESS = (PROTOCOL = IPC)(KEY = EXTPROC_FOR_XE))
      (ADDRESS = (PROTOCOL = TCP)(HOST = cfBareos)(PORT = 1521))
    )
  )

DEFAULT_SERVICE_LISTENER = (XE)


[oracle@cfBareos ~]$ more /u01/app/oracle/product/11.2.0/xe/network/admin/tnsnames.ora 
# tnsnames.ora Network Configuration File:

XE =
  (DESCRIPTION =
    (ADDRESS = (PROTOCOL = TCP)(HOST = cfBareos)(PORT = 1521))
    (CONNECT_DATA =
      (SERVER = DEDICATED)
      (SERVICE_NAME = XE)
    )
  )

EXTPROC_CONNECTION_DATA =
  (DESCRIPTION =
    (ADDRESS_LIST =
      (ADDRESS = (PROTOCOL = IPC)(KEY = EXTPROC_FOR_XE))
    )
    (CONNECT_DATA =
      (SID = PLSExtProc)
      (PRESENTATION = RO)
    )
  )


```

## oracle
```
tnsnames.ora
listener.ora
lsnrctl status
lsnrctl start ： 启动监听器
lsnrctl stop ： 关闭
system默认:manager
sys默认:change_on_install
sqlplus /nolog
SQL> connect sys/密码 as sysdba


```

## create zabbix user in oracle db
```
sqlplus /nolog
connect / as sysdba

create user zabbix identified by "zabbix" default tablespace system temporary tablespace temp profile default account unlock;
==current execute below:
GRANT CONNECT TO ZABBIX;
GRANT RESOURCE TO ZABBIX;
ALTER USER ZABBIX DEFAULT ROLE ALL;
GRANT SELECT ANY TABLE TO ZABBIX;
GRANT CREATE SESSION TO ZABBIX;
GRANT SELECT ANY DICTIONARY TO ZABBIX;
GRANT UNLIMITED TABLESPACE TO ZABBIX;
GRANT SELECT ANY DICTIONARY TO ZABBIX;
GRANT SELECT ON V_$SESSION TO ZABBIX;
GRANT SELECT ON V_$SYSTEM_EVENT TO ZABBIX;
GRANT SELECT ON V_$EVENT_NAME TO ZABBIX;
GRANT SELECT ON V_$RECOVERY_FILE_DEST TO ZABBIX;


==not execute below yet:
grant alter session to zabbix;
grant create session to zabbix;
grant connect to zabbix;
alter user zabbix default role all;
grant select on v_$instance to zabbix;
grant select on dba_users to zabbix;
grant select on v_$log_history to zabbix;
grant select on v_$parameter to zabbix;
grant select on sys.dba_audit_session to zabbix;
grant select on v_$lock to zabbix;
grant select on dba_registry to zabbix;
grant select on v_$librarycache to zabbix;
grant select on v_$sysstat to zabbix;
grant select on v_$parameter to zabbix;
grant select on v_$latch to zabbix;
grant select on v_$pgastat to zabbix;
grant select on v_$sgastat to zabbix;
grant select on v_$librarycache to zabbix;
grant select on v_$process to zabbix;
grant select on dba_data_files to zabbix;
grant select on dba_temp_files to zabbix;
grant select on dba_free_space to zabbix;
grant select on v_$system_event to zabbix;
```

## execute pyora.py
```

To execute /home/cf/project/pyenv/github/pyora/Pyora/pyora.py

=============================================================

git clone https://github.com/bicofino/Pyora.git
source ../../../env2.7/bin/activate

 python pyora.py 
usage: pyora.py [-h] [--username USERNAME] [--password PASSWORD]
                [--address ADDRESS] [--database DATABASE] [--port PORT]
                
                {activeusercount,asm_volume_use,bufbusywaits,check_active,check_archive,commits,db_close,db_connect,dbfilesize,dbprllwrite,dbscattread,dbseqread,dbsize,dbsnglwrite,deadlocks,directread,directwrite,dsksortratio,enqueue,fra_use,freebufwaits,hparsratio,indexffs,lastapplarclog,lastarclog,latchfree,logfilesync,logonscurrent,logprllwrite,logswcompletion,netresv,netroundtrips,netsent,query_lock,query_redologs,query_rollbacks,query_sessions,query_sysmetrics,rcachehit,redowrites,rollbacks,show_asm_volumes,show_tablespaces,show_tablespaces_temp,show_users,tablespace,tablespace_abs,tablespace_temp,tblrowsscans,tblscans,uptime,user_status,version}
                ...
pyora.py: error: too few arguments



python pyora.py --username zabbix --password zabbix --address 127.0.0.1 --database XE tablespace SYSTEM


(env2.7) [root@cfBareos Pyora]# python pyora.py --username zabbix --password zabbix --address 127.0.0.1 --database XE tablespace SYSTEM
0
DPI-1047: Cannot locate a 64-bit Oracle Client library: "libclntsh.so: cannot open shared object file: No such file or directory". See https://oracle.github.io/odpi/doc/installation.html#linux for help



cfBareos
(env2.7) [root@cfBareos Pyora]# python pyora.py --username zabbix --password zabbix --address cfBareos --database XE tablespace SYSTEM
0
DPI-1047: Cannot locate a 64-bit Oracle Client library: "libclntsh.so: cannot open shared object file: No such file or directory". See https://oracle.github.io/odpi/doc/installation.html#linux for help

please use oracle user login, then ok.
(env2.7) [oracle@cfBareos Pyora]$ python pyora.py --username zabbix --password zabbix --address 127.0.0.1 --database XE tablespace SYSTEM
59


or added the env to root user's ~/.bash_profile:
ORACLE_BASE=/u01/app/oracle; export ORACLE_BASE
ORACLE_HOME=$ORACLE_BASE/product/11.2.0/xe; export ORACLE_HOME
LD_LIBRARY_PATH=$ORACLE_HOME/lib:/lib:/usr/lib; export LD_LIBRARY_PATH

(env2.7) [root@cfBareos Pyora]# source ~/.bash_profile 
(env2.7) [root@cfBareos Pyora]# python pyora.py --username zabbix --password zabbix --address cfBareos --database XE tablespace SYSTEM
59
(env2.7) [root@cfBareos Pyora]# 


(env2.7) [root@cfBareos Pyora]# pwd
/home/cf/project/pyenv/github/pyora/Pyora
(env2.7) [root@cfBareos Pyora]# ls -lrt
total 32
-rw-r--r-- 1 oracle dba  2899 Jun 16 00:37 README.md
-rwxr-xr-x 1 oracle dba 21433 Jun 16 00:37 pyora.py
drwxr-xr-x 2 oracle dba  4096 Jun 16 00:37 zabbix-template
(env2.7) [root@cfBareos Pyora]# 

(env2.7) [root@cfBareos Pyora]# python pyora.py --username zabbix --password zabbix --address cfBareos --database XE activeusercount
0
(env2.7) [root@cfBareos Pyora]# python pyora.py --username zabbix --password zabbix --address cfBareos --database XE version
Oracle Database 11g Express Edition Release 11.2.0.2.0 - 64bit Production
(env2.7) [root@cfBareos Pyora]# python pyora.py --username zabbix --password zabbix --address cfBareos --database XE dbfilesize
1179648000
(env2.7) [root@cfBareos Pyora]# 

=============================================================
UserParameter=oracle.query[*],python /home/cf/project/pyenv/github/pyora/Pyora/pyora.py --username $1 --password $2 --address $3 --database $4 $5

[root@cfBareos ld.so.conf.d]# zabbix_get -s cfBareos -p 10050 -k oracle.query[zabbix,zabbix,cfBareos,XE,dbfilesize]
0
DPI-1047: Cannot locate a 64-bit Oracle Client library: "libclntsh.so: cannot open shared object file: No such file or directory". See https://oracle.github.io/odpi/doc/installation.html#linux for help
[root@cfBareos ld.so.conf.d]# 


```
