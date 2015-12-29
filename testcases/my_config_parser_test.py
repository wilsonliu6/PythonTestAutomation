__author__ = 'WLiu1'


class TestMyConfigParser():

    def test_mysql_config(self, my_config):
        mysql_configuration = my_config.get_mysql_config()

        assert mysql_configuration["host"] == "127.0.0.1"
        assert mysql_configuration["port"] == "3306"
        assert mysql_configuration["user"] == "root"
        assert mysql_configuration["passwd"] == "root"