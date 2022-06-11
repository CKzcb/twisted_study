#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：mrProtein 
@File    ：t_tcp_c.py
@Author  ：mrProtein
@Date    ：2022/6/11
@Desc    :



"""

from twisted.internet import reactor, protocol


class CProtocol(protocol.Protocol):
    def connectionMade(self):
        self.transport.write("hi~".encode())

    def dataReceived(self, data: bytes):
        print("server: ", data.decode())
        data = input()
        # print("client: ", data)
        self.transport.write(data.encode())


class CFactory(protocol.ClientFactory):
    protocol = CProtocol


if __name__ == '__main__':
    print("client start ... ")
    reactor.connectTCP("127.0.0.1", 10001, CFactory())
    reactor.run()

