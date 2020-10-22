class Observer:

    def update(self, state):
        pass

class Subject:

    def __init__(self):
        self.__observers = []

    def register(self, observer):
        self.__observers.append(observer)

    def notify_observers(self, state):
        for observer in self.__observers:
            observer.update(state)