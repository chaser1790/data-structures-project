import unittest
from src.stack import Stack

class TestStack(unittest.TestCase):
    """Тестовый класс для тестирования стека."""

    def test_push_pop(self):
        """Тестирование правильности работы методов push и pop."""
        stack = Stack()

        stack.push('data1')
        stack.push('data2')
        stack.push('data3')

        self.assertEqual(stack.pop(), 'data3')
        self.assertEqual(stack.pop(), 'data2')

        stack.push('data4')

        self.assertEqual(stack.pop(), 'data4')
        self.assertEqual(stack.pop(), 'data1')

        with self.assertRaises(Exception):
            stack.pop()

if __name__ == '__main__':
    unittest.main()
