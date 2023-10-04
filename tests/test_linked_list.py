import unittest
from src.linked_list import Node, LinkedList

class TestLinkedList(unittest.TestCase):
    def test_insert_beginning(self):
        """
        Тестирование метода insert_beginning, который выполняет вставку элемента в начало связанного списка.
        """

        ll = LinkedList()  # Создаем пример связанного списка
        ll.insert_beginning({'id': 1})  # Вставляем элемент в начало списка
        self.assertEqual(str(ll), "{'id': 1} -> None")  # Проверяем корректность добавления элемента

        ll.insert_beginning({'id': 0})  # Добавляем еще один элемент в начало списка
        self.assertEqual(str(ll), "{'id': 0} -> {'id': 1} -> None")  # Проверяем корректность добавления элемента

    def test_insert_at_end(self):
        """
        Тестирование метода insert_at_end, который выполняет вставку элемента в конец связанного списка.
        """

        ll = LinkedList()  # Создаем пример связанного списка
        ll.insert_at_end({'id': 1})  # Вставляем элемент в конец списка
        self.assertEqual(str(ll), "{'id': 1} -> None")  # Проверяем корректность добавления элемента

        ll.insert_at_end({'id': 2})  # Добавляем еще один элемент в конец списка
        self.assertEqual(str(ll), "{'id': 1} -> {'id': 2} -> None")  # Проверяем корректность добавления элемента

    def test_combo_insert(self):
        """
        Тестирование комбинированного использования методов insert_beginning и insert_at_end.
        """

        ll = LinkedList()  # Создаем пример связанного списка
        ll.insert_beginning({'id': 1})  # Вставляем элемент в начало списка
        ll.insert_at_end({'id': 2})  # Вставляем элемент в конец списка
        ll.insert_at_end({'id': 3})  # Вставляем еще один элемент в конец списка
        ll.insert_beginning({'id': 0})  # Вставляем элемент в начало списка

        # Проверяем корректность комбинации вставки элементов в начало и конец списка
        self.assertEqual(str(ll), "{'id': 0} -> {'id': 1} -> {'id': 2} -> {'id': 3} -> None")

if __name__ == '__main__':
    unittest.main()  # Запускаем все тесты
