class Node:
    def __init__(self, data, next_node=None):
        self.data = data  # Значение узла
        self.next_node = next_node  # Ссылка на следующий узел


class LinkedList:
    def __init__(self):
        self.head = None  # Начальный узел списка
        self.tail = None  # Конечный узел списка

    def insert_beginning(self, data: dict) -> None:
        """
        Метод добавляет узел в начало списка.

        :param data: Значение для узла.
        """
        new_node = Node(data, self.head)  # Создаем новый узел
        if not self.head:  # Если список пуст
            self.tail = new_node  # Новый узел становится концом списка
        self.head = new_node  # Новый узел становится началом списка

    def insert_at_end(self, data: dict) -> None:
        """
        Метод добавляет узел в конец списка.

        :param data: Значение для узла.
        """
        if not self.head:  # Если список пуст
            self.insert_beginning(data)  # добавляем узел в начало
        else:
            new_node = Node(data)  # Создаем новый узел
            self.tail.next_node = new_node  # Прошлой "хвост" ставим ссылку на новый узел
            self.tail = new_node  # Назначаем новый хвост

    def __str__(self) -> str:
        """
        Метод возвращает строковое представление списка.
        """
        node = self.head  # Начинаем с головного узла
        if node is None:  # Если список пуст
            return str(None)

        ll_string = str(node.data)  # Инициализируем строку с начальным узлом
        node = node.next_node  # Двигаемся к следующему узлу
        while node:  # Пока есть узлы в списке
            ll_string += f' -> {str(node.data)}'  # Добавляем значение узла в строку
            node = node.next_node  # Продолжаем двигаться по списку

        ll_string += ' -> None'  # Добавляем в конец '-> None', чтобы указать на конец списка
        return ll_string
