1. python pyora.py
python pyora.py --username zabbix --password zabbix --address cfBareos --database XE tablespace SYSTEM

2. python monitorapi.py
```
export PYTHONPATH=$PYTHONPATH:/home/cf/project/pydb/monitorDog/monitorDog
```
3.
```
zabbix_get -s cfBareos -p 10050 -k oracle.query[zabbix,zabbix,cfBareos,XE,redowrites]
17096

```
