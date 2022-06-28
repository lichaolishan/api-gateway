# -*- coding:utf-8 -*-
from hmac import new as _new
from hashlib import sha512 as _sha512
import urllib
import urllib.parse
import urllib.request


class SdkV1:
    """
    Desc：create signature(V1 Version)
    """

    def __init__(self, secret_key):
        self.__secret_key = secret_key

    def create_sign(self, params):
        encode_params = urllib.parse.urlencode(params)
        # print("\033[1;32m ---签名参数---\033[0m", encode_params)
        # print("\033[1;34m ---私钥---\033[0m", self.__secret_key.encode("utf-8"))
        sign = _new(
            self.__secret_key.encode(
                "utf-8"), encode_params.encode("utf-8"), _sha512
        )
        # print("\033[1;33m ---签名---\033[0m", sign.hexdigest())
        return sign.hexdigest()
