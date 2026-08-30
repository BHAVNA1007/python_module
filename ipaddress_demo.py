'''
Python ipaddress Module

The ipaddress module is a standard-library module in Python used to create, validate, and work with IPv4 and IPv6 addresses and networks.

You don't need to install it with pip.

'''

import ipaddress

ip = ipaddress.ip_address('192.168.1.10')

print(ip)

print(type(ip))

ip = ipaddress.ip_address("2001:db8::1")

print(type(ip))

print(ip.is_private)


'''
is_loopback checks whether an IP address is a loopback address.

What is loopback?

A loopback IP means:

The computer is communicating with itself. 🔄

The most common IPv4 loopback address is:

127.0.0.1
'''