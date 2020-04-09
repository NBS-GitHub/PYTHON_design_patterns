from strategy.drinkstrategies.drink_strategy import DrinkStrategy


class CoffeeDrinkStrategy(DrinkStrategy):
    def drink(self):
        print("is drinking some coffee...")
