from netmiko import ConnectHandler

sshCli = ConnectHandler(
    device_type ='cisco_ios',
    host = '10.10.20.48',
    port = 22,
    username = 'developer',
    password = 'C1sco12345'
)

config_commands = [
    'int loopback 2',
    'ip address 2.2.2.2 255.255.255.0',
    'description SECOND LOOPBACK'
    ]

output = sshCli.send_config_set(config_commands)
output = sshCli.send_command("show ip int brief")
print("show ip int brief:\n{}\n".format(output))

#Loopback1 interface is shown
#Use "SHOW IP INT BRIEF" after loopback is created to view interfaces
#Loopback2 is created succesfully but only partially
#The IP address 2.2.2.2 already exists and is conflict with loopback 1

