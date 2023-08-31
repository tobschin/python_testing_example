import unittest
from foo import Foo
from unittest.mock import MagicMock, Mock

class TestFooMethod(unittest.TestCase):
    
    def test_bigger1_should_be_true(self):
        self.assertTrue(Foo().bigger1(2))
    
    def test_should_be_false(self):
        self.assertFalse(Foo().bigger1(-1))
        
    def test_should_mock_true(self):
        testClass = Foo()
        testClass.bigger1 = MagicMock(return_value=True)
        self.assertTrue(testClass.bigger1)
        
    def test_should_mock_false(self):
        testClass = Foo()
        testClass.bigger1 = MagicMock(return_value=False)
        self.assertTrue(testClass.bigger1)

        
    def test_lowerOrEqual1_mock_false(self):
        testClass = Foo()
        testClass.bigger1 = MagicMock(return_value= False)
        self.assertTrue(testClass.lowerOrEqual1(23))