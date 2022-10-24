# Домашнее задание advance #03 (дескрипторы, метаклассы, ABC)

### 1. Метакласс, который в начале названий всех атрибутов и методов, кроме магических, добавляет префикс "custom_"
Подменяться должны так же атрибуты экземпляра после создания экземпляра класса (dynamic в примере).

```py
    class CustomMeta():
        pass

    class CustomClass(metaclass=CustomMeta):
        x = 50

        def __init__(self, val=99):
            self.val = val

        def line(self):
            return 100

        def __str__(self):
            return "Custom_by_metaclass"

    inst = CustomClass()
    inst.custom_x == 50
    inst.custom_val == 99
    inst.custom_line() == 100
    CustomClass.custom_x == 50
    str(inst) == "Custom_by_metaclass"

    inst.dynamic = "added later"
    inst.custom_dynamic == "added later"
    inst.dynamic  # ошибка

    inst.x  # ошибка
    inst.val  # ошибка
    inst.line() # ошибка
    inst.yyy  # ошибка
    CustomClass.x  # ошибка
```


### 2. Дескрипторы с проверками типов и значений данных

```py
    class Integer:
        pass

    class String:
        pass

    class PositiveInteger:
        pass

    class Data:
        num = Integer()
        name = String()
        price = PositiveInteger()

        def __init__(...):
            ....
```


### 3. Тесты в отдельном модуле

### 4. Перед отправкой на проверку код должен быть прогнан через flake8 и pylint, по желанию еще black
