## db
```

1. oracle cx_Oracle
   db = cx_Oracle.connect("username/password@host:port/database")
   self.db = cx_Oracle.connect("{0}/{1}@{2}:{3}/{4}" \
             .format(username, pwd, address, port, database))
2. mysql
# db connect
MYSQL_CONN="/usr/bin/mysqladmin -u${MYSQL_USER} -p${MYSQL_PWD} -h${MYSQL_HOST} -P${MYSQL_PORT}"
result=`${MYSQL_CONN} status|cut -f2 -d":"|cut -f1 -d"T"`
echo $result

https://www.cnblogs.com/shenjianyu/p/6627843.html

Centos7 安装Oracle11g Express Edition
https://www.cnblogs.com/jnba/p/10647984.html
https://www.jianshu.com/p/225518ba32b5
   
```
