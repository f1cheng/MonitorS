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




```
