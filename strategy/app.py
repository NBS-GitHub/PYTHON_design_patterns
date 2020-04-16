from strategy.codestrategies.java_code_strategy import JavaCodeStrategy
from strategy.codestrategies.python_code_strategy import PythonCodeStrategy
from strategy.codestrategies.php_code_strategy import PHPCodeStrategy
from strategy.eatstrategies.pizza_eat_strategy import PizzaEatStrategy
from strategy.eatstrategies.pasta_eat_strategy import PastaEatStrategy
from strategy.eatstrategies.burger_eat_strategy import BurgerEatStrategy
from strategy.drinkstrategies.coffee_drink_strategy import CoffeeDrinkStrategy
from strategy.drinkstrategies.tea_drink_strategy import TeaDrinkStrategy
from strategy.drinkstrategies.water_drink_strategy import WaterDrinkStrategy
from strategy.people.programmer import Programmer

# STRATEGY PATTERN ################################################################

print("\n--- STRATEGY PATTERN\n")

# Creating the code strategies
python_code_strategy = PythonCodeStrategy()
java_code_strategy = JavaCodeStrategy()
php_code_strategy = PHPCodeStrategy()

# Creating the eat strategies
pizza_eat_strategy = PizzaEatStrategy()
pasta_eat_strategy = PastaEatStrategy()
burger_eat_strategy = BurgerEatStrategy()

# Creating the drink strategies
coffee_drink_strategy = CoffeeDrinkStrategy()
tea_drink_strategy = TeaDrinkStrategy()
water_drink_strategy = WaterDrinkStrategy()

# Creating the programmers and calling their methods
programmer1 = Programmer("John", python_code_strategy, pasta_eat_strategy, water_drink_strategy)
programmer1.code()
programmer1.eat()
programmer1.drink()

print()

programmer2 = Programmer("Susan", java_code_strategy, burger_eat_strategy, coffee_drink_strategy)
programmer2.code()
programmer2.eat()
programmer2.drink()

print()

programmer3 = Programmer("Henry", php_code_strategy, pizza_eat_strategy, tea_drink_strategy)
programmer3.code()
programmer3.eat()
programmer3.drink()