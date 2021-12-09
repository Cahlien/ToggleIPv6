#!/usr/bin/env python

from toggler import Toggler


def main():
    """ This method attempts to toggle IPv6 on or off. """
    toggler = Toggler('/etc/sysctl.conf')
    toggler.toggle_ipv6()
    print("[+] Run 'sudo sysctl -p' to finish toggling your IPv6 settings.")


def protected_main():
    """ This method attempts to handle errors encountered during the main method. """
    try:
        main()
    except IOError:
        print('[=] Error: I/O exception encountered')


if __name__ == '__main__':
    """ This method ensures that the main function is only executed when appropriate. """
    protected_main()
