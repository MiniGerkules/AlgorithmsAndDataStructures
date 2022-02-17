'''
    В этой задаче было необходимо реализовать стек при помощи структуры
vector или её аналога в используемом вами языке (list для Python, List<T>
для C#, ArrayList<T> для Java и т.п.). Особое внимание следует обратить 
на формат ответа вашей программы на каждую из команд:
    • Команда push требовала вывод 'ok'
    • Команда clear требовала вывод 'ok'
    • Команда pop требовала вывод удаляемого элемента или сообщения
    'error', если стек пуст
    • Команда back требовала вывод сообщения 'error', если стек пуст
'''

class Stack:
    def __init__(self):
        self.__data = []

    def __len__(self) -> int:
        return len(self.__data)

    def __isEmpty(self) -> bool:
        return len(self.__data) == 0

    def push(self, newElem) -> None:
        self.__data.append(newElem)

    def pop(self):
        return self.__data.pop() if not self.__isEmpty() else 'error'

    def back(self):
        return self.__data[-1] if not self.__isEmpty() else 'error'

    def clear(self) -> None:
        self.__data.clear()
