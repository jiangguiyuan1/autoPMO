from wechat import *
import random

if __name__ == '__main__':
    path = "D:\\WeChat\\WeChat.exe"
    # 消息内容
    num = random.randint(10000, 40000)
    send_msg = f"2023“网聚职工正能量 争做中国好网民”活动启动.{num}"
    # pyautogui.hotkey('ctrl', 'alt', 'w')
    chat = Wechat(path)
    user_name = '文件传输助手'
    info = chat.send_msg(user_name, send_msg)
    if info.result == -1:
        print(f"错误代码是：{info.errcode}，错误信息是：{info.message}")