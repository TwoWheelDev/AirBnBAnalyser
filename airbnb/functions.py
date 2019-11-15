def filterhomeapt(listing):
    if listing['room_type'] == 'Entire home/apt':
        return True
    else:
        return False


def count_listings_by_host(listings):
    hosts = {}
    for listing in listings:
        if listing['host_id'] not in hosts.keys():
            hosts[listing['host_id']] = 1
        else:
            hosts[listing['host_id']] += 1

    return hosts


def hosts_with_multiple(host_list):
    hosts = {}
    for host, value in host_list.items():
        if value > 1:
            hosts[host] = value

    return hosts
