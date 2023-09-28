from src.queue import Queue

if __name__ == '__main__':
    queue = Queue()

    # Магический метод __str__ возвращает пустую строку
    assert str(Queue()) == ""

    # Добавляем данные в очередь
    queue.enqueue('data1')
    queue.enqueue('data2')
    queue.enqueue('data3')

    # Проверяем очередность хранения данных
    assert queue.head.data == 'data1'
    assert queue.head.next_node.data == 'data2'
    assert queue.tail.data == 'data3'
    assert queue.tail.next_node is None

    # Проверяем магический метод __str__
    assert str(queue) == "data1\ndata2\ndata3"

    # Проверяем вывод, который вызывает ошибку AttributeError
    if queue.tail.next_node is not None:
        print(queue.tail.next_node.data)
    else:
        print("Очередь пуста")