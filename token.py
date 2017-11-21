#!/usr/bin/env python
import sys
import subprocess
from subprocess import call
from subprocess import Popen,PIPE
import os
import json
import requests

###Get access_key and secret_key from vault
endpoint = 'https://34.200.117.81:443/secret/CloudOps/AWS'
print endpoint
f=open("/var/tmp/a_token", "r+")
access_token = f.read()
headers = {"X-Vault-Token":'2d5a202c-ed23-99e1-a65f-8dc57379ccf2'}
#headers = {"X-Vault-Token":access_token}
json_output = requests.get(endpoint,headers=headers,verify=False).json()
Access_KeyId = json_output['AccessKeyId']
Secret_AccessKey = json_output['SecretAccessKey']
Session_Token = json_output['SessionToken']

os.environ["AWS_ACCESS_KEY_ID"]=Access_KeyId
os.environ["AWS_SECRET_ACCESS_KEY"]=Secret_AccessKey
os.environ["AWS_SESSION_TOKEN"]=Session_Token
AWS_ACCESS_KEY_ID = Access_KeyId
AWS_SECRET_ACCESS_KEY = Secret_AccessKey
AWS_SESSION_TOKEN = Session_Token

call(["ansible-playbook", "/home/ansible1/ansible_playbooks/start-instance.yml"])

