#!/usr/bin/env python

from subprocess import call
from toggler import Toggler


def protected_main():
    try:
        toggler = Toggler('/etc/sysctl.conf')
        toggler.toggle_ipv6()
        call(['sysctl', '-p'])
    except IOError:
        print('[=] Error: I/O exception encountered')


if __name__ == '__main__':
    protected_main()
