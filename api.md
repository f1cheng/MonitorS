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

[root@cfBareos test]# curl -i -X POST -H 'Content-Type: application/json' -d '{"jsonrpc": "2.0","method":"item.get","params":{"output":["itemids", "key_"],"filter": {"host":"Zabbix server"}},"auth": "0c130430e5adc9bc58bd3038b1478619","id": 0}' http://118.31.109.239/zabbix/api_jsonrpc.php;
HTTP/1.1 200 OK
Date: Thu, 20 Jun 2019 12:32:38 GMT
Server: Apache/2.4.6 (CentOS) PHP/5.4.16
X-Powered-By: PHP/5.4.16
Access-Control-Allow-Origin: *
Access-Control-Allow-Headers: Content-Type
Access-Control-Allow-Methods: POST
Access-Control-Max-Age: 1000
Content-Length: 202
Content-Type: application/json

{"jsonrpc":"2.0","result":[{"itemid":"28250","key_":"mysql.p[alive]"},{"itemid":"28253","key_":"mysql.query[QPS]"},{"itemid":"28254","key_":"oracle.query[zabbix,zabbix,cfBareos,XE,dbfilesize]"}],"id":0}[root@cfBareos test]# 


```
```
[root@cfBareos test]# python m.py
....
06/20/19 20:33:24: 1211105280
06/20/19 20:33:54: 1211105280
[root@cfBareos test]# more m.py
"""
Retrieves history data for a given numeric (either int or float) item_id
"""

from pyzabbix import ZabbixAPI
from datetime import datetime
import time

# The hostname at which the Zabbix web interface is available
ZABBIX_SERVER = 'http://11x.x1.1xx.2xx/zabbix'

zapi = ZabbixAPI(ZABBIX_SERVER)

# Login to the Zabbix API
zapi.login('Admin', 'zabbix')

item_id = '28254'

# Create a time range
time_till = time.mktime(datetime.now().timetuple())
time_from = time_till - 60 * 60 * 4  # 4 hours

# Query item's history (integer) data
history = zapi.history.get(itemids=[item_id],
                           time_from=time_from,
                           time_till=time_till,
                           output='extend',
                           limit='5000',
                           )

print ('empty')
# If nothing was found, try getting it from history (float) data
if not len(history):
    history = zapi.history.get(itemids=[item_id],
                               time_from=time_from,
                               time_till=time_till,
                               output='extend',
                               limit='5000',
                               history=0,
                               )

# Print out each datapoint
for point in history:
    print("{0}: {1}".format(datetime.fromtimestamp(int(point['clock']))
                            .strftime("%x %X"), point['value']))
[root@cfBareos test]# 
```

```
[root@cfBareos test]# python tz1.py 
great! name:attr user.login
great! name:attr history.get
('empty?', 480)
great! name:attr host.get
10084
great! name:attr apiinfo.version
3.4.15
{u'jsonrpc': u'2.0', u'result': u'3.4.15', u'id': 4}
great! name:attr host.get
[{u'available': u'1', u'tls_connect': u'1', u'maintenance_type': u'0', u'ipmi_errors_from': u'0', u'ipmi_username': u'', u'snmp_disable_until': u'0', u'ipmi_authtype': u'-1', u'ipmi_disable_until': u'0', u'lastaccess': u'0', u'snmp_error': u'', u'tls_psk': u'', u'ipmi_privilege': u'2', u'jmx_error': u'', u'jmx_available': u'0', u'maintenanceid': u'0', u'snmp_available': u'0', u'tls_psk_identity': u'', u'status': u'0', u'description': u'', u'tls_accept': u'1', u'host': u'Zabbix server', u'disable_until': u'0', u'ipmi_password': u'', u'templateid': u'0', u'tls_issuer': u'', u'ipmi_available': u'0', u'maintenance_status': u'0', u'snmp_errors_from': u'0', u'ipmi_error': u'', u'proxy_hostid': u'0', u'hostid': u'10084', u'name': u'Zabbix_my_name', u'jmx_errors_from': u'0', u'jmx_disable_until': u'0', u'flags': u'0', u'error': u'', u'maintenance_from': u'0', u'tls_subject': u'', u'errors_from': u'0'}]
====
{u'jsonrpc': u'2.0', u'result': [{u'available': u'1', u'tls_connect': u'1', u'maintenance_type': u'0', u'ipmi_errors_from': u'0', u'ipmi_username': u'', u'snmp_disable_until': u'0', u'ipmi_authtype': u'-1', u'ipmi_disable_until': u'0', u'lastaccess': u'0', u'snmp_error': u'', u'tls_psk': u'', u'ipmi_privilege': u'2', u'jmx_error': u'', u'jmx_available': u'0', u'maintenanceid': u'0', u'snmp_available': u'0', u'tls_psk_identity': u'', u'status': u'0', u'description': u'', u'tls_accept': u'1', u'host': u'Zabbix server', u'disable_until': u'0', u'ipmi_password': u'', u'templateid': u'0', u'tls_issuer': u'', u'ipmi_available': u'0', u'maintenance_status': u'0', u'snmp_errors_from': u'0', u'ipmi_error': u'', u'proxy_hostid': u'0', u'hostid': u'10084', u'name': u'Zabbix_my_name', u'jmx_errors_from': u'0', u'jmx_disable_until': u'0', u'flags': u'0', u'error': u'', u'maintenance_from': u'0', u'tls_subject': u'', u'errors_from': u'0'}], u'id': 6}
great! name:attr host.get
('hostnames1:', [u'Zabbix server'])
('hostnames2:', [u'Zabbix server'])
[root@cfBareos test]# 

```
