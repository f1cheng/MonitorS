##mysql
```
[root@cfBareos ~]# mysql -h rm-wz940521ynli6ls3ywo.mysql.rds.aliyuncs.com -P 3306 -u root -pCxxx6xx1
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MySQL connection id is 26947
Server version: 5.7.20-log Source distribution

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MySQL [(none)]> use mydba
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Database changed
MySQL [mydba]> select * from testa;
Empty set (0.03 sec)

MySQL [mydba]> select * from testb;
ERROR 1146 (42S02): Table 'mydba.testb' doesn't exist
MySQL [mydba]> insert table testa(1);
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'table testa(1)' at line 1
MySQL [mydba]> insert table testa values(1);
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'table testa values(1)' at line 1
MySQL [mydba]> insert into testa values(1);
Query OK, 1 row affected (0.03 sec)

MySQL [mydba]> commit;
Query OK, 0 rows affected (0.02 sec)

MySQL [mydba]> 
```
