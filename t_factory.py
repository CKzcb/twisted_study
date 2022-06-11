#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：mrProtein 
@File    ：t_factory.py
@Author  ：mrProtein
@Date    ：2022/6/11
@Desc    :

Factory

协议工厂，用来实例化Protocol协议对象并保存持久性的公共数据（客户端连接、状态、配置等）

负责通讯时连接建立、连接中断等处理

服务端使用Protocol.Factory

客户端使用Protocol.ClientFactory

在程序运行过程中每次有连接都会使用factory实例化一个Protocol实例对象来与对端通讯

Factory：
    - Protocol Protocol协议类，一般不使用，使用buildProtocol来代替
    - buildProtocol 创建Protocol实例对象
    - startFactory 实例化协议对象时会调用，可以用来初始化数据、配置、数据库等
    - stopFactory 实例协议对象销毁时调用，可以用来销毁对象

clientFactory
    - clientConnectionFailed 客户端连接服务器回调失败
    - clientConnectionLost 客户端连接服务器断开


"""
