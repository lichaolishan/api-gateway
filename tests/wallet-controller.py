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


def wallet_activity():
    """
    activityType: adjustments | deposits | withdrawals
    :return:
    """
    path_req = "/wallets/activity"
    method_req = "get"
    params_req = {"start": "1658115303000", "end": "1658201745805", "activityType": "withdrawals"}
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
    print("\033[1;31m 获取充提记录响应\033[0m", res)


def wallets_address():
    """
    currency 如果不传就返回全部
    :return:
    """
    path_req = "/wallets/addresses"
    method_req = "get"
    params_req = {"currency": "ETH"}
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
    print("\033[1;31m 获取所有或者单个币种充币地址响应\033[0m", res)


def generate_address():
    path_req = "/wallets/address"
    method_req = "post"
    params_req = {"currency": "ETH"}
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
    print("\033[1;31m 生成地址\033[0m", res)


def withdraw():
    path_req = "/wallets/withdraw"
    method_req = "post"
    params_req = {
        "currency": "USDT",
        "amount": "100",
        "address": "TAyyU1wbUFxdq86qWhNxVJDNs2qcpYf41m",
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
    print("\033[1;31m 提现\033[0m", res)


# wallet_activity()
# wallets_address()
generate_address()
# withdraw()
