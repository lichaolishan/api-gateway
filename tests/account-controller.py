# -*- coding:utf-8 -*-
from common_utils.poloniex_sign_v2 import *
from config.ReadConfig import *
from common_utils.client_http import *
import time

headers = {"Content-Type": "application/json"}
host_gateway = data["host_gateway"]
access_key_req = data["access_key"]
secret_key_req = data["secret_key"]
timestamp = int(time.time() * 1000)
service = SDK(access_key_req, secret_key_req, timestamp)


def account():
    path_req = "/accounts"
    method_req = "get"
    params_req = {}
    sign = service.create_sign(params_req, method_req, path_req)
    headers.update(
        {
            "key": access_key_req,
            "signTimestamp": str(timestamp),
            "signature": sign,
        }
    )
    print("\033[1;32m ---headers---\033[0m", headers)
    res = ClientHttp(host_gateway, path_req, params_req, headers).get()
    print("\033[1;31m account响应\033[0m", res)


def accountBalances():
    path_req = "/accounts/balances"
    method_req = "get"
    params_req = {"accountType": "spot"}
    sign = service.create_sign(params_req, method_req, path_req)
    headers.update(
        {
            "key": access_key_req,
            "signTimestamp": str(timestamp),
            "signature": sign,
        }
    )
    print("\033[1;32m ---headers---\033[0m", headers)
    res = ClientHttp(host_gateway, path_req, params_req, headers).get()
    print("\033[1;31m accountBalances响应\033[0m", res)


def accountsID():
    path_req = "/accounts/80001/balances"
    method_req = "get"
    params_req = {}
    sign = service.create_sign(params_req, method_req, path_req)
    headers.update(
        {
            "key": access_key_req,
            "signTimestamp": str(timestamp),
            "signature": sign,
        }
    )
    print("\033[1;32m ---headers---\033[0m", headers)
    res = ClientHttp(host_gateway, path_req, params_req, headers).get()
    print("\033[1;31m accountsID响应\033[0m", res)


# account()
accountBalances()
# accountsID()
