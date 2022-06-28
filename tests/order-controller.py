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


def getOrders():
    path_req = "/orders"
    method_req = "get"
    params_req = {"limit": 10, "side": ""}
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
    print("\033[1;31m 查询所有订单响应\033[0m", res)


def place():
    path_req = "/orders"
    method_req = "post"
    params_req = {
        "symbol": "BTC_usdt",
        "accountType": "spot",
        "type": "limit",
        "side": "buy",
        "timeInForce": "GTC",
        "price": "1.01",
        "amount": "99",
        "quantity": "1",
        "clientOrderId": ""
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
    print("\033[1;31m 下单响应\033[0m", res)


def getOrdersByid():
    # 新接口根据id获取订单信息
    path_req = "/orders/62609454314598400"
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
    print("\033[1;31m 根据id查询订单响应\033[0m", res)


def CancelAll():
    # 批量取消订单
    path_req = "/orders"
    method_req = "DELETE"
    params_req = {"symbols": [], "accountTypes": ["spot"]}
    sign = service.create_sign(params_req, method_req, path_req)
    headers.update(
        {
            "key": access_key_req,
            "signTimestamp": str(timestamp),
            "signature": sign,
        }
    )
    print("\033[1;32m ---headers---\033[0m", headers)
    res = ClientHttp(host_gateway, path_req, params_req, headers).delete()
    print("\033[1;31m 撤销所有订单响应\033[0m", res)


def CancelByIDs():
    # 根据id取消订单
    path_req = "/orders/cancelByIds"
    method_req = "DELETE"
    params_req = {
        "orderIds": [""],
        "clientOrderIds": ["134"],
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
    res = ClientHttp(host_gateway, path_req, params_req, headers).delete()
    print("\033[1;31m 根据id撤销多个或单个订单响应\033[0m", res)


def CancelByID():
    # 根据id单个取消订单
    path_req = "/orders/63004634087718912"
    method_req = "DELETE"
    params_req = "None"
    sign = service.create_sign(params_req, method_req, path_req)
    headers.update(
        {
            "key": access_key_req,
            "signTimestamp": str(timestamp),
            "signature": sign,
        }
    )
    print("\033[1;32m ---headers---\033[0m", headers)
    res = ClientHttp(host_gateway, path_req, params_req, headers).delete()
    print("\033[1;31m 根据id撤销订单响应\033[0m", res)


def getSmartOrders():
    # 获取smartorders订单
    path_req = "/smartorders"
    method_req = "get"
    params_req = {"limit": ""}
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
    print("\033[1;31m 查询smart order响应\033[0m", res)


def PlaceSmartOrders():
    # 下smartorders订单
    path_req = "/smartorders"
    method_req = "POST"
    params_req = {
        "symbol": "btc_usdt",
        "accountType": "spot",
        "type": "stop",
        "side": "sell",
        "timeInForce": "GTC",
        "price": "122",
        "quantity": "1",
        "amount": "11",
        # "clientOrderId": "test_smart_order",
        "clientOrderId": "clientOrderId",
        "stopPrice": "122",
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
    print("\033[1;31m 下smart order响应\033[0m", res)


def getSmartOrdersByid():
    # 通过订单id获取smartorder订单
    path_req = "/smartorders/111"
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
    print("\033[1;31m 根据id查询smart order订单响应\033[0m", res)


def CancelAllSmartOrders():
    path_req = "/smartorders"
    method_req = "DELETE"
    params_req = {"symbols": [], "accountTypes": []}
    sign = service.create_sign(params_req, method_req, path_req)
    headers.update(
        {
            "key": access_key_req,
            "signTimestamp": str(timestamp),
            "signature": sign,
        }
    )
    print("\033[1;32m ---headers---\033[0m", headers)
    res = ClientHttp(host_gateway, path_req, params_req, headers).delete()
    print("\033[1;31m 撤销所有订单响应\033[0m", res)


def CancelSmartOrdersByids():
    # 通过id撤销smartorder订单
    path_req = "/smartorders/cancelByIds"
    method_req = "DELETE"
    params_req = {"orderIds": [], "clientOrderIds": ["133"]}
    sign = service.create_sign(params_req, method_req, path_req)
    headers.update(
        {
            "key": access_key_req,
            "signTimestamp": str(timestamp),
            "signature": sign,
        }
    )
    print("\033[1;32m ---headers---\033[0m", headers)
    res = ClientHttp(host_gateway, path_req, params_req, headers).delete()
    print("\033[1;31m 根据ids撤销smart order订单响应\033[0m", res)


def CancelSmartOrdersByid():
    # 通过id撤销smartorder订单
    path_req = "/smartorders/63004908101566464"
    method_req = "DELETE"
    params_req = "None"
    sign = service.create_sign(params_req, method_req, path_req)
    headers.update(
        {
            "key": access_key_req,
            "signTimestamp": str(timestamp),
            "signature": sign,
        }
    )
    print("\033[1;32m ---headers---\033[0m", headers)
    res = ClientHttp(host_gateway, path_req, params_req, headers).delete()
    print("\033[1;31m 根据id撤销smart order订单响应\033[0m", res)


def ordersHistory():
    path_req = "/orders/history"
    method_req = "get"
    params_req = {
        "accountType": "spot",
        "type": "market",
        "symbol": "btc_usdt",
        "side": "buy",
        "limit": 5,
        "from": "0",
        "state": "",
        "hideCancel": "",
        "startTime": "",
        "endTime": ""
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
    print("\033[1;31m 历史订单响应\033[0m", res)


def smartOrdersHistory():
    path_req = "/smartorders/history"
    method_req = "get"
    params_req = {
        "symbol": "",
        "accountType": "SPOT",
        "side": "",
        "limit": 5,
        "from": "",
        "states": "",
        "direction": "",
        "hideCancel": "",
        "startTime": "",
        "endTime": "",
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
    print("\033[1;31m 历史订单响应\033[0m", res)


# getOrders()
# place()
# getOrdersByid()
# CancelAll()
# CancelByIDs()
# CancelByID()
# getSmartOrders()
# PlaceSmartOrders()
# getSmartOrdersByid()
# CancelAllSmartOrders()
# CancelSmartOrdersByids()
# CancelSmartOrdersByid()
# ordersHistory()
# smartOrdersHistory()



#
# order_count = 0
# cancel_count = 0
# while True:
#     timestamp = int(time.time() * 1000)
#     service = SDK(access_key_req, secret_key_req, timestamp)
#     for clientOrderId in ["test41", "test42", "test43", "test44", "test45"]:
#         PlaceSmartOrders()
#         order_count = order_count + 1
#     CancelAllSmartOrders()
#     cancel_count = cancel_count + 1
#
#     print("---order_count---:", order_count, "---cancel_count---:", cancel_count)

