# -*- coding:utf-8 -*-
import time
from common_utils.client_http import *

# dev env host
# host = "https://dev-spot-asset-transfer.internal.poloniex.com"
# test env host
host = "https://test-spot-asset-transfer.internal.poloniex.com"
# sandbox env host
# host = "https://sand-spot-asset-transfer.internal.poloniex.com"

path_transfer = "/inner/account/transfer"
path_Auth = "/api/v1/token"
header_auth = {"Content-Type": "application/json"}
service_auth = ClientHttp(host, path_Auth, {}, header_auth)
response_auth = service_auth.get()
Authorization = response_auth.get("data").get("token")
header_transfer = {
    "Content-Type": "application/json",
    "Authorization": Authorization}
businessId = time.time()
# Test environment currency list
currencyId = [214, 28, 267, 125, 400, 315, 321, 243, 313, 299, 320, 668, 327]
# sandbox environment currency list
# currencyId = [214, 299, 315, 542, 327, 267, 400, 324, 320, 28, 668]
# List of users who need to add assets
# 测试环境出款账户是20100，sandbox环境出款账户是10002
toUserId = [30015]
for user in toUserId:
    for coin in currencyId:
        if coin == 28:
            amount = 100
        else:
            amount = 10000
        params = {
            "amount": amount,
            "businessId": businessId,
            "businessType": "201",
            "currencyId": coin,
            "fromUserId": 10002,
            "remark": "add fund",
            "toUserId": user,
        }
        service_transfer = ClientHttp(
            host, path_transfer, params, header_transfer)
        response_transfer = service_transfer.post()
        print(response_transfer)
        businessId = businessId + 1


# 给测试环境压测用户20100--20299增加资产
# toUserId = 20100
# while toUserId < 20300:
#     for coin in currencyId:
#         params = {
#             "amount": 10000,
#             "businessId": businessId,
#             "businessType": "201",
#             "currencyId": coin,
#             "fromUserId": 20100,
#             "remark": "测试",
#             "toUserId": toUserId,
#         }
#         a = ClientHttp(host, path_transfer, params, header_transfer)
#         b = a.post()
#         print(b)
#         businessId = businessId + 1
#     toUserId = toUserId + 1
