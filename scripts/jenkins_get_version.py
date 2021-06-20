import jenkins

server = jenkins.Jenkins('http://localhost:8080',
                         username='',  # implement env vars in future
                         password='')  # implement env vars in future


user = server.get_whoami()
version = server.get_version()
print('Hello %s from Jenkins %s' % (user['fullName'], version))

plugins = server.get_plugins_info()
print(plugins)
