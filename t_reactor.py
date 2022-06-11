#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：mrProtein 
@File    ：t_reactor.py
@Author  ：mrProtein
@Date    ：2022/6/10
@Desc    : 
"""
from twisted.internet import task
from twisted.internet import reactor


def call_back():
    print("... ")


def main():
    loop = task.LoopingCall(call_back)
    loop.start(2)


if __name__ == '__main__':
    reactor.callWhenRunning(main)
    reactor.run()



