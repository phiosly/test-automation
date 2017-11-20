__author__ = 'phiosly'
from common.variable import GetVariable as common
import os
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)
from testBLL import webCase as b_case
from testMode import webCase as m_case
from testRunner.runnerBase import TestInterfaceCase
class testComment(TestInterfaceCase):
    def __init__(self, methodName=''):
        super(testComment, self).__init__(methodName)
        self.bc = b_case.BexceCase(test_module="个人中心", getTempCase=m_case.GetWebInfoCase, BaseTestCase=m_case.GetWebCase)
    def my_comment(self):
        self.bc.execCase(PATH("../yaml/web/my_comment.yaml"), test_name="my_comment", isLast="1")

    @staticmethod
    def tearDownClass():
        common.DRIVER.quit()
    def test_home(self):
        self.my_comment()


