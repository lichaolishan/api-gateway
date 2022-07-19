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


def trades():
    path_req = "/trades"
    method_req = "get"
    params_req = {"startTime": "",
                  "endTime": "",
                  "limit": "",
                  "from": "",
                  "direction": "NEXT"
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
    print("\033[1;31m trades响应\033[0m", res)


def ordersIDTrades():
    # 根据订单查询用户trade
    path_req = "/orders/67581772635889664/trades"
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
    print("\033[1;31m 根据订单查询trade响应\033[0m", res)


trades()
ordersIDTrades()
