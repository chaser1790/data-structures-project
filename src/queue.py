class Node:
    """
    Класс для узла очереди.
    """

    def __init__(self, data, next_node=None):
        """
        Конструктор класса Node.

        :param data: данные, которые будут храниться в узле
        :param next_node: ссылка на следующий узел очереди
        """
        self.data = data
        self.next_node = next_node

class Queue:
    """
    Класс для очереди.
    """

    def __init__(self):
        """
        Конструктор класса Queue. Инициализирует пустую очередь.
        """
        self.head = None
        self.tail = None

    def enqueue(self, data):
        """
        Метод для добавления элемента в очередь.

        :param data: данные, которые будут добавлены в очередь
        """
        new_node = Node(data)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next_node = new_node
            self.tail = new_node

    def dequeue(self):
        """
        Метод для удаления элемента из очереди и возвращает данные удаленного элемента.

        :return: данные удаленного элемента или None, если очередь пуста
        """
        if self.head is None:
            return None
        data = self.head.data
        self.head = self.head.next_node
        if self.head is None:
            self.tail = None
        return data