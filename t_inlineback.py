#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：mrProtein 
@File    ：t_inlineback.py
@Author  ：mrProtein
@Date    ：2022/6/10
@Desc    :

内联回调

inlineCallbacks是一个装饰器，装饰生成器函数，如那些使用yield的函数

inlineCallbacks唯一的目的是将一个个生成器转化为一系列异步回调，每个回调被yield分隔，yield的返回值会传到下一个回调

当我们调用一个用inlineCallbacks装饰函数时，不需要自己调用send或throw方法，修饰器内部会帮我们处理细节，并确保生成器运行到结束


"""
import time
from twisted.internet import reactor, defer


def callback(num):
    print("callback start ... ")
    d = defer.Deferred()
    reactor.callLater(8, d.callback, num+1)
    return d


@defer.inlineCallbacks
def main():
    st = time.time()
    result = yield callback(3)
    print("main ... ", time.time() - st)
    print(result)


if __name__ == '__main__':
    main()
    reactor.run()





