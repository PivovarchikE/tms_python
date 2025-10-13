from __future__ import annotations
from typing import Any


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


class PizzaBuilder:
    def __init__(self):
        self.pizza = Pizza1()

    def size(self, value) -> None:
        self.pizza.add(f'Size {value}')

    def cheese(self) -> None:
        self.pizza.add("Cheese")

    def pepperoni(self) -> None:
        self.pizza.add("Pepperoni")

    def mushrooms(self) -> None:
        self.pizza.add("Mushrooms")

    def onions(self) -> None:
        self.pizza.add("Onions")

    def bacon(self) -> None:
        self.pizza.add("Bacon")

    def build(self) -> Pizza1:
        pizza = self.pizza
        self.pizza = Pizza1()
        return pizza


class Pizza1:
    def __init__(self) -> None:
        self.parts = []

    def add(self, part: Any) -> None:
        self.parts.append(part)

    def list_parts(self) -> None:
        print(f"Pizza size and ingredients: {', '.join(self.parts)}", end="\n")


class PizzaDirector:
    def __init__(self, builder):
        self.builder = builder

    def make_pizza(self, size="средняя", ingredients=None):
        if ingredients is None:
            ingredients = []

        self.builder.size(size)

        for ingredient in ingredients:
            if ingredient == "cheese":
                self.builder.cheese()
            elif ingredient == "pepperoni":
                self.builder.pepperoni()
            elif ingredient == "mushrooms":
                self.builder.mushrooms()
            elif ingredient == "onions":
                self.builder.onions()
            elif ingredient == "bacon":
                self.builder.bacon()

        return self.builder.build()


builder = PizzaBuilder()
director = PizzaDirector(builder)

print("The most delicious pizza: ")
pizza1 = director.make_pizza("Large", ["cheese", "pepperoni", "mushrooms"])
pizza1.list_parts()

print("The pizza isn't that tasty: ")
pizza2 = director.make_pizza("Small", ["cheese"])
pizza2.list_parts()
