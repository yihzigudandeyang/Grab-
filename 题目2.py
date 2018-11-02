#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests

def APItest_func(url):
    headers = {}
    params = {}
    req = requests.get(url, headers=headers, params=params)
    print(req.text)


if __name__ == '__main__':
    url = "https://developer.mapquest.com/documentation/geocoding-api/address/get/"
    APItest_func(url)
