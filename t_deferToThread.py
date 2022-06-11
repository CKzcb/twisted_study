#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：mrProtein 
@File    ：t_deferToThread.py
@Author  ：mrProtein
@Date    ：2022/6/11
@Desc    :


同步非阻塞

deferToThread使用线程实现的，不建议

范湖一个deferred对象,把回调函数在另一个线程里进程处理，主要用于IO操作，例如: 数据库文件读写

callinThread  单独放到一个线程处理，所以不阻塞

callfromThread


"""

from twisted.internet import reactor, defer
from twisted.internet.threads import deferToThread
import time, functools


def func(num):
    print("func start ...")
    time.sleep(4)
    print("func end ...")
    return num + 1


def callback(result):
    print("callback in ... ", result)



if __name__ == '__main__':
    # 同步阻塞
    # d = defer.Deferred()
    # d.addCallback(func)
    # d.addCallback(callback)
    # d.callback(10)

    # 同步非阻塞
    func = functools.partial(func, 42)
    d = deferToThread(func)
    d.addCallback(callback)

    print("in main ... ")
    reactor.run()



