# -*- coding:utf-8 -*-
import random
import time
from common_utils.poloniex_sign_v2 import *
from config.ReadConfig import *
from client_http import *

headers = {"Content-Type": "application/json"}
host_gateway = data["host_gateway"]
access_key_req = data["access_key"]
secret_key_req = data["secret_key"]

path_req = "/orders"
method_req = "post"
price = 5

while True:
    order_type = ["limit"]
    side = ["sell", "buy"]
    symbols = ["btc_USDT"]
    amount = ["10", "12", "15", "17", "19", "23", "26", "32"]
    quantity = ["1", "2", "3", "1.3", "2.5", "3.6"]
    price_float = [0.99, 1.01]
    params_req = {
        "symbol": random.choice(symbols),
        "accountType": "spot",
        "type": random.choice(order_type),
        "side": random.choice(side),
        "timeInForce": "GTC",
        "price": str(price),
        "amount": random.choice(amount),
        "quantity": random.choice(quantity),
        "clientOrderId": "",
    }
    timestamp = int(time.time() * 1000)
    price_choice = random.choice(price_float)
    price = round(price * price_choice, 2)
    sign = SDK(access_key_req, secret_key_req, timestamp).create_sign(
        params_req, method_req, path_req
    )
    headers.update(
        {
            "key": access_key_req,
            "signTimestamp": str(timestamp),
            "signature": sign,
        }
    )
    res = ClientHttp(host_gateway, path_req, params_req, headers).post()
    print("\033[1;31m 响应\033[0m", res)
