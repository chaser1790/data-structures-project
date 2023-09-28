class Node:
    """
    Класс для узла стека.
    """

    def __init__(self, data, next_node=None):
        """
        Конструктор класса Node.

        :param data: данные, которые будут храниться в узле.
        :param next_node: ссылка на следующий узел стека.
        """
        self.data = data
        self.next_node = next_node

class Stack:
    """
    Класс для стека.
    """

    def __init__(self):
        """
        Конструктор класса Stack.
        Создает пустой стек.
        """
        self.top = None

    def push(self, data):
        """
        Метод для добавления элемента на вершину стека.

        :param data: данные, которые будут добавлены на вершину стека.
        """
        new_node = Node(data, self.top)
        self.top = new_node

    def pop(self):
        """
        Метод для удаления элемента с вершины стека и его возвращения.

        :return: данные удаленного элемента.
        :raise: исключение, если стек пуст.
        """
        if self.top is None:
            raise Exception('Стек пуст')
        else:
            data = self.top.data
            self.top = self.top.next_node
            return data

    def __str__(self):
        """
        Магический метод для строкового представления объекта.
        Возвращает строку, представляющую содержимое стека.
        """
        current = self.top
        result = []
        while current:
            result.append(str(current.data))
            current = current.next_node
        return '\n'.join(result)