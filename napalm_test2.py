import json
from napalm import get_network_driver
driver = get_network_driver('panos')
dev = driver(hostname='192.168.101.135', username='cisco', password='cisco')
dev.open()
dev_info = dev.get_facts()
dev.close()
print(json.dumps(dev_info, sort_keys=True, indent=4))
