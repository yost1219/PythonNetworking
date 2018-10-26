"""
Author: Yost
Title: Lab 5B
Date: 27 Sep 2018

Lab 5B:

Create an IPv6 UDP chat server in Python using multicast to transmit to all clients.

Message strings should follow the following format:

Username: TextGoes Here

The receiver A should display recieved chats in the following format:

[(IPv6Addr)]: The quick brown fox jumps over the lazy dogs

**Hints:

Ref:http://man7.org/linux/man-pages/man7/ipv6.7.html​

Using the reference set the following socket options, with a level of socket.IPPROTO_IPV6:

Sender:

•Set the multicast hops to 5

Receiver:

Set the socket's multicast group (this is for the OS, it is _NOT_ IPv6 related)

The group is a value obtained by combining the following:

    Packing the multicast IPv6 addr using socket.inet_pton()

    Packing a 32 bit unsigned integer with the value 0, using struct.pack()
"""

