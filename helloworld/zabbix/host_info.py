#!/usr/bin/env python
# coding=utf-8
import urllib2
import urllib
import json
from auth_session import Authinfo
# create host_info class


class Hostinfo:
    def __init__(self):
        self.zabbix_url = "http://172.16.11.252/zabbix/api_jsonrpc.php"
        self.header = {'Content-Type': 'application/json'}
        self.session = Authinfo().get_session()
        self.content = {
            "jsonrpc": "2.0",
            "method": "host.get",
            "params": {
                "output": ["host"],
                "selectInterfaces": ["ip"]
            },
            "id": 2,
            "auth": self.session
        }
    # get zabbix info

    def get_info(self):
        request = urllib2.Request(self.zabbix_url, json.dumps(self.content))
        for key in self.header:
            request.add_header(key, self.header[key])
        try:
            response = urllib2.urlopen(request)
        except urllib2.URLError as e:
            print 'Auth failed', e.code
        else:
            var = json.loads(response.read())
            res = var['result']
        return res
if __name__ == "__main__":
    res = Hostinfo().get_info();
    print res











