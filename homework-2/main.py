from src.stack import Stack

# Пример использования и проверки метода pop() класса Stack.
if __name__ == '__main__':
    # Создаем новый стэк.
    stack = Stack()

    # Добавляем элемент с данными 'data1' на вершину стека.
    stack.push('data1')

    # Удаляем элемент с вершины стека и сохраняем значение, возвращает метод pop.
    data = stack.pop()

    # Стек должен стать пустым.
    assert stack.top is None

    # Проверяем удаленный элемент.
    assert data == 'data1'

    stack = Stack()
    stack.push('data1')
    stack.push('data2')
    data = stack.pop()

    # Теперь последний элемент содержит данные 'data1'
    assert stack.top.data == 'data1'

    # Данные удаленного элемента.
    assert data == 'data2'
