# coding:utf-8
from __future__ import absolute_import, unicode_literals
import subprocess

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


def tt():
    p = subprocess.Popen(
        'D:\minicap\adb\adb.exe shell LD_LIBRARY_PATH=/data/local/tmp/ /data/local/tmp/minicap -P 720x1280@720x1280/0 -s',
        shell=True,
        stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    e = p.stderr.read(1)

    while 1:
        s = p.stdout.read(1)
        print s


if __name__ == '__main__':
    tt()
