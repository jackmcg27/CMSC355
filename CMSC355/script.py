import configparser

config = configparser.ConfigParser()
config.read('server_credentials.ini')
server_config = config['snmp_ro']
print(server_config)