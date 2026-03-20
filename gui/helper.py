import datetime


class Helper:
    """
    帮助类
    """

    @staticmethod
    def print(msg):
        """
        打印和记录消息
        :param msg:
        :return:
        """
        time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f'{msg} 当前时间：{time}')

    @staticmethod
    def get_time():
        """
        获取时间字符串%Y-%m-%d %H:%M:%S
        :return:
        """
        return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


class AutoMsg:
    """
    定义自动化操作的结果类
    """

    def __init__(self):
        self.result = 0
        self.message = ""
        self.errcode = ""

    def get_result(self):
        """
        获取结果信息 1 成功 -1失败 0未知
        :return:
        """
        return self.result

    def get_errcode(self):
        """
        获取错误的编码
        :return:
        """
        return self.errcode


class UserNotFoundError(Exception):
    """
    微信用户没有找到异常
    """
    pass


class AppNotFoundError(Exception):
    """
    没有找到应用程序
    """
    pass


class EleNotFoundError(Exception):
    """
    没有找到应用程序
    """
    pass