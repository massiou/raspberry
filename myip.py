#coding: utf-8

"""
    Simply return your public IP address
"""

import subprocess


def myip(output=None):
    """
    @param output: output file, if None output in default stdout
    @return: string, public IP address
    """
    cmd_ip = 'wget -qO - canhazip.com'
    try:
        with open(output, "w") as output_file:
            subprocess.call(cmd_ip.split(), stdout=output_file)
    except TypeError:
        subprocess.call(cmd_ip.split())

if __name__ == '__main__':
    myip()
    myip('./ip.txt')
