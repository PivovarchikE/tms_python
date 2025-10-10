from abc import ABC, abstractmethod
"""
Паттерн «Фабричный метод»
• Создайте абстрактный класс Animal, у которого есть
абстрактный метод speak.
• Создайте классы Dog и Cat, которые наследуют от Animal и
реализуют метод speak.
• Создайте класс AnimalFactory, который использует паттерн
«Фабричный метод» для создания экземпляра Animal. Этот
класс должен иметь метод create_animal, который принимает
строку («dog» или «cat») и возвращает соответствующий
объект (Dog или Cat).
"""


class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass


class Dog(Animal):
    def speak(self) -> str:
        return "woof woof woof"


class Cat(Animal):
    def speak(self) -> str:
        return "meow meow meow"


class AnimalFactory:
    def create_animal(self, animal_type: str) -> Animal:
        if animal_type == "cat":
            return Cat()
        elif animal_type == "dog":
            return Dog()
        else:
            raise ValueError('Expected value dog or cat')


factory = AnimalFactory()
barsik = factory.create_animal("cat")
print(barsik.speak())
tuzik = factory.create_animal("dog")
print(tuzik.speak())
kesha = factory.create_animal("parrot")
