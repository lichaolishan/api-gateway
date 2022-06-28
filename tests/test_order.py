#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
import pytest
from common_utils.poloniex_sign_v2 import *
from config.ReadConfig import *
from common_utils.client_http import *


class TestorderApi:
    def setup_class(self):
        self.access_key = data["access_key"]
        self.secret_key = data["secret_key"]
        self.timestamp = int(time.time() * 1000)
        self.order_service = SDK(
            self.access_key,
            self.secret_key,
            self.timestamp)
        self.headers = {"Content-Type": "application/json"}
        self.host_gateway = data["host_gateway"]

    @pytest.mark.parametrize(
        argnames=["parameters", "expect_result"],
        argvalues=[
            ({"limit": 10}, {"success": True, "code": 200, "message": "null"})],
    )
    def test_orders(self, parameters, expect_result):
        # 获取订单信息接口
        path_req = "/v2/orders/"
        method_req = "get"
        sign = self.order_service.create_sign(parameters, method_req, path_req)
        self.headers.update(
            {
                "key": self.access_key,
                "signTimestamp": str(self.timestamp),
                "signature": sign,
            }
        )
        print("\033[1;32m ---headers---\033[0m", self.headers)
        res = ClientHttp(
            self.host_gateway,
            path_req,
            parameters,
            self.headers).get()
        print(res)
        assert (len(res)) >= 0

    @pytest.mark.parametrize(
        argnames=["parameters", "expect_result"],
        argvalues=[
            (
                {
                    "symbol": "trx_usdt",
                    "accountType": "spot",
                    "type": "limit",
                    "side": "buy",
                    "timeInForce": "GTC",
                    "price": "100",
                    "amount": "1",
                    "quantity": "1",
                    "clientOrderId": "",
                },
                {"success": True, "state": "PENDING_NEW", "message": "null"},
            )
        ],
    )
    def test_orders_palce(self, parameters, expect_result):
        # 下单测试
        path_req = "/v2/orders/"
        method_req = "post"
        sign = self.order_service.create_sign(parameters, method_req, path_req)
        self.headers.update(
            {
                "key": self.access_key,
                "signTimestamp": str(self.timestamp),
                "signature": sign,
            }
        )
        print("\033[1;32m ---headers---\033[0m", self.headers)
        res = ClientHttp(
            self.host_gateway,
            path_req,
            parameters,
            self.headers).post()
        print(res)
        assert res["id"] != ""
