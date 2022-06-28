# -*- coding:utf-8 -*-
from config.ReadConfig import *
from common_utils.client_http import *

headers = {"Content-Type": "application/json"}
host_gateway = data["host_gateway"]
access_key_req = data["access_key"]
secret_key_req = data["secret_key"]


def candles():
    # 获取kline
    path_req = "/markets/btc_usdt/candles"
    method_req = "get"
    params_req = {"interval": "DAY_1", "limit": 10}
    res = ClientHttp(host_gateway, path_req, params_req, headers).get()
    print("\033[1;31m kline响应\033[0m", res)


def orderbook():
    #  获取订单薄
    path_req = "/markets/btc_usdt/orderBook"
    method_req = "get"
    params_req = {"scale": "0.1", "limit": 5}
    res = ClientHttp(host_gateway, path_req, params_req, headers).get()
    print("\033[1;31m 盘口响应\033[0m", res)


def symbolPrice():
    # 获取某个交易对的最新价
    path_req = "/markets/ltc_usdt/price"
    method_req = "get"
    params_req = {}
    res = ClientHttp(host_gateway, path_req, params_req, headers).get()
    print("\033[1;31m 某个交易对最新价响应\033[0m", res)


def SymbolTicker24h():
    # 获取某个交易对ticker24h
    path_req = "/markets/btc_usdt/ticker24h"
    method_req = "get"
    params_req = {}
    res = ClientHttp(host_gateway, path_req, params_req, headers).get()
    print("\033[1;31m 某个交易对24ticker响应\033[0m", res)


def SymbolTrades():
    # 获取某个交易对trades
    path_req = "/markets/btc_usdt/trades"
    method_req = "get"
    params_req = {"limit": 10}
    res = ClientHttp(host_gateway, path_req, params_req, headers).get()
    print("\033[1;31m 某个交易对最新成交响应\033[0m", res)


def price():
    # 获取全部交易对的最新价
    path_req = "/markets/price"
    method_req = "get"
    params_req = {}
    res = ClientHttp(host_gateway, path_req, params_req, headers).get()
    print("\033[1;31m 全部交易对最新价响应\033[0m", res)


def Ticker24h():
    # 获取全部交易对的ticker24h
    path_req = "/markets/ticker24h"
    method_req = "get"
    params_req = {}
    res = ClientHttp(host_gateway, path_req, params_req, headers).get()
    print("\033[1;31m 全部交易对24h ticker响应\033[0m", res)


# candles()
# orderbook()
symbolPrice()
# SymbolTicker24h()
# SymbolTrades()
# price()
# Ticker24h()
