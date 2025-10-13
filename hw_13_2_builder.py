from __future__ import annotations
from abc import ABC, abstractmethod
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


class Pizza(ABC):
    @property
    @abstractmethod
    def pizza(self) -> None:
        pass

    @abstractmethod
    def size(self, value) -> None:
        pass

    @abstractmethod
    def cheese(self) -> None:
        pass

    @abstractmethod
    def pepperoni(self) -> None:
        pass

    @abstractmethod
    def mushrooms(self) -> None:
        pass

    @abstractmethod
    def onions(self) -> None:
        pass

    @abstractmethod
    def bacon(self) -> None:
        pass


class PizzaBuilder(Pizza):
    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._pizza = Pizza1()

    @property
    def pizza(self) -> Pizza1:
        pizza = self._pizza
        self.reset()
        return pizza

    def size(self, value) -> None:
        self._pizza.add(f'Size {value}')

    def cheese(self) -> None:
        self._pizza.add("Cheese")

    def pepperoni(self) -> None:
        self._pizza.add("Pepperoni")

    def mushrooms(self) -> None:
        self._pizza.add("Mushrooms")

    def onions(self) -> None:
        self._pizza.add("Onions")

    def bacon(self) -> None:
        self._pizza.add("Onions")


class Pizza1:
    def __init__(self) -> None:
        self.parts = []

    def add(self, part: Any) -> None:
        self.parts.append(part)

    def list_parts(self) -> None:
        print(f"Pizza size and ingredients: {', '.join(self.parts)}", end="\n")


class PizzaDirector:
    def __init__(self) -> None:
        self._pizza_builder = None

    @property
    def pizza_builder(self) -> PizzaBuilder:
        return self._pizza_builder

    @pizza_builder.setter
    def pizza_builder(self, pizza_builder: PizzaBuilder) -> None:
        self._pizza_builder = pizza_builder

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


director = PizzaDirector()
builder = PizzaBuilder()
director.pizza_builder = builder

print("The most delicious pizza: ")
director.build_pizza_1()
builder.pizza.list_parts()

print("The pizza isn't that tasty: ")
director.build_pizza_2()
builder.pizza.list_parts()
