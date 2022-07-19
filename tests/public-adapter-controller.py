# -*- coding:utf-8 -*-
from common_utils.client_http import *
from config.ReadConfig import *

headers = {"Content-Type": "application/x-www-form-urlencoded"}
host_gateway = data["host_gateway"]
path_req = "/public"


def returnTicker():
    params_req = {"command": "returnTicker"}
    res = ClientHttp(host_gateway, path_req, params_req, headers).get()
    print("\033[1;31m returnTicker响应\033[0m", res)


def return24hVolume():
    params_req = {"command": "return24hVolume"}
    res = ClientHttp(host_gateway, path_req, params_req, headers).get()
    print("\033[1;31m return24hVolume响应\033[0m", res)


def returnOrderBook():
    params_req = {
        "command": "returnOrderBook",
        "currencyPair": "USDT_BTC",
        "depth": 10}
    res = ClientHttp(host_gateway, path_req, params_req, headers).get()
    print("\033[1;31m returnOrderBook响应\033[0m", res)


def returnTradeHistory():
    params_req = {
        "command": "returnTradeHistory",
        "currencyPair": "USDT_BTC",
        "start": "1653418232",
        "end": "1653418232",
    }
    res = ClientHttp(host_gateway, path_req, params_req, headers).get()
    print("\033[1;31m returnTradeHistory响应\033[0m", res)


def returnChartData():
    params_req = {
        "command": "returnChartData",
        "start": "1653418232",
        "end": "1654418232",
        "currencyPair": "USDT_LTC",
        "period": 300,
    }
    res = ClientHttp(host_gateway, path_req, params_req, headers).get()
    print("\033[1;31m returnChartData响应\033[0m", res)


def returnCurrencies():
    params_req = {"command": "returnCurrencies"}
    res = ClientHttp(host_gateway, path_req, params_req, headers).get()
    print("\033[1;31m returnCurrencies响应\033[0m", res)


# returnTicker()
# return24hVolume()
# returnOrderBook()
# returnTradeHistory()
# returnChartData()
returnCurrencies()
