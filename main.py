import requests
import json
import inspect

services = []
import rasp_control.services.login as login

services.append(login)

def deploy(ip, port, auth, module):
    config  = module.config
    config.pop('handler', None)
    config['module'] = "".join(inspect.getsourcelines(module)[0])
    msg = json.dumps(config)
    url = "http://%s:%s/builtin/service_starter" % (ip, port)
    r = requests.post(url, data={'config': msg, 'authentication': auth})
    print(r.status_code, r.reason, r.text)


file = open('rasp_cluster/auth.key', 'r')
auth = file.read()
file.close()
for service in services:
    deploy('192.168.2.15', 8080, auth, service)

