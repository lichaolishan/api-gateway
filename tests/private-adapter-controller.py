# -*- coding:utf-8 -*-
import time
from common_utils.poloniex_sign_v1 import *
from common_utils.client_http import *
from config.ReadConfig import *

host_gateway = data["host_gateway"]
access_key_req = data["access_key"]
secret_key_req = data["secret_key"]
path = "/tradingApi"
headers = {"Content-Type": "application/x-www-form-urlencoded"}
nonce = str(int(time.time() * 100000))
headers["Key"] = access_key_req


def returnBalances():
    arg = {"command": "returnBalances", "nonce": nonce}
    Sign = SdkV1(secret_key_req).create_sign(arg)
    headers["Sign"] = Sign
    print("\033[1;34m ---headers---\033[0m", headers)
    services = ClientHttp(host_gateway, path, arg, headers)
    response = services.post()
    print("\033[1;31m ---returnBalances---\033[0m", response)


def returnCompleteBalances():
    arg = {"command": "returnCompleteBalances", "nonce": nonce}
    Sign = SdkV1(secret_key_req).create_sign(arg)
    headers["Sign"] = Sign
    print("\033[1;34m ---headers---\033[0m", headers)
    services = ClientHttp(host_gateway, path, arg, headers)
    response = services.post()
    print("\033[1;31m ---returnCompleteBalances---\033[0m", response)


def returnDepositAddresses():
    arg = {"command": "returnDepositAddresses", "nonce": nonce}
    Sign = SdkV1(secret_key_req).create_sign(arg)
    headers["Sign"] = Sign
    print("\033[1;34m ---headers---\033[0m", headers)
    services = ClientHttp(host_gateway, path, arg, headers)
    response = services.post()
    print("\033[1;31m ---returnDepositAddresses---\033[0m", response)


def generateNewAddress():
    arg = {"command": "generateNewAddress", "currency": "ETH", "nonce": nonce}
    Sign = SdkV1(secret_key_req).create_sign(arg)
    headers["Sign"] = Sign
    print("\033[1;34m ---headers---\033[0m", headers)
    services = ClientHttp(host_gateway, path, arg, headers)
    response = services.post()
    print("\033[1;31m ---generateNewAddress---\033[0m", response)


def returnDepositsWithdrawals():
    arg = {"command": "returnDepositsWithdrawals", "start": "1655649781", "end": "1658241781", "nonce": nonce}
    Sign = SdkV1(secret_key_req).create_sign(arg)
    headers["Sign"] = Sign
    print("\033[1;34m ---headers---\033[0m", headers)
    services = ClientHttp(host_gateway, path, arg, headers)
    response = services.post()
    print("\033[1;31m ---returnDepositsWithdrawals---\033[0m", response)


def returnOpenOrders():
    """
    currencyPair:all  ?????????????????????
    :return:
    """
    arg = {
        "command": "returnOpenOrders",
        "currencyPair": "ALL",
        "nonce": nonce}
    Sign = SdkV1(secret_key_req).create_sign(arg)
    headers["Sign"] = Sign
    print("\033[1;34m ---headers---\033[0m", headers)
    services = ClientHttp(host_gateway, path, arg, headers)
    response = services.post()
    print("\033[1;31m ---returnOpenOrders---\033[0m", response)


def returnTradeHistory():
    """
        currencyPair:all  ?????????????????????
        start&end: ??????????????????
        :return:
    """
    arg = {
        "command": "returnTradeHistory",
        "currencyPair": "ALL",
        "start": "1656952035",
        "end": "1657124835",
        "limit": 1,
        "nonce": nonce}
    Sign = SdkV1(secret_key_req).create_sign(arg)
    headers["Sign"] = Sign
    print("\033[1;34m ---headers---\033[0m", headers)
    services = ClientHttp(host_gateway, path, arg, headers)
    response = services.post()
    print("\033[1;31m ---returnTradeHistory---\033[0m", response)


def returnOrderTrades():
    arg = {
        "command": "returnOrderTrades",
        "orderNumber": 67688219294134272,
        "nonce": nonce}
    Sign = SdkV1(secret_key_req).create_sign(arg)
    headers["Sign"] = Sign
    print("\033[1;34m ---headers---\033[0m", headers)
    services = ClientHttp(host_gateway, path, arg, headers)
    response = services.post()
    print("\033[1;31m ---returnOrderTrades---\033[0m", response)


def returnOrderStatus():
    arg = {
        "command": "returnOrderStatus",
        "orderNumber": 67644449693421568,
        "nonce": nonce}
    Sign = SdkV1(secret_key_req).create_sign(arg)
    headers["Sign"] = Sign
    print("\033[1;34m ---headers---\033[0m", headers)
    services = ClientHttp(host_gateway, path, arg, headers)
    response = services.post()
    print("\033[1;31m ---returnOrderStatus---\033[0m", response)


def buy():
    """
    rate: price,
    amount: total amount
    fillOrKill: (optional) Set to "1" if this order should either fill in its entirety or be completely aborted.
    immediateOrCancel: (optional) Set to "1" if this order can be partially or completely filled, but any portion of the order that cannot be filled immediately will be canceled.
    postOnly: (optional) Set to "1" if you want this buy order to only be placed if no portion of it fills immediately.
    clientOrderId: (optional) 64-bit Integer value used for tracking order across http responses and "o", "n" & "t" web socket messages. Must be unique across all open orders for each account.
    :return:
    """
    arg = {
        "command": "buy",
        "currencyPair": "USDT_BTC",
        "rate": "1.11",
        "amount": "1.1111",
        # "postOnly": "0",
        # "fillOrKill": "0",
        # "immediateOrCancel": "1",
        "clientOrderId": "",
        "nonce": nonce,
    }
    Sign = SdkV1(secret_key_req).create_sign(arg)
    headers["Sign"] = Sign
    print("\033[1;34m ---headers---\033[0m", headers)
    services = ClientHttp(host_gateway, path, arg, headers)
    response = services.post()
    print("\033[1;31m ---buy---\033[0m", response)


def sell():
    """
    rate: price,
    amount: total amount
    fillOrKill: (optional) Set to "1" if this order should either fill in its entirety or be completely aborted.
    immediateOrCancel: (optional) Set to "1" if this order can be partially or completely filled, but any portion of the order that cannot be filled immediately will be canceled.
    postOnly: (optional) Set to "1" if you want this buy order to only be placed if no portion of it fills immediately.
    clientOrderId: (optional) 64-bit Integer value used for tracking order across http responses and "o", "n" & "t" web socket messages. Must be unique across all open orders for each account.
    :return:
    """
    arg = {
        "command": "sell",
        "currencyPair": "USDT_BTC",
        "rate": "99998",
        "amount": "1",
        # "fillOrKill": "1",
        # "immediateOrCancel": "1",
        # "postOnly": "1",
        "clientOrderId": "",
        "nonce": nonce,
    }
    Sign = SdkV1(secret_key_req).create_sign(arg)
    headers["Sign"] = Sign
    print("\033[1;34m ---headers---\033[0m", headers)
    services = ClientHttp(host_gateway, path, arg, headers)
    response = services.post()
    print("\033[1;31m ---sell---\033[0m", response)


def cancelOrder():
    arg = {
        "command": "cancelOrder",
        "orderNumber": "67699040183214080",
        "clientOrderId": "312",
        "nonce": nonce,
    }
    Sign = SdkV1(secret_key_req).create_sign(arg)
    headers["Sign"] = Sign
    print("\033[1;34m ---headers---\033[0m", headers)
    services = ClientHttp(host_gateway, path, arg, headers)
    response = services.post()
    print("\033[1;31m ---cancelOrder---\033[0m", response)


def cancelAllOrders():
    arg = {
        "command": "cancelAllOrders",
        "currencyPair": "USDT_BTC",
        "nonce": nonce}
    Sign = SdkV1(secret_key_req).create_sign(arg)
    headers["Sign"] = Sign
    print("\033[1;34m ---headers---\033[0m", headers)
    services = ClientHttp(host_gateway, path, arg, headers)
    response = services.post()
    print("\033[1;31m ---cancelAllOrders---\033[0m", response)


def cancelReplace():
    """
    ??????????????????????????????????????????????????????
    orderNumber: The identity number of the order to be canceled.
    clientOrderId???(optional) User specified 64-bit integer identifier to be associated with the new order being placed. Must be unique across all open orders for each account.
    rate??? The price. Units are market quote currency. Eg USDT_BTC market, the value of this field would be around 10,000. Naturally this will be dated quickly but should give the idea.
    amount???(optional) The amount of tokens in this order.
    :return:
    """
    arg = {
        "command": "cancelReplace",
        "orderNumber": "67699550479007744",
        "rate": "2.22",
        "amount": "2.222222",
        "nonce": nonce,
    }
    Sign = SdkV1(secret_key_req).create_sign(arg)
    headers["Sign"] = Sign
    print("\033[1;34m ---headers---\033[0m", headers)
    services = ClientHttp(host_gateway, path, arg, headers)
    response = services.post()
    print("\033[1;31m ---cancelReplace---\033[0m", response)


def moveOrder():
    """
    ??????????????????????????????????????????????????????????????????
    orderNumber: The identity number of the order to be canceled.
    clientOrderId???(optional) User specified 64-bit integer identifier to be associated with the new order being placed. Must be unique across all open orders for each account.
    rate??? The price. Units are market quote currency. Eg USDT_BTC market, the value of this field would be around 10,000. Naturally this will be dated quickly but should give the idea.
    amount???(optional) The amount of tokens in this order.
    :return:
    """
    arg = {
        "command": "moveOrder",
        "orderNumber": "67699754305417216",
        "clientOrderId": "",
        "rate": "4",
        "amount": "4",
        "nonce": nonce,
    }
    Sign = SdkV1(secret_key_req).create_sign(arg)
    headers["Sign"] = Sign
    print("\033[1;34m ---headers---\033[0m", headers)
    services = ClientHttp(host_gateway, path, arg, headers)
    response = services.post()
    print("\033[1;31m ---moveOrder---\033[0m", response)


def withdraw():
    """
    currency: For currencies where there are multiple networks to choose from (like USDT or BTC), you can specify the chain by setting the "currency" parameter to be a multiChain currency name, like USDTTRON, USDTETH, or BTCTRON
    :return:
    """
    arg = {
        "command": "withdraw",
        "currency": "USDT",
        "amount": "11",
        "address": "12AD5BXx6DehqjPY4itVVsYgTXazvdeHZ1",
        "nonce": nonce,
    }
    Sign = SdkV1(secret_key_req).create_sign(arg)
    headers["Sign"] = Sign
    print("\033[1;34m ---headers---\033[0m", headers)
    services = ClientHttp(host_gateway, path, arg, headers)
    response = services.post()
    print("\033[1;31m ---withdraw---\033[0m", response)


def returnFeeInfo():
    arg = {"command": "returnFeeInfo", "nonce": nonce}
    Sign = SdkV1(secret_key_req).create_sign(arg)
    headers["Sign"] = Sign
    print("\033[1;34m ---headers---\033[0m", headers)
    services = ClientHttp(host_gateway, path, arg, headers)
    response = services.post()
    print("\033[1;31m ---returnFeeInfo---\033[0m", response)


def returnAvailableAccountBalances():
    arg = {"command": "returnAvailableAccountBalances", "nonce": nonce}
    Sign = SdkV1(secret_key_req).create_sign(arg)
    headers["Sign"] = Sign
    print("\033[1;34m ---headers---\033[0m", headers)
    services = ClientHttp(host_gateway, path, arg, headers)
    response = services.post()
    print("\033[1;31m ---returnAvailableAccountBalances---\033[0m", response)


def returnTradableBalances():
    arg = {"command": "returnTradableBalances", "nonce": nonce}
    Sign = SdkV1(secret_key_req).create_sign(arg)
    headers["Sign"] = Sign
    print("\033[1;34m ---headers---\033[0m", headers)
    services = ClientHttp(host_gateway, path, arg, headers)
    response = services.post()
    print("\033[1;31m ---returnTradableBalances---\033[0m", response)


def transferBalance():
    """
    fromAccount:
    toAccount: The account from which this value should be moved (exchange, margin, lending, or futures)
    :return: The account from which this value should be moved (exchange, margin, lending, or futures)
    """
    arg = {
        "command": "transferBalance",
        "currency": "btc",
        "amount": "12",
        "fromAccount": "exchange",
        "toAccount": "futures",
        "nonce": nonce,
    }
    Sign = SdkV1(secret_key_req).create_sign(arg)
    headers["Sign"] = Sign
    print("\033[1;34m ---headers---\033[0m", headers)
    services = ClientHttp(host_gateway, path, arg, headers)
    response = services.post()
    print("\033[1;31m ---transferBalance---\033[0m", response)


# returnBalances()
# returnCompleteBalances()
# returnDepositAddresses()
# generateNewAddress()
# returnDepositsWithdrawals()
# returnOpenOrders()
# returnTradeHistory()
# returnOrderTrades()
# returnOrderStatus()
# buy()
# sell()
# cancelOrder()
# cancelAllOrders()
# cancelReplace()
# moveOrder()
withdraw()
# returnFeeInfo()
# returnAvailableAccountBalances()
# returnTradableBalances()
# transferBalance() ?????????adapters??????
