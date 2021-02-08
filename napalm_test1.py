import napalm
import json

net_driver = napalm.get_network_driver('ios')
net_device = device(hostname="192.168.101.135", username="cisco", password="cisco")
device.open()
print(device.get_config(retrieve='running', full=False))
print(device.get_environment())
device.close()
