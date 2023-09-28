import unittest
from src.stack import Stack


class TestStack(unittest.TestCase):
    """
    Тестовый класс для тестирования стека.
    """

    def test_push_pop(self):
        """
        Тестирование правильности работы методов push и pop для класса Stack.
        """
        # Создаем экземпляр класса Stack для тестирования
        stack = Stack()

        # Добавляем элементы в стек
        stack.push('data1')
        stack.push('data2')
        stack.push('data3')

        # Проверяем, что элементы удаляются из стека в правильном порядке
        self.assertEqual(stack.pop(), 'data3')
        self.assertEqual(stack.pop(), 'data2')

        # Добавляем еще один элемент
        stack.push('data4')

        # Проверяем, что элементы удаляются в правильном порядке после добавления нового элемента
        self.assertEqual(stack.pop(), 'data4')
        self.assertEqual(stack.pop(), 'data1')

        # Проверяем, что стек вызывает исключение, когда пытаемся удалить элемент из пустого стека.
        with self.assertRaises(Exception):
            stack.pop()

    def test_str_method(self):
        """
        Тестирование правильности работы магического метода __str__ для класса Stack.
        """
        stack = Stack()

        # Добавляем элементы в стек
        stack.push('data1')
        stack.push('data2')
        stack.push('data3')

        # Проверяем, что магический метод __str__ возвращает правильную строку
        self.assertEqual(str(stack), "data3\ndata2\ndata1")


if __name__ == '__main__':
    unittest.main()