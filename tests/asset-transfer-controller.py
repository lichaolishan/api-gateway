# -*- coding:utf-8 -*-
import time
from common_utils.poloniex_sign_v2 import *
from config.ReadConfig import *
from common_utils.client_http import *

headers = {"Content-Type": "application/json"}
host_gateway = data["host_gateway"]
access_key_req = data["access_key"]
secret_key_req = data["secret_key"]
timestamp = int(time.time() * 1000)
service = SDK(access_key_req, secret_key_req, timestamp)


def transferBalance():
    path_req = "/accounts/transferBalance"
    method_req = "post"
    params_req = {
        "currency": "USDT",
        "amount": "0.7744",
        "fromAccount": "spot",
        "toAccount": "futures",
    }
    sign = service.create_sign(params_req, method_req, path_req)
    headers.update(
        {
            "key": access_key_req,
            "signTimestamp": str(timestamp),
            "signature": sign,
        }
    )
    print("\033[1;32m ---headers---\033[0m", headers)
    res = ClientHttp(host_gateway, path_req, params_req, headers).post()
    print("\033[1;31m 划转响应\033[0m", res)


def transferBalance_history():
    path_req = "/accounts/transferBalance/history"
    method_req = "get"
    params_req = {
        "limit": "",
        "from": "",
        "direction": "",
        "currency": ""
    }
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
    print("\033[1;31m 划转记录响应\033[0m", res)


transferBalance()
transferBalance_history()