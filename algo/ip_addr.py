def main(ipaddr):
  addr = ipaddr.split(".")
  net_class = get_class(addr[0])
  net_id = get_netid(addr, net_class)
  host_id = get_hostid(addr, net_class)
  return net_class, net_id, host_id

def get_class(cl):
  cl = int(cl)
  if cl < 128:
    return 'a'
  if cl < 192:
    return 'b'
  if cl < 224:
    return 'c'
  if cl < 240:
    return 'd'
  return 'e'

def get_netid(addr, net_class):
  class_to_net_id = {
    'a': '.'.join([addr[0], '0', '0', '0']),
    'b': '.'.join([addr[0], addr[1], '0', '0']),
    'c': '.'.join([addr[0], addr[1], addr[2], '0']),
    'd': '.'.join(['0']*4),
    'e': '.'.join(['0']*4)
  }
  return class_to_net_id[net_class]

def get_hostid(addr, net_class):
  class_to_host_id = {
    'a': '.'.join(['0', *addr[1:]]),
    'b': '.'.join(['0', '0', *addr[2:]]),
    'c': '.'.join(['0', '0', '0', addr[3]]),
    'd': '.'.join(addr),
    'e': '.'.join(addr)
  }
  return class_to_host_id[net_class]

if __name__ == '__main__':
  addr = input("Enter ip addr: ")
  net_class, net_id, host_id = main(addr)
  print("IP: {}\nClass: {}\nNet Id: {}\nHost Id: {}".format(addr, net_class, net_id, host_id))
