''''
Created on Jun 5, 2019

@author: Chester
'''

from helper.HTMLTestRunner import HTMLTestRunner
from helper.log import MyLog
import config.config as Config
import os
import unittest
import argparse
from helper.common import Common
from testcases.login_test import LoginTest
from testcases.trusts_edit_test import TrustsEditTest


def get_test_cases():
    ts = unittest.TestSuite()
    tc_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), './testcases')
    # way 1
    tc = unittest.defaultTestLoader.discover(tc_folder,pattern='*edit_test.py')
    # way 2
    #tc = unittest.defaultTestLoader.loadTestsFromTestCase(TrustsEditTest)
    ts.addTests(tc)

    # way 3
    #ts.addTest(LoginTest('test_01_login_with_correct_user_pwd'))
    #ts.addTest(TrustsEditTest('test_01_Pools_button_refresh_dim_mapping'))
    return ts


def run():
    with open('test.txt', "w+") as f:
        runner = unittest.TextTestRunner(f, descriptions='report', verbosity=2)
        runner.run(get_test_cases())


if __name__ == '__main__':
    pass
    import sys

    print(sys.argv)
    run()
