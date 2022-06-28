# !/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib
import urllib.parse
import urllib.request
import requests
import json


class ClientHttp:
    def __init__(self, host, path, params, headers):
        self.host = host
        self.headers = headers
        self.params = params
        self.path = path

    def get(self):
        params = urllib.parse.urlencode(self.params)
        print("\033[1;35m ---请求参数---\033[0m", params)
        if params == "":
            host = "{host}{path}".format(host=self.host, path=self.path)
        else:
            host = "{host}{path}?{params}".format(
                host=self.host, path=self.path, params=params
            )
        print("\033[1;34m ---请求域名---\033[0m", host)
        response = requests.get(host, params={}, headers=self.headers)
        return response.json()

    def post(self):
        if self.headers["Content-Type"] == "application/json":
            print("\033[1;35m ---报文---\033[0m", json.dumps(self.params))
            print("\033[1;36m ---host---\033[0m", self.host + self.path)
            if self.params == "None":
                try:
                    response = requests.post(
                        self.host + self.path,
                        headers=self.headers,
                        data={},
                    )
                    return response.json()
                except Exception as e:
                    print(e)
            else:
                try:
                    response = requests.post(
                        self.host + self.path,
                        headers=self.headers,
                        data=json.dumps(self.params),
                    )
                    return response.json()
                except Exception as e:
                    print(e)
        if self.headers["Content-Type"] == "application/x-www-form-urlencoded":
            print(
                "\033[1;35m ---报文---\033[0m",
                urllib.parse.urlencode(
                    self.params))
            print("\033[1;36m ---host---\033[0m", self.host + self.path)
            try:
                response = requests.post(
                    self.host + self.path,
                    headers=self.headers,
                    data=urllib.parse.urlencode(self.params),
                )
                return response.json()
            except Exception as e:
                print(e)

    def put(self):
        print("\033[1;35m ---报文---\033[0m", json.dumps(self.params))
        print("\033[1;36m ---host---\033[0m", self.host + self.path)
        try:
            response = requests.put(
                self.host + self.path,
                headers=self.headers,
                data=json.dumps(self.params),
            )
            return response.json()
        except Exception as e:
            print(e)

    def delete(self):
        print("\033[1;35m ---报文---\033[0m", json.dumps(self.params))
        print("\033[1;36m ---host---\033[0m", self.host + self.path)
        try:
            response = requests.delete(
                self.host + self.path,
                headers=self.headers,
                data=json.dumps(self.params),
            )
            return response.json()
        except Exception as e:
            print(e)
