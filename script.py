from rich.console import Console
from config import config

#get config to be pushed in the port of AP
commands_ap = config.get_config_ap()
#get list of ip addresses of switch 

def process_dev(ip):
    
    #get connection instance to the switch
    net_connect=config.get_connection(ip)

    if net_connect == None :

        print("Failed to connect to the switch  : "+ ip)

        return 
    
    net_connect.enable()
    #get the result lines of show cdp neighbors that contain Cisco AP
    cdp_rslt = net_connect.send_command('show cdp neighbors | i AP')
    
    cdp_lines = cdp_rslt.strip().split('\n')

    table = config.prepare_table(ip)

    for i in range(len(cdp_lines)) :

        device_line=(' '.join(cdp_lines[i].replace(", ",",").split())).split(" ")

        device_name = device_line[0]

        if(device_name.startswith('AP')):
        

            interface_taged = device_line[1]+device_line[2]
            #push config to the port of Access point 
            net_connect.send_config_set(['default int '+ interface_taged,'int '+interface_taged]+commands_ap)

            table.add_row(device_name,interface_taged,"Pushed", style='bright_green')
    
    #save the current configuration of switch
    op=net_connect.send_command_timing("wr")

    console = Console()
    #print the table of AP and ports found in the current switch
    console.print(table)

    net_connect.disconnect()

    return 
 


if __name__ == '__main__':
    
    addresses = config.get_ip_adresses()

    for ip in addresses :
       
       process_dev(ip)


