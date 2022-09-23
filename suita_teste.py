import unittest
import HtmlTestRunner

from alerts import Alerts
from comanda_produse import Test3
from completare_date import Test2
from creare_cont_phptravels import Test1
from herokuapp_login import Login

class TestSuite(unittest.TestCase):

    def test_suite(self):
        teste_de_rulat = unittest.TestSuite()
        teste_de_rulat.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(Test1),
            unittest.defaultTestLoader.loadTestsFromTestCase(Test2),
            unittest.defaultTestLoader.loadTestsFromTestCase(Test3),
            unittest.defaultTestLoader.loadTestsFromTestCase(Alerts),
            unittest.defaultTestLoader.loadTestsFromTestCase(Login)
        ])

        runner = HtmlTestRunner.HTMLTestRunner\
        (
            combine_reports=True,
            report_title='TestReport',
            report_name='Smoke Test Result'
        )

        runner.run(teste_de_rulat)