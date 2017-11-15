import os

import nmap as nmap


#nmap scan


def get_nmap(options, ip):
    command = "nmap " + options + " " + ip
    process = os.popen(command)
    results = str(process.read())
    return results

# print("4___Fast scan using nmap of '54.186.250.79' = " + get_nmap('-F', '54.186.250.79'))





