from strategy.drinkstrategies.drink_strategy import DrinkStrategy


class WaterDrinkStrategy(DrinkStrategy):
    def drink(self):
        print("is drinking some water...")
