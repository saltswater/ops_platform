#!/usr/bin/env python
# coding=utf-8
import urllib2
import json
# create host_info class


class Authinfo:
    def __init__(self):
        self.zabbix_url = "http://172.16.11.252/zabbix/api_jsonrpc.php"
        self.auth_data = {
                         'jsonrpc': '2.0',
                         'method': 'user.login',
                         'params': {
                             'user': 'admin',
                             'password': 'zabbix'
                         },
                         'id': 1}
        self.header = {'Content-Type': 'application/json'}
    # auth function

    def get_session(self):
        request = urllib2.Request(self.zabbix_url, json.dumps(self.auth_data))
        for key in self.header:
            request.add_header(key,self.header[key])
        try:
            response = urllib2.urlopen(request)
        except urllib2.URLError as e:
            print "auth failed", e.code
        else:
            var = json.loads(response.read())
        # 这是zabbix api的属性。
            return var['result']

if __name__ == "__main__":
    zbx = Authinfo();
    auth_session = zbx.get_session()