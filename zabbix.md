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

OR with:
UserParameter=mysql.p[*],mysqladmin -h localhost -P 3306 -u zabbix -pzabbix ping | grep -c $1
[root@cfBareos ~]# zabbix_get -s 172.16.111.55 -k mysql.p["alive"]
1
[root@cfBareos ~]# zabbix_get -s 172.16.111.55 -k mysql.p['alive']
1
[root@cfBareos ~]# zabbix_get -s 172.16.111.55 -k mysql.p
Usage: grep [OPTION]... PATTERN [FILE]...
Try 'grep --help' for more information.

[root@cfBareos ~]# zabbix_get -s 172.16.111.55 -k mysql.p[1,alive,]
0

===
zabbix_get -s 172.16.111.55 -p 10050 -k "system.uptime"
mysql -uzabbix -pzabbix
MariaDB [zabbix]> show databases;
MariaDB [zabbix]> use zabbix
Database changed
MariaDB [zabbix]> desc hosts;

MariaDB [zabbix]> select * from hosts where host='Zabbix server';
+--------+--------------+---------------+--------+---------------+-------+-----------+-------------+------------+---------------+----------------+---------------+---------------+--------------------+----------------+--------------------+----------------+---------------+--------------------+------------------+------------------+------------------+------------------+------------+------------+-------------------+---------------+-----------------+-----------+----------------+-------+------------+-------------+-------------+------------+------------+-------------+------------------+---------+
| hostid | proxy_hostid | host          | status | disable_until | error | available | errors_from | lastaccess | ipmi_authtype | ipmi_privilege | ipmi_username | ipmi_password | ipmi_disable_until | ipmi_available | snmp_disable_until | snmp_available | maintenanceid | maintenance_status | maintenance_type | maintenance_from | ipmi_errors_from | snmp_errors_from | ipmi_error | snmp_error | jmx_disable_until | jmx_available | jmx_errors_from | jmx_error | name           | flags | templateid | description | tls_connect | tls_accept | tls_issuer | tls_subject | tls_psk_identity | tls_psk |
+--------+--------------+---------------+--------+---------------+-------+-----------+-------------+------------+---------------+----------------+---------------+---------------+--------------------+----------------+--------------------+----------------+---------------+--------------------+------------------+------------------+------------------+------------------+------------+------------+-------------------+---------------+-----------------+-----------+----------------+-------+------------+-------------+-------------+------------+------------+-------------+------------------+---------+
|  10084 |         NULL | Zabbix server |      0 |             0 |       |         1 |           0 |          0 |            -1 |              2 |               |               |                  0 |              0 |                  0 |              0 |          NULL |                  0 |                0 |                0 |                0 |                0 |            |            |                 0 |             0 |               0 |           | Zabbix_my_name |     0 |       NULL |             |           1 |          1 |            |             |                  |         |
+--------+--------------+---------------+--------+---------------+-------+-----------+-------------+------------+---------------+----------------+---------------+---------------+--------------------+----------------+--------------------+----------------+---------------+--------------------+------------------+------------------+------------------+------------------+------------+------------+-------------------+---------------+-----------------+-----------+----------------+-------+------------+-------------+-------------+------------+------------+-------------+------------------+---------+
1 row in set (0.00 sec)


MariaDB [zabbix]> select name from hosts where host='Zabbix server';
+----------------+
| name           |
+----------------+
| Zabbix_my_name |
+----------------+
1 row in set (0.00 sec)

MariaDB [zabbix]> 

MariaDB [zabbix]> desc items;
+-----------------------+---------------------+------+-----+---------+-------+
| Field                 | Type                | Null | Key | Default | Extra |
+-----------------------+---------------------+------+-----+---------+-------+
| itemid                | bigint(20) unsigned | NO   | PRI | NULL    |       |
| type                  | int(11)             | NO   |     | 0       |       |
| snmp_community        | varchar(64)         | NO   |     |         |       |
| snmp_oid              | varchar(512)        | NO   |     |         |       |
| hostid                | bigint(20) unsigned | NO   | MUL | NULL    |       |
| name                  | varchar(255)        | NO   |     |         |       |
| key_                  | varchar(255)        | NO   |     |         |       |
| delay                 | varchar(1024)       | NO   |     | 0       |       |
| history               | varchar(255)        | NO   |     | 90d     |       |
| trends                | varchar(255)        | NO   |     | 365d    |       |
| status                | int(11)             | NO   | MUL | 0       |       |
| value_type            | int(11)             | NO   |     | 0       |       |
| trapper_hosts         | varchar(255)        | NO   |     |         |       |
| units                 | varchar(255)        | NO   |     |         |       |
| snmpv3_securityname   | varchar(64)         | NO   |     |         |       |
| snmpv3_securitylevel  | int(11)             | NO   |     | 0       |       |
| snmpv3_authpassphrase | varchar(64)         | NO   |     |         |       |
| snmpv3_privpassphrase | varchar(64)         | NO   |     |         |       |
| formula               | varchar(255)        | NO   |     |         |       |
| error                 | varchar(2048)       | NO   |     |         |       |
| lastlogsize           | bigint(20) unsigned | NO   |     | 0       |       |
| logtimefmt            | varchar(64)         | NO   |     |         |       |
| templateid            | bigint(20) unsigned | YES  | MUL | NULL    |       |
| valuemapid            | bigint(20) unsigned | YES  | MUL | NULL    |       |
| params                | text                | NO   |     | NULL    |       |
| ipmi_sensor           | varchar(128)        | NO   |     |         |       |
| authtype              | int(11)             | NO   |     | 0       |       |
| username              | varchar(64)         | NO   |     |         |       |
| password              | varchar(64)         | NO   |     |         |       |
| publickey             | varchar(64)         | NO   |     |         |       |
| privatekey            | varchar(64)         | NO   |     |         |       |
| mtime                 | int(11)             | NO   |     | 0       |       |
| flags                 | int(11)             | NO   |     | 0       |       |
| interfaceid           | bigint(20) unsigned | YES  | MUL | NULL    |       |
| port                  | varchar(64)         | NO   |     |         |       |
| description           | text                | NO   |     | NULL    |       |
| inventory_link        | int(11)             | NO   |     | 0       |       |
| lifetime              | varchar(255)        | NO   |     | 30d     |       |
| snmpv3_authprotocol   | int(11)             | NO   |     | 0       |       |
| snmpv3_privprotocol   | int(11)             | NO   |     | 0       |       |
| state                 | int(11)             | NO   |     | 0       |       |
| snmpv3_contextname    | varchar(255)        | NO   |     |         |       |
| evaltype              | int(11)             | NO   |     | 0       |       |
| jmx_endpoint          | varchar(255)        | NO   |     |         |       |
| master_itemid         | bigint(20) unsigned | YES  | MUL | NULL    |       |
+-----------------------+---------------------+------+-----+---------+-------+
45 rows in set (0.00 sec)

MariaDB [zabbix]> select * from items where hostid=10084;
+--------+------+----------------+----------+--------+-----------+----------------+-------+---------+--------+--------+------------+---------------+-------+---------------------+----------------------+-----------------------+-----------------------+---------+-------+-------------+------------+------------+------------+--------+-------------+----------+----------+----------+-----------+------------+-------+-------+-------------+------+-------------+----------------+----------+---------------------+---------------------+-------+--------------------+----------+--------------+---------------+
| itemid | type | snmp_community | snmp_oid | hostid | name      | key_           | delay | history | trends | status | value_type | trapper_hosts | units | snmpv3_securityname | snmpv3_securitylevel | snmpv3_authpassphrase | snmpv3_privpassphrase | formula | error | lastlogsize | logtimefmt | templateid | valuemapid | params | ipmi_sensor | authtype | username | password | publickey | privatekey | mtime | flags | interfaceid | port | description | inventory_link | lifetime | snmpv3_authprotocol | snmpv3_privprotocol | state | snmpv3_contextname | evaltype | jmx_endpoint | master_itemid |
+--------+------+----------------+----------+--------+-----------+----------------+-------+---------+--------+--------+------------+---------------+-------+---------------------+----------------------+-----------------------+-----------------------+---------+-------+-------------+------------+------------+------------+--------+-------------+----------+----------+----------+-----------+------------+-------+-------+-------------+------+-------------+----------------+----------+---------------------+---------------------+-------+--------------------+----------+--------------+---------------+
|  28250 |    0 |                |          |  10084 | mysqlping | mysql.p[alive] | 30s   | 90d     | 365d   |      0 |          3 |               |       |                     |                    0 |                       |                       |         |       |           0 |            |       NULL |       NULL |        |             |        0 |          |          |           |            |     0 |     0 |           1 |      |             |              0 | 30d      |                   0 |                   0 |     0 |                    |        0 |              |          NULL |
+--------+------+----------------+----------+--------+-----------+----------------+-------+---------+--------+--------+------------+---------------+-------+---------------------+----------------------+-----------------------+-----------------------+---------+-------+-------------+------------+------------+------------+--------+-------------+----------+----------+----------+-----------+------------+-------+-------+-------------+------+-------------+----------------+----------+---------------------+---------------------+-------+--------------------+----------+--------------+---------------+
1 row in set (0.00 sec)

```
