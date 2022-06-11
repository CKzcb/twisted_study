#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：mrProtein 
@File    ：quick_start.py
@Author  ：mrProtein
@Date    ：2022/6/10
@Desc    : 
"""
from twisted.internet import selectreactor
selectreactor.install()
from twisted.internet import reactor


def main(s):
    print(s)
    reactor.stop()


if __name__ == '__main__':
    reactor.callWhenRunning(main, "start ,,,")
    reactor.run()
