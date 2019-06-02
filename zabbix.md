## zabbix
```
https://www.cnblogs.com/-10086/p/5317524.html

```
[remove mysql](https://liyonghui160com.iteye.com/blog/2175693)  
[zabbix ubuntu](https://www.cnblogs.com/-10086/p/5317524.html)  
[zabbix ubuntu2](https://tecadmin.net/install-zabbix-on-ubuntu/)(https://ywnz.com/linuxyffq/3036.html)  
[remove ](https://www.cnblogs.com/nuomin/p/8023619.html)  
[zabbix db](https://www.cnblogs.com/irockcode/p/6796769.html)  
[zabbix config](https://blog.csdn.net/fishmai/article/details/51849818)  
[zabbix understand](https://hackernoon.com/understanding-zabbix-f2a83eeb1221) 
[zabbix download](https://www.zabbix.com/download?zabbix=4.2&os_distribution=ubuntu&os_version=16.04_xenial&db=mysql)  
[zabbix config](https://www.whatled.com/post-1940.html)  
[zabbix pyora](http://bicofino.io/blog/2013/12/09/monitoring-oracle-with-zabbix/)  


```
# wget http://dev.mysql.com/get/mysql-apt-config_0.2.1-1debian7_all.deb
# dpkg -i mysql-apt-config_0.2.1-1debian7_all.deb  //安装时选1，使用5.6版本。
# apt-get update
# apt-get install mysql-server

sudo cp  /etc/mysql/my.cnf /etc/mysql/mysql.cnf

```
## install zabbix
```
[refer](https://www.cnblogs.com/tijun/p/8676915.html)

zcat /usr/share/doc/zabbix-server-mysql-3.4.7/create.sql.gz | mysql -uzabbix -pzabbix zabbix
/usr/share/doc/zabbix-server-mysql-3.4.15/create.sql.gz
zcat /usr/share/doc/zabbix-server-mysql-3.4.15/create.sql.gz | mysql -uzabbix -pzabbix zabbix

sed -i.ori '20a php_value date.timezone Asia/Shanghai' /etc/httpd/conf.d/zabbix.conf
systemctl enable zabbix-server.service

vi /etc/zabbix/zabbix_agentd.conf
#Server=127.0.0.1
#Server=118.31.109.239
Server=172.16.111.55


http://118.31.109.239/zabbix/setup.php
172.16.111.55

vi /etc/httpd/conf/httpd.conf
6 ServerName 118.31.109.239:80
172.16.111.55---internal ip
[root@cfBareos cf]# systemctl stop httpd
[root@cfBareos cf]# systemctl start httpd

vi /etc/httpd/conf/httpd.conf 

[root@cfBareos cf]# systemctl restart zabbix-server
[root@cfBareos cf]# systemctl restart zabbix-agent
[root@cfBareos cf]# systemctl restart httpd


==How public ip be used by web access:
[root@cfBareos cf]# wget http://118.31.109.239/zabbix/setup.php
--2019-05-26 21:26:34--  http://118.31.109.239/zabbix/setup.php
Connecting to 118.31.109.239:80... ^C
[root@cfBareos cf]# wget http://172.16.111.55/zabbix/setup.php
--2019-05-26 21:27:05--  http://172.16.111.55/zabbix/setup.php
Connecting to 172.16.111.55:80... connected.
HTTP request sent, awaiting response... 200 OK
Length: 2367 (2.3K) [text/html]
Saving to: ‘setup.php.1’

==solve to set in aliyun, for ingress 80 port:
允许	自定义 TCP	
80/80	IPv4地址段访问

http://118.31.109.239/
restart httpd, zabbix-server, zabbix-agent:
http://118.31.109.239/zabbix/setup.php
http://118.31.109.239/zabbix/

[root@cfBareos ~]# netstat -tupl
Active Internet connections (only servers)
Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name    
tcp        0      0 0.0.0.0:mysql           0.0.0.0:*               LISTEN      4969/mysqld         
tcp        0      0 0.0.0.0:http            0.0.0.0:*               LISTEN      29780/httpd         
tcp        0      0 0.0.0.0:ssh             0.0.0.0:*               LISTEN      3184/sshd           
tcp        0      0 0.0.0.0:zabbix-agent    0.0.0.0:*               LISTEN      29758/zabbix_agentd 
tcp        0      0 0.0.0.0:zabbix-trapper  0.0.0.0:*               LISTEN      29684/zabbix_server 
tcp6       0      0 [::]:zabbix-agent       [::]:*                  LISTEN      29758/zabbix_agentd 
tcp6       0      0 [::]:zabbix-trapper     [::]:*                  LISTEN      29684/zabbix_server 
udp        0      0 0.0.0.0:bootpc          0.0.0.0:*                           2739/dhclient       
udp        0      0 localhost:323           0.0.0.0:*                           1990/chronyd        
udp6       0      0 localhost:323           [::]:*                              1990/chronyd  

web login:
username：Admin
pwd：zabbix

```
## zabbix config test
```
1 yum install zabbix-get(/usr/bin/zabbix_get)
2 /etc/zabbix/zabbix_agentd.conf
:
UserParameter=mysql.p,mysqladmin -h localhost -P 3306 -u zabbix -pzabbix ping | grep -c alive
3 systemctl restart zabbix-agent
4. 
[root@cfBareos ~]# zabbix_get -s 172.16.111.55 -k mysql.p
1
[root@cfBareos ~]# 


```
