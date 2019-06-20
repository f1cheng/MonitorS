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

```
