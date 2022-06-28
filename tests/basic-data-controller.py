# -*- coding:utf-8 -*-
from config.ReadConfig import *
from common_utils.client_http import *

headers = {"Content-Type": "application/json"}
host_gateway = data["host_gateway"]
access_key_req = data["access_key"]
secret_key_req = data["secret_key"]


def currencies():
    # 获取全部币种信息
    path_req = "/currencies"
    method_req = "get"
    params_req = {}
    res = ClientHttp(host_gateway, path_req, params_req, headers).get()
    print("\033[1;31m 查询币种信息响应\033[0m", res)


def currenciesName():
    # 根据币种名称获取币种的信息
    path_req = "/currencies/btc"
    method_req = "get"
    params_req = {}
    res = ClientHttp(host_gateway, path_req, params_req, headers).get()
    print("\033[1;31m 根据币种名称查询币种信息响应\033[0m", res)


def markets():
    # 获取全部交易对信息
    path_req = "/markets"
    method_req = "get"
    params_req = {}
    res = ClientHttp(host_gateway, path_req, params_req, headers).get()
    print("\033[1;31m 查询交易对响应\033[0m", res)


def marketsName():
    # 新增根据交易对名称获取交易对信息
    path_req = "/markets/btc_usdt"
    method_req = "get"
    params_req = {}
    res = ClientHttp(host_gateway, path_req, params_req, headers).get()
    print("\033[1;31m 根据交易对名称查询交易对信息响应\033[0m", res)


def timestamp():
    # 获取服务器时间戳
    path_req = "/timestamp"
    method_req = "get"
    params_req = {}
    res = ClientHttp(host_gateway, path_req, params_req, headers).get()
    print("\033[1;31m 时间戳响应\033[0m", res)


def platformStatus():
    # api-gateway 暂时没有实现，unified已实现
    path_req = "/spot/broker/platform/status"
    method_req = "get"
    params_req = {}
    host_gateway = "https://test-spot-unified-gateway.poloniex.com"
    res = ClientHttp(host_gateway, path_req, params_req, headers).get()
    print("\033[1;31m platformStatus响应\033[0m", res)


currencies()
currenciesName()
markets()
marketsName()
timestamp()
platformStatus()