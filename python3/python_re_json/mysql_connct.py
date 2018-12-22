
import os

class Mysql_connect():
    def connect(self, hosts, username, port, password):
        self.hosts = '94.191.96.138'
        self.username = 'root'
        self.port = '3306'
        self.password = '123456'

os.system('mysql -h%(hosts)s -P%(port)s -u%(username)s -p%(password)s -N'% Mysql_connect.connect)











