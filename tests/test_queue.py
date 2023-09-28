import unittest
from src.queue import Queue

class TestQueue(unittest.TestCase):
    def test_enqueue_dequeue(self):
        """
        Тестирование правильности работы методов enqueue и dequeue для класса Queue.
        """
        # Создаем экземпляр класса Queue для тестирования
        queue = Queue()

        # Добавляем элементы в очередь
        queue.enqueue('data1')
        queue.enqueue('data2')
        queue.enqueue('data3')

        # Проверяем, что элементы удаляются из очереди в правильном порядке
        self.assertEqual(queue.dequeue(), 'data1')
        self.assertEqual(queue.dequeue(), 'data2')

        # Добавляем еще один элемент
        queue.enqueue('data4')

        # Проверяем, что элементы удаляются в правильном порядке после добавления нового элемента
        self.assertEqual(queue.dequeue(), 'data3')
        self.assertEqual(queue.dequeue(), 'data4')

        # Проверяем, что очередь вызывает исключение, когда пытаемся извлечь элемент из пустой очереди.
        with self.assertRaises(Exception):
            queue.dequeue()

if __name__ == '__main__':
    unittest.main()
