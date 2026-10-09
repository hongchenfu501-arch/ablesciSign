#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import requests

# 从环境变量读取 Server酱 SendKey
SCKEY = os.getenv("SCKEY", "").strip()


def serverJ(title, content):
    """通过 Server酱发送通知"""
    if not SCKEY:
        print("Server酱的 SCKEY 未设置")
        return

    print("Server酱服务启动")
    data = {
        "text": title,
        "desp": content.replace("\n", "\n\n"),
    }

    try:
        response = requests.post(
            f"https://sctapi.ftqq.com/{SCKEY}.send",
            data=data,
            timeout=15,
        )
        print("HTTP 状态码:", response.status_code)
        response.raise_for_status()

        result = response.json()
        if result.get("code") == 0 or result.get("data", {}).get("errno") == 0:
            print("Server酱推送成功！")
        else:
            print("Server酱推送失败:", result)

    except requests.RequestException as e:
        print("Server酱请求失败:", e)
    except ValueError:
        print("Server酱返回的内容不是有效 JSON")


def send(title, content):
    """发送 Server酱通知"""
    print(f"通知标题: {title}")
    print(f"通知内容:\n{content}")

    if not SCKEY:
        print("未配置 SCKEY，跳过通知发送")
        return

    serverJ(title, content)


if __name__ == "__&#8203;main__":
    send("测试通知", "这是一条测试通知消息")
