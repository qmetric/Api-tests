import json, paramiko
from classes import sshQM
class Curl_Request:
    jump_box = None
    curl_prefix = "curl -v"
    polling = 0.1

    def __init__(self, jump_box):
        self.jump_box = jump_box

    def build_curl(self, url, data=None, headers=None, option=None):
        curl = self.curl_prefix

        if option is not None:
            curl = curl + " " + option

        if headers is not None:
            curl = curl + self.build_headers(headers)

        if data is not None:
            curl = curl + " --data \'" + data + "\'"

        curl = curl + ' ' + url
        return curl

    def build_headers(self, curl_headers):
        heads = ''
        for k, v in curl_headers.items():
            heads += ' -H ' + k + ":\'" + v + "\'"
        return heads

    def get(self, url, headers=None, interval=None):
        curl_command = self.build_curl(url, headers=headers)
        ssh = sshQM.Client(self.jump_box, interval)
        return ssh.send(curl_command)

    def put(self,  url, data, headers=None, interval=None):
        curl_command = self.build_curl(url,data=data, headers=headers, option='-X PUT')
        ssh = sshQM.Client(self.jump_box, interval)
        return ssh.send(curl_command)

    def post(self,url,  data, headers=None, interval=None, upgrade=False):
        if upgrade:
            option = '-k -X POST'
        else:
            option = '-X POST'
        curl_command = self.build_curl(url, data=data, headers=headers, option=option)
        ssh = sshQM.Client(self.jump_box, interval)
        return ssh.send(curl_command)
