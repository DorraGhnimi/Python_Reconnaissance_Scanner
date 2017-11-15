import os


# Getting the ip address of the target

def get_ip_address(url):
    command = "host " + url
    process = os.popen(command)
    results = str(process.read())
    marker = results.find('has address') + 12
    return results[marker:].splitlines()[0]


print('3___getting ip_address . . .')
print('ip_address of thenewboston.com = ' + get_ip_address('thenewboston.com'))


