from strategy.eatstrategies.eat_strategy import EatStrategy


class BurgerEatStrategy(EatStrategy):
    def eat(self):
        print("is eating a burger...")