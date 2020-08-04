#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import re
import unittest
from tools.logger import log
from common.readconfig import ini
from selenium import webdriver
from page_object.searchpage import SearchPage

driver = None


def setUpModule():
    global driver
    if driver is None:
        driver = webdriver.Chrome()


def tearDownModule():
    driver.quit()


class TestSearch(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.search = SearchPage(driver)
        cls.search.get_url(ini.url)

    @classmethod
    def tearDownClass(cls) -> None:
        pass

    def test_001(self):
        """搜索"""
        self.search.input_search("selenium")
        self.search.click_search()
        result = re.search(r'selenium', self.search.getSource)
        log.info(result)
        assert result

    def test_002(self):
        """测试搜索候选"""
        self.search.input_search("selenium")
        log.info(list(self.search.imagine))
        assert all(["selenium" in i for i in self.search.imagine])


if __name__ == '__main__':
    unittest.main(verbosity=2)
