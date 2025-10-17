from __future__ import annotations


"""
Паттерн «Строитель»
• Создайте класс Pizza, который содержит следующие
атрибуты: size, cheese, pepperoni, mushrooms, onions, bacon.
• Создайте класс PizzaBuilder, который использует паттерн
«Строитель» для создания экземпляра Pizza. Этот класс
должен содержать методы для добавления каждого из
атрибутов Pizza.
• Создайте класс PizzaDirector, который принимает экземпляр
PizzaBuilder и содержит метод make_pizza, который
использует PizzaBuilder для создания Pizza.
"""


class Pizza:
    """Класс пиццы - продукт, который мы создаем"""

    def __init__(self):
        self.size = None
        self.cheese = False
        self.pepperoni = False
        self.mushrooms = False
        self.onions = False
        self.bacon = False

    def __str__(self):
        ingredients = []
        if self.cheese:
            ingredients.append("сыр")
        if self.pepperoni:
            ingredients.append("пепперони")
        if self.mushrooms:
            ingredients.append("грибы")
        if self.onions:
            ingredients.append("лук")
        if self.bacon:
            ingredients.append("бекон")

        ingredients_str = ", ".join(ingredients) if ingredients \
            else "без добавок"
        return f"Пицца {self.size} с {ingredients_str}"


class PizzaBuilder:
    """Строитель пиццы - создает пиццу пошагово"""

    def __init__(self):
        self.pizza = Pizza()

    def set_size(self, size):
        """Устанавливает размер пиццы"""
        self.pizza.size = size
        return self

    def add_cheese(self):
        """Добавляет сыр"""
        self.pizza.cheese = True
        return self

    def add_pepperoni(self):
        """Добавляет пепперони"""
        self.pizza.pepperoni = True
        return self

    def add_mushrooms(self):
        """Добавляет грибы"""
        self.pizza.mushrooms = True
        return self

    def add_onions(self):
        """Добавляет лук"""
        self.pizza.onions = True
        return self

    def add_bacon(self):
        """Добавляет бекон"""
        self.pizza.bacon = True
        return self

    def build(self):
        """Возвращает готовую пиццу"""
        return self.pizza


class PizzaDirector:
    """Директор - использует строитель для создания пиццы"""

    def __init__(self, builder):
        self.builder = builder

    def make_pizza(self, size="средняя", ingredients=None):
        if ingredients is None:
            ingredients = []

        self.builder.set_size(size)

        for ingredient in ingredients:
            if ingredient == "cheese":
                self.builder.add_cheese()
            elif ingredient == "pepperoni":
                self.builder.add_pepperoni()
            elif ingredient == "mushrooms":
                self.builder.add_mushrooms()
            elif ingredient == "onions":
                self.builder.add_onions()
            elif ingredient == "bacon":
                self.builder.add_bacon()

        return self.builder.build()


if __name__ == "__main__":
    builder = PizzaBuilder()

    director = PizzaDirector(builder)

    pizza1 = director.make_pizza("большая",
                                 ["cheese", "pepperoni", "mushrooms"])
    print(f"Пицца 1: {pizza1}")

    pizza2 = director.make_pizza("маленькая", ["cheese", "bacon"])
    print(f"Пицца 2: {pizza2}")

    builder2 = PizzaBuilder()
    pizza3 = (builder2
              .set_size("средняя")
              .add_cheese()
              .add_onions()
              .add_bacon()
              .build())
    print(f"Пицца 3: {pizza3}")
