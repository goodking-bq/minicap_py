# coding:utf-8
from __future__ import absolute_import, unicode_literals

__author__ = "golden"
__date__ = '2016/12/1'

import socket


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('127.0.0.1', 1717))
    while 1:
        a = s.recv(1024)
        if a:
            print a
        else:
            print 'wait...'


if __name__ == '__main__':
    main()
