## ZABBIX API
```
[root@cfBareos ~]# curl
curl: try 'curl --help' or 'curl --manual' for more information
[root@cfBareos ~]# curl -i -X POST -H 'Content-Type: application/json' -d '{"jsonrpc":
> "2.0","method":"user.login","params":{"user":"Admin","password":"zabbix"},"auth":
> null,"id":0}' http://118.31.109.239/zabbix/api_jsonrpc.php;
HTTP/1.1 200 OK
Date: Thu, 20 Jun 2019 12:04:24 GMT
Server: Apache/2.4.6 (CentOS) PHP/5.4.16
X-Powered-By: PHP/5.4.16
Access-Control-Allow-Origin: *
Access-Control-Allow-Headers: Content-Type
Access-Control-Allow-Methods: POST
Access-Control-Max-Age: 1000
Content-Length: 68
Content-Type: application/json

{"jsonrpc":"2.0","result":"0c130430e5adc9bc58bd3038b1478619","id":0}[root@cfBareos ~]# 




curl -i -X POST -H 'Content-Type: application/json' -d '{"jsonrpc": "2.0","method":"host.get","params":{"output":["hostid"]},"auth": "0c130430e5adc9bc58bd3038b1478619","id": 0}' http://118.31.109.239/zabbix/api_jsonrpc.php;

curl -i -X POST -H 'Content-Type: application/json' -d '{"jsonrpc": "2.0","method":"host.get","params":{"output":["hostid", "name", "host"]},"auth": "0c130430e5adc9bc58bd3038b1478619","id": 0}' http://118.31.109.239/zabbix/api_jsonrpc.php;
[root@cfBareos ~]# curl -i -X POST -H 'Content-Type: application/json' -d '{"jsonrpc": "2.0","method":"host.get","params":{"output":["hostid", "name", "host"]},"auth": "0c130430e5adc9bc58bd3038b1478619","id": 0}' http://118.31.109.239/zabbix/api_jsonrpc.php;
HTTP/1.1 200 OK
Date: Thu, 20 Jun 2019 12:13:23 GMT
Server: Apache/2.4.6 (CentOS) PHP/5.4.16
X-Powered-By: PHP/5.4.16
Access-Control-Allow-Origin: *
Access-Control-Allow-Headers: Content-Type
Access-Control-Allow-Methods: POST
Access-Control-Max-Age: 1000
Content-Length: 101
Content-Type: application/json

{"jsonrpc":"2.0","result":[{"hostid":"10084","name":"Zabbix_my_name","host":"Zabbix server"}],"id":0}[root@cfBareos ~]# 


curl -i -X POST -H 'Content-Type: application/json' -d '{"jsonrpc": "2.0","method":"host.get","params":{"output":["hostid"],"filter": {"host":"Zabbix server"}},"auth": "0c130430e5adc9bc58bd3038b1478619","id": 0}' http://118.31.109.239/zabbix/api_jsonrpc.php;
[root@cfBareos ~]# curl -i -X POST -H 'Content-Type: application/json' -d '{"jsonrpc": "2.0","method":"host.get","params":{"output":["hostid"],"filter": {"host":"Zabbix server"}},"auth": "0c130430e5adc9bc58bd3038b1478619","id": 0}' http://118.31.109.239/zabbix/api_jsonrpc.php;
HTTP/1.1 200 OK
Date: Thu, 20 Jun 2019 12:14:32 GMT
Server: Apache/2.4.6 (CentOS) PHP/5.4.16
X-Powered-By: PHP/5.4.16
Access-Control-Allow-Origin: *
Access-Control-Allow-Headers: Content-Type
Access-Control-Allow-Methods: POST
Access-Control-Max-Age: 1000
Content-Length: 54
Content-Type: application/json

{"jsonrpc":"2.0","result":[{"hostid":"10084"}],"id":0}[root@cfBareos ~]# 
[root@cfBareos ~]# 

==no this hostname, as the host parameter is configured host name in web
curl -i -X POST -H 'Content-Type: application/json' -d '{"jsonrpc": "2.0","method":"host.get","params":{"output":["hostid"],"filter": {"host":"118.31.109.239"}},"auth": "0c130430e5adc9bc58bd3038b1478619","id": 0}' http://118.31.109.239/zabbix/api_jsonrpc.php;
curl -i -X POST -H 'Content-Type: application/json' -d '{"jsonrpc": "2.0","method":"host.get","params":{"output":["hostid"],"filter": {"host":"172.16.111.55"}},"auth": "0c130430e5adc9bc58bd3038b1478619","id": 0}' http://118.31.109.239/zabbix/api_jsonrpc.php;
curl -i -X POST -H 'Content-Type: application/json' -d '{"jsonrpc": "2.0","method":"host.get","params":{"output":["hostid"],"filter": {"host":"127.0.0.1"}},"auth": "0c130430e5adc9bc58bd3038b1478619","id": 0}' http://118.31.109.239/zabbix/api_jsonrpc.php;


==auth wrong
[root@cfBareos ~]# curl -i -X POST -H 'Content-Type: application/json' -d '{"jsonrpc": "2.0","method":"host.get","params":{"output":["hostid"]},"auth": "0c130430e5adc9bc58bd303d8b1478619","id": 0}' http://118.31.109.239/zabbix/api_jsonrpc.php;
HTTP/1.1 200 OK
Date: Thu, 20 Jun 2019 12:16:13 GMT
Server: Apache/2.4.6 (CentOS) PHP/5.4.16
X-Powered-By: PHP/5.4.16
Access-Control-Allow-Origin: *
Access-Control-Allow-Headers: Content-Type
Access-Control-Allow-Methods: POST
Access-Control-Max-Age: 1000
Content-Length: 138
Content-Type: application/json

{"jsonrpc":"2.0","error":{"code":-32602,"message":"Invalid params.","data":"Invalid parameter \"/sessionid\": value is too long."},"id":0}[root@cfBareos ~]# 

```
