# Задача №1 "Ферма Дядюшки Джо"
from pprint import pprint


class Cow:
    'Корова'
    def __init__(self, name, weight, satiety=5, voice="Мууу"):
        self.name = name
        self.weight = weight
        self.satiety = satiety
        self.voice = voice

    def feed(self, eat):
        self.satiety += eat
        return 'Покормили'

    def milking(self):
        if self.satiety >= 5:
            self.satiety -= 2
            return 'Надоили 2 ведра молока.'
        elif 0 < self.satiety < 5:
            self.satiety -= 1
            return 'Надоили 1 ведро молока.'
        else:
            return 'Нужно покормить'
    pass


class Goat:
    'Коза'
    def __init__(self, name, weight, satiety=5, voice="Меее"):
        self.name = name
        self.weight = weight
        self.satiety = satiety
        self.voice = voice

    def milking(self):
        if self.satiety >= 5:
            self.satiety -= 2
            return 'Надоили 2 литра молока.'
        elif 0 < self.satiety < 5:
            self.satiety -= 1
            return 'Надоили 1 литр молока.'
        else:
            return 'Нужно покормить'
    pass


class Ram:
    'Баран'
    def __init__(self, name, weight, satiety=5, voice="Беее"):
        self.name = name
        self.weight = weight
        self.satiety = satiety
        self.voice = voice

    def feed(self, eat):
        self.satiety += eat
        return 'Покормили'

    def cut(self):
        if self.satiety >= 5:
            self.satiety -= 2
            return 'Настригли 2 корзины шерсти.'
        elif 0 < self.satiety < 5:
            self.satiety -= 1
            return 'Настригли 1 корзину шерсти.'
        else:
            return 'Нужно покормить.'
    pass


class Goose:
    'Гусь'
    def __init__(self, name, weight, satiety=5, voice="Гага"):
        self.name = name
        self.weight = weight
        self.satiety = satiety
        self.voice = voice

    def feed(self, eat):
        self.satiety += eat
        return 'Покормили'

    def coll_eggs(self):
        if self.satiety >= 5:
            self.satiety -= 2
            return 'Собрали 5 яиц.'
        elif 0 < self.satiety < 5:
            self.satiety -= 1
            return 'Собрали 2 яйца.'
        else:
            return 'Нужно покормить.'


class Hen:
    'Курица'
    def __init__(self, name, weight, satiety=5, voice="Коооо"):
        self.name = name
        self.weight = weight
        self.satiety = satiety
        self.voice = voice

    def feed(self, eat):
        self.satiety += eat
        return 'Покормили'

    def coll_eggs(self):
        if self.satiety >= 5:
            self.satiety -= 2
            return 'Собрали 5 яиц.'
        elif 0 < self.satiety < 5:
            self.satiety -= 1
            return 'Собрали 2 яйца.'
        else:
            return 'Нужно покормить.'


class Duck:
    'Утка'
    def __init__(self, name, weight, satiety=5, voice="Крякря"):
        self.name = name
        self.weight = weight
        self.satiety = satiety
        self.voice = voice

    def feed(self, eat):
        self.satiety += eat
        return 'Покормили'

    def coll_eggs(self):
        if self.satiety >= 5:
            self.satiety -= 2
            return 'Собрали 5 яиц.'
        elif 0 < self.satiety < 5:
            self.satiety -= 1
            return 'Собрали 2 яйца.'
        else:
            return 'Нужно покормить.'


def main():
    manya = Cow("Манька", 500)
    roga = Goat("Рога", 60)
    kopyta = Goat("Копыта", 70)
    barash = Ram("Барашек", 45)
    kudryav = Ram("Кудрявый", 50)
    seriy = Goose("Серый", 15)
    beliy = Goose("Белый", 5)
    ko_ko = Hen("Ко-Ко", 3)
    kukareku = Hen("Кукареку", 4)
    kryakva = Duck("Кряква", 5)
    animals = [manya, roga, kopyta, barash, kudryav, seriy, beliy, ko_ko, kukareku, kryakva]
    total_weight = 0
    weight = 0
    name_animal_max_weight = ''

    for animal in animals:
        total_weight = total_weight + animal.weight
        if weight < animal.weight:
            weight = animal.weight
            name_animal_max_weight = animal.__doc__

    print(f'Общий вес животных: {total_weight}.')
    print(f'Самое тяжелое жимотное: {name_animal_max_weight}.')


if __name__ == __name__:
    main()
