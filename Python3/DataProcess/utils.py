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

    @staticmethod
    def get_csv_encoding(file_path: str) -> str:
        """
        获取csv文件的编码格式
        :param file_path: csv文件的位置
        :return: csv文件的编码格式
        """
        import chardet

        with open(file_path, 'rb') as f:
            rawdata = f.read()
            result = chardet.detect(rawdata)
            return result['encoding']
