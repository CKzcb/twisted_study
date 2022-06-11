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
    - 保存所有的公共属性和方法

transport：用来收发数据，服务器和客户端收发数据的连接
    代表网络两个通信点的连接，负责秒速连接的细节，比如连接时面向流的还是面向数据的
    流控以及可靠性
    - write 以阻塞的方式按顺序依次将数据写入到物理连接
    - writeSequence 将一个字符串列表写到物理连接上
    - loseConnection 将所有挂起的数据写入，然后主动断开连接
    - getPeer 获取连接中对端的信息
        - host 地址
        - port 断开
    - getHost 获取连接中本端的信息
        - host 地址
        - port 端口

Protocols：描述了如何以异步的方法处理网络中的事件，HTTP/DNS以及IMAP是应用协议中的例子，Protocol实现了IProtocol接口
    - factory 默认为none，协议工厂的实例对象，需要在构建协议对象时赋值
    - connected 连接状态，默认为0，连接成功后为true
    - transport
    - makeConnection 在transport和客户端建立连接时的第一条协议
    - dataReceived 接受数据时
    - connectionLost 关闭连接时
    - connectionMade 连接建立起来之后使用



"""

from twisted.internet import reactor, protocol


class SFactory(protocol.ServerFactory):
    # protocol = SProtocol
    clients = []

    def buildProtocol(self, addr):
        return SProtocol(self)

    def add_clients(self, client):
        self.clients.append(client)

    def startFactory(self):
        """公共数据初始化"""
        print("init ... factory ... ")

    def stopFactory(self):
        """关闭"""
        print("stop ... factory ... ")


class SProtocol(protocol.Protocol):

    def __init__(self, factory: SFactory):
        super(SProtocol, self).__init__()
        self.factory: SFactory = factory

    def connectionMade(self):
        print("{} is connected ... ", self.transport.getHost())

        print("remain ... ", len(self.factory.clients))
        if self not in self.factory.clients:
            self.factory.add_clients(self)

    def dataReceived(self, data: bytes):
        print("server recv: ", data.decode())
        for client in self.factory.clients:
            if client is self:
                continue
            client.transport.write(data)

    def connectionLost(self, reason):
        self.factory.clients.remove(self)
        print("remain ... ", len(self.factory.clients))



if __name__ == '__main__':
    print("server start ... ")
    reactor.listenTCP(10001, SFactory())
    reactor.run()

