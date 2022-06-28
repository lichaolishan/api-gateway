# -*- coding:utf-8 -*-
from common_utils.poloniex_sign_v2 import *
from config.ReadConfig import *
import time

if __name__ == "__main__":
    timestamp = int(time.time() * 1000)
    headers = {"Content-Type": "application/json"}
    path = "/ws"
    method = "get"
    params = {}
    access_key_req = data["access_key"]
    secret_key_req = data["secret_key"]
    service = SDK(access_key_req, secret_key_req, timestamp)
    sign = service.auth_sign(path, method, params)
    auth = {"event": "subscribe", "channel": ["auth"], "params": sign}
    print("\033[1;34m ---发送私有频道鉴权auth的消息---\033[0m", auth)
