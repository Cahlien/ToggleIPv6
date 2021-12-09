from typing import TextIO, List


class Toggler:
    """ This class exposes the ability to toggle the system's use of IPv6 on and off. """

    __data: List[str]

    def __init__(self, filename: str) -> None:
        """ The Toggler class's constructor takes a string representing the name of the config file. """
        self.__config_file = open(filename, 'r+')
        self.read_file()

    def __del__(self) -> None:
        """ The Toggler class's destructor closes the file opened by the constructor. """
        self.file.close()

    def read_file(self) -> None:
        """ This method retrieves the data from the specified file. """
        self.file.seek(0)
        self.__data = self.file.readlines()

    def write_file(self) -> None:
        """ This method writes the data stored in the Toggler instance to the specified file. """
        self.file.seek(0)
        self.file.truncate(0)
        self.file.writelines(self.data)

    def disable_ipv6(self) -> None:
        """ This method changes the relevant IPv6 variables' values to 1 to disable IPv6. """
        data = []

        for line in self.data:
            if line.find('ipv6'):
                line = line.replace('ipv6=0', 'ipv6=1')

            data.append(line)

        self.__data = data
        self.write_file()

    def enable_ipv6(self) -> None:
        """ This method changes the relevant IPv6 variables' values to 0 to enable IPv6. """
        data = []
        for line in self.data:
            if line.find('ipv6=1') >= 0:
                line = line.replace('ipv6=1', 'ipv6=0')

            data.append(line)

            self.__data = data
            self.write_file()

    def is_using_ipv6(self) -> bool:
        """ This method determines whether the IPv6 variables are configured for the system to use IPv6. """
        is_active = True

        for line in self.data:
            if is_active is True and line.find('ipv6=1') >= 0:
                is_active = False
            elif is_active is False and line.find('ipv6=0') >= 0:
                is_active = True

        return is_active

    def toggle_ipv6(self) -> None:
        """ This method toggles the IPv6 variables to enable or disable IPv6 according to their current values. """
        is_ipv6_active = self.is_using_ipv6()

        if is_ipv6_active is True:
            self.disable_ipv6()
        else:
            self.enable_ipv6()

    @property
    def file(self) -> TextIO:
        """ This property exposes the Toggler class's private config_file field. """
        return self.__config_file

    @property
    def data(self) -> List[str]:
        """ This property exposes the Toggler class's private data field. """
        return self.__data
