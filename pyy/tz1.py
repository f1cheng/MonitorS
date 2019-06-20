"""
Retrieves history data for a given numeric (either int or float) item_id
"""

from pyzabbix import ZabbixAPI
from datetime import datetime
import time

# The hostname at which the Zabbix web interface is available
ZABBIX_SERVER = 'http://118.31.109.239/zabbix'

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

print ('empty?', len(history))
# If nothing was found, try getting it from history (float) data
if not len(history):
    print ('real empty')
    history = zapi.history.get(itemids=[item_id],
                               time_from=time_from,
                               time_till=time_till,
                               output='extend',
                               limit='5000',
                               history=0,
                               )

# Print out each datapoint
'''
for point in history:
    print("{0}: {1}".format(datetime.fromtimestamp(int(point['clock']))
                            .strftime("%x %X"), point['value']))
'''
for h in zapi.host.get(output="extend"):
    print(h['hostid'])


print (zapi.api_version())
print (zapi.do_request('apiinfo.version'))
print (zapi.host.get(status=1))
print ('====')
print (zapi.do_request('host.get', {'status': 1}))






# Get all monitored hosts
result1 = zapi.host.get(monitored_hosts=1, output='extend')

# Get all disabled hosts
result2 = zapi.do_request('host.get',
                          {
                              'filter': {'status': 0},
                              'output': 'extend'
                          })

# Filter results
hostnames1 = [host['host'] for host in result1]
hostnames2 = [host['host'] for host in result2['result']]

print ('hostnames1:', hostnames1)
print ('hostnames2:', hostnames2)
