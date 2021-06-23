import unittest
from case.login_test import LoginTest

class Start(unittest.TestCase):

    def driven(self):
        ts = unittest.TestSuite()
        loader = unittest.TestLoader()
        tests = loader.loadTestsFromNames()
        ts.addTests(tests)
        pass

    # def driven(self):
    #     ts = unittest.TestSuite()
    #     loader = unittest.TestLoader()
    #     tests = loader.loadTestsFromNames()
    #     ts.addTests(tests)
    #     pass