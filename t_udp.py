#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：mrProtein 
@File    ：t_udp.py
@Author  ：mrProtein
@Date    ：2022/6/11
@Desc    :

udp网络

仅需要实现DatagramProtocol

基于socket实现的，通过socket来绑定


"""

from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor
import socket


class UDPProtocol(DatagramProtocol):

    def datagramReceived(self, datagram: bytes, addr):
        print(datagram.decode(), addr)
        self.transport.write("fa".encode(), addr)




if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.setblocking(False)
    s.bind(("127.0.0.1", 10002))
    reactor.adoptDatagramPort(s.fileno(), socket.AF_INET, UDPProtocol())
    reactor.run()


