#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import os
import unittest
from config.conf import TEST_SUITES, REPORT_PATH
from tools.send_mail import send_report_mail
from tools.times import datetime_strftime
from tools.HTMLTestRunner_cn import HTMLTestRunner

discover = unittest.defaultTestLoader.discover(TEST_SUITES, pattern="test*.py")


def report_path():
    """报告文件"""
    if not os.path.exists(REPORT_PATH):
        os.makedirs(REPORT_PATH)
    return os.path.join(REPORT_PATH, '{}.html'.format(datetime_strftime("%Y%m%d_%H%M%S")))


if __name__ == "__main__":
    try:
        with open(report_path(), 'wb+') as fp:
            runner = HTMLTestRunner(stream=fp,
                                    title="测试结果",
                                    description="用例执行情况",
                                    verbosity=2,
                                    retry=1,
                                    save_last_try=True)
            runner.run(discover)
    except Exception as e:
        print("用例执行失败:{}".format(e))
    else:
        send_report_mail()
