# -*- encoding: UTF-8 -*-
"""
 @desc:
 @author: lichao
 @software: PyCharm  on 2020/10/13

"""
import os
import yaml.loader

config_dir_path = os.path.join(os.path.abspath(os.path.dirname(__file__)))
env_file_path = os.path.join(config_dir_path, "env.yaml")


def parse_config(filepath):
    try:
        result = yaml.safe_load(open(filepath))
        return result
    except Exception as e:
        print(e)


def ConfigRead():
    data = parse_config(env_file_path)
    if data["Switch"]["env"] == "DEV":
        return {
            "host_gateway": data["DEV"]["host_gateway"],
            "access_key": data["DEV"]["access_key"],
            "secret_key": data["DEV"]["secret_key"],
        }
    if data["Switch"]["env"] == "TEST":
        return {
            "host_gateway": data["TEST"]["host_gateway"],
            "access_key": data["TEST"]["access_key"],
            "secret_key": data["TEST"]["secret_key"],
        }
    if data["Switch"]["env"] == "SAND":
        return {
            "host_gateway": data["SAND"]["host_gateway"],
            "access_key": data["SAND"]["access_key"],
            "secret_key": data["SAND"]["secret_key"],
        }
    if data["Switch"]["env"] == "PROD":
        return {
            "host_gateway": data["PROD"]["host_gateway"],
            "access_key": data["PROD"]["access_key"],
            "secret_key": data["PROD"]["secret_key"],
        }


data = ConfigRead()
