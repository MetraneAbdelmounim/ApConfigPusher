# ApConfigPusher Script

ApConfigPusher is a script that automates the process of pushing configuration settings to Cisco access points. This script simplifies and streamlines the configuration deployment process, saving time and effort for network administrators.

## Requirements

* Python 3.9+
* Netmiko
* Pandas
* xlrd
* openpyxl
* rich
* Switch Cisco configured for SSH access

Note: Code tested on Python 3.9.12

## Configuration

Configure your network access devices and the template of configuration of cisco Access point in the `config/config.json` file using the following format:

``` json
{
    "ap" : [
        "description Access_Point",
        "switchport trunk native vlan 100",
        "switchport trunk allowed vlan 10,20,30,40",
        "switchport mode trunk",
        "ip dhcp snooping trust",
        "sh",
        "no sh"
    ],
    "credential":{
        "username": "cisco",
        "password": "cisco"
    
    }
    
}
```


## Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/MetraneAbdelmounim/ApConfigPusher.git
   ```

2. Install the dependencies:

   ```bash
   pip3 install -r requirements.txt
   ```

3. Modify the ip addresses of hosts in the excel `addresses.xlsx` with your specific hosts.

4. Modify the `config.json` file in the `config` directory with your specific settings.

5. Run the script:

   ```bash
   python3 script.py
   ```


## Sample Output
                 10.190.100.192
| Device Name| Port                 | Status    |
| ---------  | -----------------    | --------- |
| AP1        | GigabitEthernet1/0/1 | Pushed    |
| AP2        | GigabitEthernet0/0/1 | Pushed    |


## Notes

* Testing done on IOS and IOS-XE
