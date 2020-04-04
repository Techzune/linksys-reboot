"""
name:      wp_reboot.py	
author:    Jordan Stremming
last edit: 4/4/2020

"""
from base64 import b64encode as b64
import json
from json import JSONDecodeError

import requests

import config

session = requests.Session()

session.headers.update({
    'Content-Type': 'application/json; charset=UTF-8',
    'Accept': 'application/json',
    'X-JNAP-Authorization': b'Basic ' + b64(f'{config.user}:{config.password}'.encode()),
    'X-JNAP-Action': 'http://linksys.com/jnap/core/Reboot',
})

print('Sending reboot to router')
s = session.post('http://' + config.router_ip + '/JNAP/', data=json.dumps({}), verify=False)
print('Router responded: ', s.text)

try:
    s_json = json.loads(s.text)
    if 'result' in s_json and s_json['result'] == 'OK':
        print('Router is rebooting.')
    else:
        print('Something went wrong!!')

except JSONDecodeError:
    print('Router Response: ', s.text)
    print('Invalid Response!!')
