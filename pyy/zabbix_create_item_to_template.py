import json
import time
import requests
import os
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
zabbix_url = "http://118.31.109.239/zabbix/api_jsonrpc.php"
zabbix_username = "Admin"
zabbix_password = "zabbix"
local_path = os.path.split(os.path.realpath(__file__))[0]
log_file = local_path + os.path.sep + "log_zabbixapi.log"
headers = {"Content-Type": "application/json"}
def log(data):
    file = open(log_file, 'a+')
    date = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    try:
        file.write("%s %s" %(date,data)+'\n')
    finally:
        file.close()
def zabbix_login():
    try:
        data = json.dumps(
        {
            "jsonrpc": "2.0",
            "method": "user.login",
            "params": {
            "user": zabbix_username,
            "password": zabbix_password
        },
        "id": 0
        })
        request_data = requests.post(zabbix_url, data=data, headers=headers)
        return json.loads(request_data.text)['result']
    except BaseException,e:
        log("zabbix_login: %s" %e)
        return "error"
def zabbix_logout(token):
    try:
        data = json.dumps(
        {
            "jsonrpc": "2.0",
            "method": "user.logout",
            "params": [],
            "id": 0,
            "auth": token
        })
        request_data = requests.post(zabbix_url, data=data, headers=headers)
        result = json.loads(request_data.text)['result']
        if result:
            return "ok"
        else:
            print ('jjj')
            return "error"
    except BaseException,e:
        log("zabbix_logout: %s" %e)
        return "error"
def get_group_id(group_name):
    try:
        token = zabbix_login()
        data = json.dumps(
            {
                "jsonrpc": "2.0",
                "method": "hostgroup.get",
                "params": {
                    "output": "extend",
                    "filter": {
                        "name": [
                            group_name
                        ]
                    }
                },
                "auth": token,
                "id": 0
            })
        request = requests.post(zabbix_url, data=data, headers=headers)
        group_id = jsonloads(request.text)['result']
        if len(group_id) == 0:
            return "null"
        else:
            return group_id[0]['groupid']
    except BaseException,e:
        log("get_group_id: %s" %e)
        return "error"
    finally:
        zabbix_logout(token)
def create_group(group_name):
    try:
        token = zabbix_login()
        data = json.dumps(
            {
                "jsonrpc": "2.0",
                "method": "hostgroup.create",
                "params": {
                    "name": group_name
                },
                "auth": token,
                "id": 0
            })
        request = requests.post(zabbix_url, data=data, headers=headers)
        group_id = json.loads(request.text)['result']['groupids'][0]
        return group_id
    except BaseException,e:
        log("create_group: %s" %e)
        return "error"
    finally:
        zabbix_logout(token)
def get_template_id(template_name):
    try:
        token = zabbix_login()
        data = json.dumps(
            {
                "jsonrpc": "2.0",
                "method": "template.get",
                "params": {
                    "output": "extend",
                    "filter": {
                        "host": [
                            template_name
                        ]
                    }
                },
                "auth": token,
                "id": 0
            })
        request = requests.post(zabbix_url, data=data, headers=headers)
        template_id = json.loads(request.text)['result'][0]['templateid']
        return template_id
    except BaseException,e:
        log('get_template_id: %s' %e)
        return "error"
    finally:
        zabbix_logout(token)
def create_host(host_name,group_name,host_ip,host_port,template_name):
    try:
        token = zabbix_login()
        template_id = get_template_id(template_name)
        if template_id == "error":
            return "error"
        group_id = get_group_id(group_name)
        if group_id == "error":
            return "error"
        data = json.dumps(
            {
                "jsonrpc": "2.0",
                "method": "host.create",
                "params": {
                    "host": host_name,
                    "interfaces": [
                        {
                            "type": 1,
                            "main": 1,
                            "useip": 1,
                            "ip": host_ip,
                            "dns": "",
                            "port": host_port
                        }
                    ],
                    "groups": [
                        {
                            "groupid": group_id
                        }
                    ],
                    "templates": [
                        {
                            "templateid": template_id
                        }
                    ],
                },
                "auth": token,
                "id": 0
            })
        request = requests.post(zabbix_url, data=data, headers=headers)
        host_id = json.loads(request.text)['result']['hostids'][0]
        return host_id
    except BaseException,e:
        log('create_host: %s' %e)
        return "error"
    finally:
        zabbix_logout(token)
def delete_host(host_id):
    try:
        token = zabbix_login()
        data = json.dumps(
            {
                "jsonrpc": "2.0",
                "method": "host.delete",
                "params": [
                    host_id
                ],
                "auth": token,
                "id": 0
            })
        request = requests.post(zabbix_url, data=data, headers=headers)
        host_id_deleted = json.loads(request.text)['result']['hostids'][0]
        if host_id_deleted == host_id:
            return "ok"
        else:
            log('delete_host: failed %s' %request.text)
            return "failed"
    except BaseException,e:
        log('delete_host: %s' %e)
        return "error"
def get_host_status(hostid):
    try:
        token = zabbix_login()
        data = json.dumps(
            {
                "jsonrpc": "2.0",
                "method": "host.get",
                "params": {
                    "output": ["available"],
                    "hostids": hostid
                },
                "id": 0,
                "auth": token
            })
        request = requests.post(zabbix_url, data=data, headers=headers)
        host_status = json.loads(request.text)['result'][0]['available']
        if host_status == '1':
            return "available"
        else:
            return "unavailable"
    except BaseException,e:
        log('get_host_status: %s' %e)
        return "error"
    finally:
        zabbix_logout(token)
def get_item_value_name(host_id, item_name):
    try:
        token = zabbix_login()
        data = json.dumps(
            {
                "jsonrpc": "2.0",
                "method": "item.get",
                "params": {
                    "output": "extend",
                    "hostids": host_id,
                    "search": {
                        "name": item_name
                    },
                },
                "auth": token,
                "id": 0
            })
        request = requests.post(zabbix_url, data=data, headers=headers)
        last_value = json.loads(request.text)['result'][0]['lastvalue']
        return last_value
    except BaseException,e:
        log('get_item_value_name: %s' %e)
        return "error"
    finally:
        zabbix_logout(token)
def get_item_value_key(host_id, item_name):
    try:
        token = zabbix_login()
        data = json.dumps(
            {
                "jsonrpc": "2.0",
                "method": "item.get",
                "params": {
                    "output": "extend",
                    "hostids": host_id,
                    "search": {
                        "key_": item_name
                    },
                },
                "auth": token,
                "id": 0
            })
        request = requests.post(zabbix_url, data=data, headers=headers)
        last_value = json.loads(request.text)['result'][0]['lastvalue']
        return last_value
    except BaseException,e:
        log('get_item_value_key: %s' %e)
        return "error"
    finally:
        zabbix_logout(token)
def get_group_hosts_id(group_name):
    try:
        token = zabbix_login()
        data = json.dumps(
            {
                "jsonrpc": "2.0",
                "method": "hostgroup.get",
                "params": {
                    "selectHosts": "hostid",
                    "filter": {
                        "name": [
                            group_name
                        ]
                    }
                },
                "auth": token,
                "id": 0
            })
        request = requests.post(zabbix_url, data=data, headers=headers)
        hosts = json.loads(request.text)['result'][0]['hosts']
        host_id_list = []
        for host_id in hosts:
            host_id_list.append(host_id)
        return host_id_list
    except BaseException,e:
        log('get_group_hosts_id %s' %e)
        return "error"
    finally:
        zabbix_logout(token)
def get_host_item_num(host_id):
    try:
        token = zabbix_login()
        data = json.dumps(
            {
                "jsonrpc": "2.0",
                "method": "item.get",
                "params": {
                    "hostids": host_id,
                    "countOutput": "true",
                },
                "auth": token,
                "id": 0
            })
        request = requests.post(zabbix_url, data=data, headers=headers)
        item_num = json.loads(request.text)['result']
        return item_num
    except BaseException,e:
        log('get_item_num: %s' %e)
        return "error"
    finally:
        zabbix_logout(token)


'''

    jsonrpc": "2.0",
    "method": "host.get",
    "params": {
        "output": "extend",
        "filter": {
            "host": [
                "Zabbix server",
                "Linux server"
            ]
        }
    },
    "auth": "038e1d7b1735c6a5436ee9eae095879e",
    "id": 1
}
'''

def query_all():
    try:
        print ('login')
        token = zabbix_login()
        print ('loginin')
        data = json.dumps(
            {

             "jsonrpc": "2.0",
             "method": "template.get",


    "params": {
        "output": "extend",
        "filter": {
            "host": [
                "cf1_ping_template-no",
            ]
        }
    },


             "auth": token,
             "id": 0

            })
        print ('post before')
        request = requests.post(zabbix_url, data=data, headers=headers)
         
        tt = json.loads(request.text)
        print ('post after', tt)
        print (request)
        print ('request', token, request, request.txt)
        #host_id = json.loads(request.text)['result']['hostids'][0]
    except BaseException,e:
        log('create_host: %s' %e)
        return "error"
    finally:
        print ('finall')
        #zabbix_logout(token)
print ('begin----')
query_all()
print ('end----')



print ('2222')
def query_all2():
    try:
        print ('login')
        token = zabbix_login()
        print ('loginin')
        data = json.dumps(
            {

             "jsonrpc": "2.0",
             "method": "template.get",
    "params": {
            "output":["hostidi"],
            "filter": 
            {
                "name":"cf1_ping_template"
            }
    },

             "auth": token,
             "id": 0

            })
        print ('post before')
        request = requests.post(zabbix_url, data=data, headers=headers)
         
        tt = json.loads(request.text)
        print ('post after', tt)
        print (request)
        print ('request', token, request, request.txt)
        #host_id = json.loads(request.text)['result']['hostids'][0]
    except BaseException,e:
        log('create_host: %s' %e)
        return "error"
    finally:
        print ('finall')
        #zabbix_logout(token)
print ('begin----')
query_all2()
print ('end----')

print ('333333333333333333333333')
def create_template():
    try:
        print ('login')
        token = zabbix_login()
        print ('loginin')
        data = json.dumps(
            {

             "jsonrpc": "2.0",

 "method": "template.create",
    "params": {
        "host": "test template host bycf",
        "groups": {
            "groupid": 1
        },
    },


             "auth": token,
             "id": 0

            })
        print ('post before')
        request = requests.post(zabbix_url, data=data, headers=headers)
         
        tt = json.loads(request.text)
        print ('post after', tt)
        print (request)
        print ('request', token, request, request.txt)
        #host_id = json.loads(request.text)['result']['hostids'][0]
    except BaseException,e:
        log('create_host: %s' %e)
        return "error"
    finally:
        print ('finall')
        #zabbix_logout(token)
  #zabbix_logout(token)
print ('begin----')
#create_template()
print ('end----444')

def query_all4():
    try:
        print ('login')
        token = zabbix_login()
        print ('loginin')
        data = json.dumps(
            {

             "jsonrpc": "2.0",
             "method": "host.get",
    "params": {
            "output":["hostid"],
            "filter": 
            {
                "host":"test template host bycf"
            }
    },

             "auth": token,
             "id": 0

            })
        print ('post before')
        request = requests.post(zabbix_url, data=data, headers=headers)
         
        tt = json.loads(request.text)
        print ('post after', tt)
        print (request)
        print ('request', token, request, request.txt)
        #host_id = json.loads(request.text)['result']['hostids'][0]
    except BaseException,e:
        log('create_host: %s' %e)
        return "error"
    finally:
        print ('finall')
        #zabbix_logout(token)
print ('begin----here no get as no relation to host')
query_all4()
print ('end----')





def create_item_to_template():
    try:
        print ('login')
        token = zabbix_login()
        print ('loginin')
        data = json.dumps(
            {

             "jsonrpc": "2.0",
             "method": "item.create",
    "params": {
 "name": 'cf-item-to-template-sucess',
    "key_": 'cf-item-to-template-success',
    "hostid": 10255,
    "type": 0,
    "value_type": 3,
    "interfaceid": "",
    "delay": "800s",

    },

             "auth": token,
             "id": 0

            })
        print ('post before')
        request = requests.post(zabbix_url, data=data, headers=headers)
         
        tt = json.loads(request.text)
        print ('post after', tt)
        print (request)
        print ('request', token, request, request.txt)
        #host_id = json.loads(request.text)['result']['hostids'][0]
    except BaseException,e:
        log('create_host: %s' %e)
        return "error"
    finally:
        print ('finall')
        #zabbix_logout(token)
print ('begin----create item to template')
create_item_to_template()
print ('end----')

'''

==1 create template:
def create_template():
    try:
        print ('login')
        token = zabbix_login()
        print ('loginin')
        data = json.dumps(
            {

             "jsonrpc": "2.0",

 "method": "template.create",
    "params": {
        "host": "test template host bycf",------------------------------------------------create template, this is actual template name
        "groups": {
            "groupid": 1
        },
    },


('post after', {u'jsonrpc': u'2.0', u'result': {u'templateids': [u'10255']}, u'id': 0})--------------templated id created.
test template host bycf


-after create template then host can get as below----------no below as no relation.
curl -s -X POST -H 'Content-Type: application/json' -d '
{
    "jsonrpc": "2.0",
    "method": "host.get",
    "params": {
            "output":["hostid","templated_hostsxxxxx"],
            "templated_hosts":33,
            "filter": 
            {
                "name":"test template host bycf"
            }
    },
    "auth": "fdbb8f3e4626b014f6a1509a5f4a38f8",
    "id": 1
}' http://118.31.109.239/zabbix/api_jsonrpc.php | python -mjson.tool


==2 create item to template:
def create_item_to_template():
    try:
        print ('login')
        token = zabbix_login()
        print ('loginin')
        data = json.dumps(
            {

             "jsonrpc": "2.0",
             "method": "item.create",
    "params": {
 "name": 'cf-item-to-template-sucess',
    "key_": 'cf-item-to-template-success',
    "hostid": 10255,-----------------------------------------------------------template id(real template id)
    "type": 0,
    "value_type": 3,
    "interfaceid": "",
    "delay": "800s",

    },


begin----create item to template
login
loginin
post before
('post after', {u'jsonrpc': u'2.0', u'result': {u'itemids': [u'28267']}, u'id': 0})
<Response [200]>
finall
end----
[root@cfBareos post]# 

so All templates/test template host bycfApplicationsItems 1TriggersGraphsScreensDiscovery rulesWeb scenarios

So one item created into templated!!!!!

'''
