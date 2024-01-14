#!/usr/bin/python3
# -*- coding: utf-8 -*-

from DataProcess.utils import DataProcess

if __name__ == "__main__":
    dp = DataProcess()
    print(dp.is_ipv4("192.168.100.255"))
    print(dp.is_ipv4("192.168.100.256"))
