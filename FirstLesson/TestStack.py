from random import random
import unittest as test
from Stack import Stack


class TestStack(test.TestCase):
    __dataToCheck = [(random() * i for i in range(1, 101))]

    def setUp(self):
        self.stack = Stack()

    def tearDown(self):
        self.stack.clear()

    def __addInStackValues(self):
        for val in TestStack.__dataToCheck:
            self.stack.push(val)

    def testPush(self):
        for index, val in enumerate(TestStack.__dataToCheck):
            self.stack.push(val)

            self.assertEqual(index + 1, len(self.stack))
            self.assertEqual(val, self.stack.back())

    def testPop(self):
        self.__addInStackValues()
        for val in TestStack.__dataToCheck[::-1]:
            self.assertEqual(val, self.stack.pop())

        self.assertEqual('ok', self.stack.pop())

    def testBack(self):
        valToPush = 5
        self.assertEqual('ok', self.stack.back())
        self.stack.push(valToPush)
        self.assertEqual(valToPush, self.stack.back())

    def testClear(self):
        self.__addInStackValues()
        self.assertTrue(len(self.stack) != 0)

        self.stack.clear()
        self.assertTrue(len(self.stack) == 0)

        self.stack.clear()
        self.assertTrue(len(self.stack) == 0)


if __name__ == '__main__':
    test.main()
