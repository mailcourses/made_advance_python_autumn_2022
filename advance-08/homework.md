# Домашнее задание advance #08 (аннотация типов)

### 1. Механизм сбора метрик
Нужно реализовать группу классов для сбора метрик со следующим интерфейсом:
1) `Stats` отвечает за управление сбором метрик, пользователь взаимодействует с данным классом.
   - создание глобального экзампляра `Stats` не нужно: используется либо сам класс, либо `Stats` реализуется как Singleton;
   - `collect` возвращает всю собранную на данный момент непустую статистику и обнуляет значения всех метрик;
   - `timer`, `avg`, `count` возвращают метрику по её имени. Если метрики данного типа с данным именем не существует, то создается новая, регистрируется в `Stats` и возвращается.

2) Классы `MetricTimer`, `MetricAvg`, `MetricCount` отвечают за метрику с определенным именем и типом.
   - `get_name` возвращает полное имя метрики: переданное в конструктор имя + тип метрики через точку;
   - имя, возвращаемое `get_name`, должно генерироваться в экземпляре метрики;
   - `get_value` возвращает текущее значение метрики или, если текущее значение пустое, то None;
   - `add` добавляет новое значение метрики по правилам данной метрики;
   - `clear` очищает метрику до нулевого состояния
   - метрика `MetricTimer` может использоваться как контекстный менеджер;
   - `MetricTimer` собирает суммарное время выполнения;
   - `MetricCount` собирает количество вызовов;
   - `MetricAvg` собирает среднее арифметическое переданных значений;
   - `MetricCount` и `MetricAvg` должны работать независимо друг от друга.


```py
class BaseMetric:
    def __init__(self, name: str):
        NotImplemented

    def get_name(self):
        NotImplemented

    def get_value(self):
        NotImplemented

    def add(self, value):
        NotImplemented

    def clear(self):
        NotImplemented


class MetricTimer:
    pass


class MetricAvg:
    pass


class MetricCount:
    pass


class Stats:
    def timer(name):
        pass

    def avg(name):
        pass

    def count(name):
        pass

    def collect():
        pass


def calc():
    pass

with Stats.timer("calc"):  # 0.1
    res = calc()  # 3

Stats.count("calc").add()
Stats.avg("calc").add(res)

t1 = time()
res = calc()  # 7
t2 = time()
Stats.timer("calc").add(t2 - t1)  # 0.3
Stats.count("calc").add()
Stats.avg("calc").add(res)

Stats.count("http_get_data").add()
Stats.avg("http_get_data").add(0.7)

Stats.count("no_used")  # не попадет в результат collect

metrics = Stats.collect()
assert metrics == {
    "calc.count": 2,
    "calc.avg": 5.0,
    "calc.timer": 0.4,
    "http_get_data.count": 1,
    "http_get_data.avg": 0.7,
}

metrics = Stats.collect()
assert metrics == {}
```

### 2. Аннотация типов
Для проверки будет использоваться mypy

### 3. Тесты в отдельном модуле

### 4. Перед отправкой на проверку код должен быть прогнан через flake8 и pylint, по желанию еще black
