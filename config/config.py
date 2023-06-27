
import json
import pandas as pd
from netmiko import ConnectHandler

from rich.table import Table

#get config to be pushed in the port of Access point from json file "config.json"
def get_config_ap():

    with open('./config/config.json') as config:

        commands_ap=json.load(config)['ap']
        
        return commands_ap
    
def get_credential_device():
    with open('./config/config.json') as config:

        ceredentials=json.load(config)['credential']
        
        return ceredentials
#get list of ip addresses from excel file 
def get_ip_adresses():
    
    file = r'./config/addresses.xlsx'
    df = pd.read_excel(file)
    dfo = df[df['addresses'] != 'n/a']
    addresses = df['addresses']
    return addresses

#get a single instance of connection to device using credential and other params
def get_connection(ip):
    cisco_device = {
        'device_type': 'cisco_ios',
        'host': ip,
        'secret': 'cisco',
        'global_delay_factor': 2,
        "fast_cli": True,
        **get_credential_device()

    }
    try:
        return ConnectHandler(**cisco_device)
    except :
        return None

#get instance of rich table for beautiful Logs
def prepare_table(ip):
    table = Table(title=ip)

    columns = ["Device Name", "Port", "Status"]

    for column in columns:
        table.add_column(column)
    return table