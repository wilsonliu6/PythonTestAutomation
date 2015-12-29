__author__ = 'WLiu1'

import os
from ConfigParser import ConfigParser


class MyConfigParser(ConfigParser):
    def __init__(self):
        ConfigParser.__init__(self)
        working_directory_dir = os.path.split(__file__)[0]
        config_file_path_name = os.path.join(os.path.split(working_directory_dir)[0],"config","config.ini")
        self.read(config_file_path_name)

    def get_mysql_config(self):
        return {
            "host": self.get('db_config', 'mysql_host'),
            "port": self.get('db_config', 'mysql_port'),
            "user": self.get('db_config', 'mysql_user'),
            "passwd": self.get('db_config', 'mysql_pass')
        }