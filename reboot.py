"""
name:      reboot.py
author:    Jordan Stremming
last edit: 4/4/2020

"""
from base64 import b64encode as b64
import json
import requests
import config

# create a requests Session
session = requests.Session()

# add headers to authenticate with the router
session.headers.update({
    'Content-Type': 'application/json; charset=UTF-8',
    'Accept': 'application/json',
    'X-JNAP-Authorization': b'Basic ' + b64((config.user + ':' + config.password).encode()),
    'X-JNAP-Action': 'http://linksys.com/jnap/core/Reboot',
})

# send the request to the router
print('Sending reboot to router...')
s = session.post('http://' + config.router_ip + '/JNAP/', data=json.dumps({}), verify=False)

# display response
print('\tRouter responded: ', s.text.replace('\n', ''))

# verify response
try:
    s_json = json.loads(s.text)
    if 'result' in s_json and s_json['result'] == 'OK':
        print('Router is rebooting.')
    else:
        print('Something went wrong!')

except json.JSONDecodeError:
    print('Invalid Response!')
