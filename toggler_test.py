import unittest

from toggler import Toggler


class TestToggler(unittest.TestCase):
    def setUp(self):
        self.toggler = Toggler('.test/etc/sysctl.conf')

    def tearDown(self) -> None:
        del self.toggler

    def test_constructor(self):
        self.assertIsNotNone(self.toggler)

    def test_read_data(self):
        self.toggler.read_file()
        self.assertTrue(len(self.toggler.data) > 0)

    def test_is_using_ipv6(self):
        ipv6_active = self.toggler.is_using_ipv6()
        verified_ipv6_active = False

        data = self.toggler.data
        for line in data:
            if line.find('ipv6') >= 0 and line[0] != '#':
                verified_ipv6_active = True

        self.assertEqual(ipv6_active, verified_ipv6_active)

    def test_disable_ipv6(self):
        self.toggler.disable_ipv6()

        self.toggler.file.seek(0)
        data = self.toggler.file.readlines()

        ipv6_is_disabled = True

        for line in data:
            if line.find('ipv6=0') >= 0:
                ipv6_is_disabled = False

        self.assertTrue(ipv6_is_disabled)

    def test_enable_ipv6(self):
        self.toggler.enable_ipv6()
        self.toggler.file.seek(0)
        data = self.toggler.file.readlines()

        ipv6_is_enabled = True

        for line in data:
            if line.find('ipv6') >= 0 and line[0] == '#':
                ipv6_is_enabled = False

            self.assertTrue(ipv6_is_enabled)

    def test_toggle_ipv6(self):
        start_data = self.toggler.data
        is_ipv6_active_at_start = False
        is_ipv6_active_at_finish = False

        for line in start_data:
            if line.find('ipv6=0') >= 0:
                is_ipv6_active_at_start = True

        self.toggler.toggle_ipv6()

        finish_data = self.toggler.data
        for line in finish_data:
            if line.find('ipv6=0') >= 0:
                is_ipv6_active_at_finish = True

        self.assertNotEqual(is_ipv6_active_at_start, is_ipv6_active_at_finish)
