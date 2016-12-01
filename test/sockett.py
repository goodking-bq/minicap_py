# coding:utf-8
from __future__ import absolute_import, unicode_literals

__author__ = "golden"
__date__ = '2016/12/1'

import socket


def main():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('127.0.0.1', 1717))
        while 1:
            a = s.recv(4096)
            if a:
                print a
            else:
                print 'wait...'
    except:
        print 'error'


if __name__ == '__main__':
    main()
