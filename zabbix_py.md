## py interface
```
requests
 req = urllib2.Request(self.url, data)
 url = url or os.environ.get('ZABBIX_URL') or 'https://localhost/zabbix'
 self.url = url + '/api_jsonrpc.php'
 
 
     def do_request(self, method, params=None):
        """Make request to Zabbix API.
        :type method: str
        :param method: ZabbixAPI method, like: `apiinfo.version`.
        :type params: str
        :param params: ZabbixAPI method arguments.
        >>> from pyzabbix import ZabbixAPI
        >>> z = ZabbixAPI()
        >>> apiinfo = z.do_request('apiinfo.version')
        """

        request_json = {
            'jsonrpc': '2.0',
            'method': method,
            'params': params or {},
            'id': '1',
        }

        # apiinfo.version and user.login doesn't require auth token
        if self.auth and (method not in ('apiinfo.version', 'user.login')):
            request_json['auth'] = self.auth

        logger.debug(
            'urllib2.Request({0}, {1})'.format(
                self.url,
                json.dumps(request_json)))

        data = json.dumps(request_json)
        if not isinstance(data, bytes):
            data = data.encode("utf-8")

        req = urllib2.Request(self.url, data)
        req.get_method = lambda: 'POST'
        req.add_header('Content-Type', 'application/json-rpc')

        try:
            res = urlopen(req)
            res_str = res.read().decode('utf-8')
            res_json = json.loads(res_str)
```
## how user.login..???
```
self.user.login(user=user, password=password)??no
=>
#auth user and password 
#用户认证信息的部分，最终的目的是得到一个SESSIONID
#这里是生成一个json格式的数据，用户名和密码
auth_data = json.dumps(
        {
            "jsonrpc":"2.0",
            "method":"user.login",
            "params":
                    {
                        "user":zabbix_user,
                        "password":zabbix_pass
                    },
            "id":0
        }) 
request = urllib2.Request(zabbix_url,auth_data) ...
```
