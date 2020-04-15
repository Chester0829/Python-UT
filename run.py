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
from helper.driver import BoxDriver

def add_args():
    parse = argparse.ArgumentParser(description="run Profectus automation with param")
    parse.add_argument("-n", "--build_num",
                       required=True,
                       type=int,
                       help='build num e.g. 3'
                       )
    parse.add_argument("-c", "--case_list",
                       required=True,
                       help='choose test case to run e.g. data_compare_test'
                       )
    parse.add_argument("-e", "--env",
                       help='choose which environment to run'
                       )
    parse.add_argument("-hl", "--headless",
                       help='headless mode to run automation or not'
                       )
    args = parse.parse_args()
    return args


if __name__ == '__main__':
    args = add_args()
    logger = MyLog.logger_with_file_and_console()
    logger.info('change suffix to build_num')
    MyLog.suffix = str(args.build_num)
    Common.url = args.env
    BoxDriver._headless = args.headless
    cl = args.case_list.split(',')
    logger.info('start run test suite')
    tc_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), './testcases')
    test_suite = unittest.TestSuite()
    if "All" in cl:
        logger.info('execute all the test cases')
        discover = unittest.defaultTestLoader.discover(tc_folder, pattern='*.py')
        test_suite.addTest(discover)
    else:
        for case in cl:
            if os.path.isfile(os.path.join(tc_folder, './' + case + '.py')):
                discover = unittest.defaultTestLoader.discover(tc_folder, pattern=case + '.py')
                test_suite.addTest(discover)
                logger.info('add case %s.py to testsuite list' % case)
            else:
                logger.info('case %s.py not found!!' % case)

    'define HTML report'
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                             "./report/Report-" + Common.get_sufix_time_format(suffix=str(args.build_num)) + ".html")
    logger.info('HTML report is:%s' % file_path)
    file_result = open(file_path, 'wb')

    'define runner'
    runner = HTMLTestRunner(stream=file_result, title=u"Profectus Test Report", description=u"Testcase Result")

    'run tests'
    runner.run(test_suite)
    file_result.close()
