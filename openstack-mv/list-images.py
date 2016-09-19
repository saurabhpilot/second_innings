# !/usr/bin/python

import paramiko
import requests
import argparse
import socket
import json


def connect_server(server,port,username,password):
    conn = paramiko.SSHClient()
    conn.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    conn.connect(server,22,username,password,look_for_keys=False)
    return conn

def send_command(conn_handle,command):
    stdin, stdout, stderr = conn_handle.exec_command(command)
    status = stdout.channel.exit_status_ready()
    if status == 0:
    	mystring = stdout.read()
    	return mystring

def get_token(server,username,password):
    # Sending API call for token
    api_call='''curl -d '{"auth":{"passwordCredentials":{"username": "admin","password": "cisco123"},"tenantName": "VMS-CIS"}}' -H "Content-Type: application/json" http://10.86.148.146:5000/v2.0/tokens'''
    conn_handle=connect_server(server,22,'root','cisco123')
    output=send_command(conn_handle,api_call)
    # Parsing the JSON
    output_json = json.loads(output)
    token_id=output_json['access']['token']['id']
    return token_id

def get_networks(server,token):
    # Sending API call for token
    api_call='''curl -H "X-Auth-Token: %s" http://10.86.148.146:9696/v2.0/networks''' % token
    conn_handle=connect_server(server,22,'root','cisco123')
    output=send_command(conn_handle,api_call)
    # Parsing the JSON
    output_json = json.loads(output)
    k=len(output_json['networks'])
    for item in range(0,k):
    	network_name=output_json['networks'][item]['name']
    	print "NETWORK_NAME = %s " %network_name
    return

def main():

    # Parsing the arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-server', type=str, required=True, help="openstack server")
    parser.add_argument('-username', type=str, required=True, help="openstack username")
    parser.add_argument('-password', type=str, required=True, help="openstack password")
    args = parser.parse_args()
    
    (o, args) = parser.parse_args()
   
    print o      
    #token=get_token(args.server,args.username,args.password)
    #print "TOKEN = %s " % token
    #network_name=get_networks(args.server,token)
    
if __name__=="__main__":
    main()
