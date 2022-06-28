# -*- coding:utf-8 -*-
import hashlib
import urllib
import urllib.parse
import urllib.request
import hmac
import base64
import json


class SDK:
    """
    Desc：create signature(V2 Version)
    """

    def __init__(self, access_key, secret_key, timestamp):
        self.__access_key = access_key
        self.__secret_key = secret_key
        self.__timestamp = timestamp

    def create_sign(self, params, method, path):
        if method.upper() == "GET":
            params.update({"signTimestamp": self.__timestamp})
            sorted_params = sorted(
                params.items(),
                key=lambda d: d[0],
                reverse=False)
            encode_params = urllib.parse.urlencode(sorted_params)
            del params["signTimestamp"]
            # 将签名里面的时间戳参数去掉
        if (
            method.upper() == "POST"
            or method.upper() == "PUT"
            or method.upper() == "DELETE"
        ):
            if params == "None":
                encode_params = "signTimestamp={}".format(
                    str(self.__timestamp)
                )
            else:
                requestBody = json.dumps(params)
                encode_params = "requestBody={}&signTimestamp={}".format(
                    requestBody, str(self.__timestamp)
                )
        sign_params_first = [method.upper(), path, encode_params]
        sign_params_second = "\n".join(sign_params_first)
        sign_params = sign_params_second.encode(encoding="UTF8")
        print("\033[1;32m ---签名参数---\033[0m", sign_params)
        secret_key = self.__secret_key.encode(encoding="UTF8")
        print("\033[1;34m ---私钥---\033[0m", secret_key)
        digest = hmac.new(
            secret_key,
            sign_params,
            digestmod=hashlib.sha256).digest()
        signature = base64.b64encode(digest)
        signature = signature.decode()
        print("\033[1;33m ---生成的签名---\033[0m", signature)
        return signature

    def auth_sign(self, path, method, params):
        sign = self.create_sign(params=params, method=method, path=path)
        params.update(
            {
                "key": self.__access_key,
                "signTimestamp": str(self.__timestamp),
                "signature": sign,
            }
        )
        return params
