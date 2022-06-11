#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：mrProtein 
@File    ：t_defered.py
@Author  ：mrProtein
@Date    ：2022/6/10
@Desc    :


A flag which is False until either callback or errback is called and afterwards always True.
(type: bool)

"""
from twisted.internet import defer


def f1():
    return 20


def f2(n):
    a = 20 / 0
    print("f2 .. ", n)


def f3(n):
    print("f3 .. ")


def cb1(num):
    a = 20 / 0
    print("cb1 : ", num)
    return num + 1


def cb2(num):
    print("cb2 : ", num)
    return num + 1


def cb3(num):
    print("cb3 : ", num)
    return num + 1


def eb1(num):
    print("eb1 ... ")
    return num


def eb2(num):
    print("eb2 ... ")
    return 2


if __name__ == '__main__':

    d = defer.Deferred()
    d.callback(f1())
    # d.addCallback(f2)
    # d.addErrback(f3)

    # d.addCallbacks(callback=f2, errback=f3)

    d.addCallback(cb1)
    d.addErrback(eb1)
    d.addCallback(cb2)
    d.addErrback(eb2)
    d.addCallback(cb3)
