# coding:utf-8
from __future__ import absolute_import, unicode_literals
import subprocess
import os
import socket
import time

__author__ = "golden"
__date__ = '2016/12/2'


class Minicap(object):
    bash_path = os.path.abspath(os.path.dirname(__file__))
    minicap_path = os.path.join(bash_path, 'minicap')
    phone_tmp_path = '/data/local/tmp/'
    bash_shell = r'D:\minicap\adb\adb.exe shell '
    push_shell = r'D:\minicap\adb\adb.exe push '
    screen_shell = 'wm size'
    abi_shell = 'getprop ro.product.cpu.abi | tr -d \'\r\''
    sdk_shell = 'getprop ro.build.version.sdk | tr -d \'\r\''
    chmod_shell = 'chmod 777 '
    port = 1717

    def command(self, command):
        print command
        p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if p.wait():
            raise Exception(p.stderr.read().decode('gbk'))
        return p.stdout.read().strip()

    def push_file(self, filename):
        self.command(self.push_shell + filename + ' ' + self.phone_tmp_path)
        self.command(self.bash_shell + self.chmod_shell + self.phone_tmp_path + os.path.split(filename)[-1])

    def run_minicap(self):
        scree = self.command(self.bash_shell + self.screen_shell).split(':')[1].strip()
        api_version = self.command(self.bash_shell + self.abi_shell)
        sdk_version = self.command(self.bash_shell + self.sdk_shell)
        minicap_file = os.path.join(self.minicap_path, 'bin', api_version, 'minicap')
        self.push_file(minicap_file)
        minicap_so_file = os.path.join(self.minicap_path, 'shared', 'android-%s' % sdk_version, api_version,
                                       'minicap.so')
        self.push_file(minicap_so_file)
        exec_shell = self.bash_shell + 'LD_LIBRARY_PATH=%s' % self.phone_tmp_path + ' ' + self.phone_tmp_path + 'minicap -P {0}@{0}/0'.format(
            scree)
        print scree
        print api_version
        print sdk_version
        print self.command(exec_shell + ' -t')
        print self.command(exec_shell)
        print self.command(r'D:\minicap\adb\adb.exe forward --remove-all')
        print self.command(r'D:\minicap\adb\adb.exe forward tcp:%s localabstract:minicap' % str(self.port))
        print 'check minicap...'
        # print self.command(self.bash_shell + 'ps |grep min')

    def run_test(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('127.0.0.1', self.port))
        i = 0
        while i < 10:
            a = s.recv(1024)
            if a:
                print a
            else:
                print 'wait...'
            time.sleep(1)
            i += 1

    def run(self):
        self.run_minicap()
        self.run_test()


if __name__ == '__main__':
    minicap = Minicap()
    minicap.run()
