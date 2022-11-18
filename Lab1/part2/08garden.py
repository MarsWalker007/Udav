#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# в саду сорвали цветы
garden = ('ромашка', 'роза', 'одуванчик', 'ромашка', 'гладиолус', 'подсолнух', 'роза', )

# на лугу сорвали цветы
meadow = ('клевер', 'одуванчик', 'ромашка', 'клевер', 'мак', 'одуванчик', 'ромашка', )


# TODO здесь ваш код
garden_set = set(garden)
print(garden_set)
# выведите на консоль все виды цветов
# TODO здесь ваш код
garden2 = set(garden)
meadow2 = set(meadow)
print(garden2.union(meadow2))
# выведите на консоль те, которые растут и там и там
# TODO здесь ваш код
print(garden2 & meadow2)
# выведите на консоль те, которые растут в саду, но не растут на лугу
# TODO здесь ваш код
print(garden2.difference(meadow2))
# выведите на консоль те, которые растут на лугу, но не растут в саду
# TODO здесь ваш код
print(meadow2.difference(garden2))