import unittest
import TestCase.test.HtmlTestRunner as HtmlTestRunner
import os

from TestCase.test.homepage_test import TestHomePage
from TestCase.test.registration_test import TestRegistration
from TestCase.test.login_test import TestLogin
from TestCase.test.logout_test import TestLogout
from TestCase.test.demosite_test import TestDemoSite
from TestCase.test.address_test import TestAddress
from TestCase.test.shopping_test import TestShopping
from TestCase.test.order_test import TestShoppingOrder

from TestCase.test.account_test import TestAccountDetails


import datetime

dir = os.getcwd()


test_suite = unittest.TestSuite()


test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestLogin))
test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestDemoSite))
test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestShoppingOrder))



"""test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestAccountDetails))
test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestHomePage))
test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestRegistration))
test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestLogin))
test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestDemo))
test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestDemoSite))
test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestAddress))
test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestShopping))
test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestShoppingOrder))
"""


# open the report file
date = datetime.datetime.now().strftime("%Y-%m-%d")
outfile = open(dir +  "/demo.html", "w")

# configure HTMLTestRunner options
# runner = HtmlTestRunner.HTMLTestRunner(stream=outfile, report_title='Test Report', descriptions='Acceptance Tests')
runner = HtmlTestRunner.HTMLTestRunner(stream=outfile,verbosity=2,title='TEST REPORT',description='This is a website test report')

# run the suite using HTMLTestRunner
runner.run(test_suite)