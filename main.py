class Pizza:
    def __init__(self):
        self.dough = None
        self.sauce = None
        self.topping = None

    def set_dough(self, dough):
        self.dough = dough

    def set_sauce(self, sauce):
        self.sauce = sauce

    def set_topping(self, topping):
        self.topping = topping


class PizzaBuilder:
    def __init__(self):
        self.pizza = Pizza()

    def build(self):
        return self.pizza


class MargheritaPizzaBuilder(PizzaBuilder):
    def set_dough(self):
        self.pizza.set_dough("Regular dough")

    def set_sauce(self):
        self.pizza.set_sauce("Tomato sauce")

    def set_topping(self):
        self.pizza.set_topping("Mozzarella cheese")


class PepperoniPizzaBuilder(PizzaBuilder):
    def set_dough(self):
        self.pizza.set_dough("Thick dough")

    def set_sauce(self):
        self.pizza.set_sauce("Tomato sauce")

    def set_topping(self):
        self.pizza.set_topping("Pepperoni and cheese")


class PineapplePizzaBuilder(PizzaBuilder):
    def set_dough(self):
        self.pizza.set_dough("Thin dough")

    def set_sauce(self):
        self.pizza.set_sauce("Barbecue sauce")

    def set_topping(self):
        self.pizza.set_topping("Ham, pineapple, and cheese")


class MushroomPizzaBuilder(PizzaBuilder):
    def set_dough(self):
        self.pizza.set_dough("Regular dough")

    def set_sauce(self):
        self.pizza.set_sauce("Tomato sauce")

    def set_topping(self):
        self.pizza.set_topping("Mushrooms, onions, and cheese")

class Director:
    def __init__(self, builder):
        self.builder = builder

    def construct(self):
        self.builder.set_dough()
        self.builder.set_sauce()
        self.builder.set_topping()


margherita_builder = MargheritaPizzaBuilder()
director = Director(margherita_builder)
director.construct()
margherita_pizza = margherita_builder.build()

pepperoni_builder = PepperoniPizzaBuilder()
director = Director(pepperoni_builder)
director.construct()
pepperoni_pizza = pepperoni_builder.build()

pineapple_builder = PineapplePizzaBuilder()
director = Director(pineapple_builder)
director.construct()
pineapple_pizza = pineapple_builder.build()

mushroom_builder = MushroomPizzaBuilder()
director = Director(mushroom_builder)
director.construct()
mushroom_pizza = mushroom_builder.build()

print("Margherita pizza:")
print(f"Dough: {margherita_pizza.dough}")
print(f"Sauce: {margherita_pizza.sauce}")
print(f"Topping: {margherita_pizza.topping}")

print("\nPepperoni pizza:")
print(f"Dough: {pepperoni_pizza.dough}")
print(f"Sauce: {pepperoni_pizza.sauce}")
print(f"Topping: {pepperoni_pizza.topping}")

print("\nPineapple pizza:")
print(f"Dough: {pineapple_pizza.dough}")
print(f"Sauce: {pineapple_pizza.sauce}")
print(f"Topping: {pineapple_pizza.topping}")

print("\nMushroom pizza:")
print(f"Dough: {mushroom_pizza.dough}")
print(f"Sauce: {mushroom_pizza.sauce}")
print(f"Topping: {mushroom_pizza.topping}")
margherita_builder = MargheritaPizzaBuilder()
director = Director(margherita_builder)
director.construct()
margherita_pizza = margherita_builder.build()

pepperoni_builder = PepperoniPizzaBuilder()
director = Director(pepperoni_builder)
director.construct()
pepperoni_pizza = pepperoni_builder.build()
