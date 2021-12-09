from typing import TextIO, List


class Toggler:
    __data: List[str]

    def __init__(self, filename) -> None:
        self.__config_file = open(filename, 'r+')
        self.read_file()

    def __del__(self):
        self.file.close()

    def read_file(self):
        self.file.seek(0)
        self.__data = self.file.readlines()

    def write_file(self):
        self.file.seek(0)
        self.file.truncate(0)
        self.file.writelines(self.data)

    def disable_ipv6(self):
        data = []

        for line in self.data:
            if line.find('ipv6') >= 0 and not line.startswith('#'):
                line = '#' + line

            data.append(line)

        self.__data = data
        self.write_file()

    def enable_ipv6(self):
        data = []
        for line in self.data:
            if line.find('ipv6') >= 0 and line.startswith('#'):
                line = line[1:len(line)]

            data.append(line)

            self.__data = data
            self.write_file()

    def is_using_ipv6(self) -> bool:
        is_active = True

        for line in self.data:
            if is_active is True and line.find('ipv6') >= 0 and line[0] == '#':
                is_active = False
            elif is_active is False and line.find('ipv6') >= 0 and line[0] != '#':
                is_active = True

        return is_active

    def toggle_ipv6(self):
        is_ipv6_active = self.is_using_ipv6()

        if is_ipv6_active is True:
            self.disable_ipv6()
        else:
            self.enable_ipv6()

    @property
    def file(self) -> TextIO:
        return self.__config_file

    @property
    def data(self) -> List[str]:
        return self.__data
