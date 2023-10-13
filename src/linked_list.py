class Node:
    def __init__(self, data, next_node=None):
        self.data = data  # Значение текущего узла
        self.next_node = next_node  # Ссылка на следующий узел


class LinkedList:
    """
    Класс, представляющий односвязный список.
    """
    def __init__(self):
        self.head = None  # Головной узел списка
        self.tail = None  # Хвостовой узел списка

    def __str__(self):
        """
        Метод для вывода связного списка в виде строки.

        :return: строковое представление данных в списке
        """
        node = self.head
        nodes = []
        while node is not None:  # Пока узел не является пустым
            nodes.append(str(node.data))  # Добавляем значение текущего узла в список
            node = node.next_node  # Переходим к следующему узлу
        nodes.append("None")
        return " -> ".join(nodes)  # Преобразуем список в строку

    def insert_beginning(self, data: dict) -> None:
        """
        Метод для добавления узла в начало связного списка.

        :param data: Значение для узла.
        """
        new_node = Node(data, self.head)  # Создаем новый узел
        if not self.head:  # Если список пуст
            self.tail = new_node  # Новый узел становится хвостовым узлом
        self.head = new_node  # Новый узел становится головным узлом

    def insert_at_end(self, data: dict) -> None:
        """
        Метод для добавления узла в конец связного списка.

        :param data: Значение для узла.
        """
        if not self.head:  # Если список пуст
            self.insert_beginning(data)  # Добавляем узел в начало
        else:
            new_node = Node(data)  # Создаем новый узел
            self.tail.next_node = new_node  # Устанавливаем ссылку от предыдущего хвоста к новому узлу
            self.tail = new_node  # Новый узел становится хвостовым

    def to_list(self):
        """
        Метод для преобразования связного списка в стандартный список Python.

        :return: список со значениями узлов
        """
        res_list = []  # Инициализируем пустой список
        node = self.head

        while node:  # Пока узел не является пустым
            res_list.append(node.data)  # Добавляем данные узла в список
            node = node.next_node  # Переходим к следующему узлу

        return res_list

    def get_data_by_id(self, id):
        """
        Метод для поиска в списке данных с указанным id.

        :param id: id, по которому производится поиск
        :return: данные узла или None, если такого id нет в списке
        """
        node = self.head

        while node:  # Пока узел не является пустым
            try:
                if node.data.get('id') == id:  # Если id узла соответствует заданному
                    return node.data  # Возвращаем данные этого узла
            except (TypeError, AttributeError):  # Если данные не являются словарем или в словаре нет элемента 'id'
                print('Данные не являются словарем или в словаре нет ключа id.')

            node = node.next_node  # Переходим к следующему узлу

        return None  # Если в списке не найдено данных с заданным id
