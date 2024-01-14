#!/usr/bin/python3
# -*- coding: utf-8 -*-

class DataProcess:
    def __init__(self):
        self.name = "data_process"

    @staticmethod
    def is_ipv4(address: str) -> bool:
        """
        判断字符串是否为IPV4字符串
        :param address: 字符串
        :return: True or False
        """
        import re
        pattern = r'^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'
        if re.match(pattern, address):
            return True
        else:
            return False
