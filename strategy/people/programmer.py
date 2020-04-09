class Programmer:
    def __init__(self, name, code_strategy, eat_strategy, drink_strategy):
        self.name = name
        self.code_startegy = code_strategy
        self.eat_strategy = eat_strategy
        self.drink_strategy = drink_strategy

    def code(self):
        print(self.name, end=" ")
        self.code_startegy.code()

    def eat(self):
        print(self.name, end=" ")
        self.eat_strategy.eat()

    def drink(self):
        print(self.name, end=" ")
        self.drink_strategy.drink()
