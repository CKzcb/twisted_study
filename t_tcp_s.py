#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：mrProtein 
@File    ：t_tcp_s.py
@Author  ：mrProtein
@Date    ：2022/6/11
@Desc    :

3个基础模块

Protocol、factory、transport

Protocol：定义一个处理协议的类，这个代码实现了通信数据的收发
    - connectionMade：客户端连接
    - connectionLost：客户端断开
    - dataReceived: 接收数据接口


factory：工厂模式的体现，在这里面生成协议，生成协议的工厂
    -

transport：用来收发数据，服务器和客户端收发数据的连接






"""

from twisted.internet import reactor, protocol


class SProtocol(protocol.Protocol):

    def connectionMade(self):
        print("{} is connected ... ", self.transport.getHost())

    def dataReceived(self, data: bytes):
        print("server recv: ", data.decode())
        self.transport.write("emm..".encode())


class SFactory(protocol.Factory):
    protocol = SProtocol


if __name__ == '__main__':
    print("server start ... ")
    reactor.listenTCP(10001, SFactory())
    reactor.run()

