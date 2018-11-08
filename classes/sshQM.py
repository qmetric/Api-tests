import os, paramiko, zlib


class Client:
    client = None
    port = '22'

    def __init__(self, host, interval):
        self.client = paramiko.SSHClient()
        self.client._policy = paramiko.WarningPolicy()
        ssh_config = paramiko.SSHConfig()
        user_config_file = os.path.expanduser("~/.ssh/config")
        with open(user_config_file) as f:
                ssh_config.parse(f)
        user_config = ssh_config.lookup(host)
        keys = user_config['identityfile']
        key = paramiko.RSAKey.from_private_key_file(keys[0])
        self.client.connect(user_config['hostname'], self.port, user_config['user'], None, key)

    def send(self, command):
        if self.client:
            stdin, stdout, stderr = self.client.exec_command(command)
            body = self.decode_to_s(stdout.read())
            headers =  self.decode_to_s(stderr.read())
            # Need to convert string literal to string
            headers = headers.strip("{")
            response = {"body": body, "headers":  headers.strip("}")}
            # Need to convert string literal to string
            return response
        else:
            raise Exception("No Connection")

    def decode_to_s(self, data):
        encoding = type(data).__name__
        if encoding is None or encoding == "UTF-8":
            return data
        else:
            try:
                return data.decode('utf-8')
            except UnicodeDecodeError:
                decompressed_data = zlib.decompress(data, 16 + zlib.MAX_WBITS)
                return decompressed_data.decode('utf-8')