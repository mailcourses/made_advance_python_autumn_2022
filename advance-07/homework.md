# Домашнее задание advance #07 (тестирование)

### 1. Функция оценки сообщения
Реализовать функцию predict_message_mood, которая приниамает на вход строку, экземпляр модели SomeModel и пороги хорошести.
Функция возвращает:
- "неуд", если предсказание модели меньше bad_threshold
- "отл", если предсказание модели больше good_threshold
- "норм" в остальных случаях

```py
class SomeModel:
    def predict(self, message: str) -> float:
        # реализация не важна


def predict_message_mood(
    message: str,
    model: SomeModel,
    bad_thresholds: float = 0.3,
    good_thresholds: float = 0.8,
) -> str:
    ...


assert predict_message_mood("Чапаев и пустота", model) == "отл"
```

### 2. Тестирование int и метода str.partition()

### 3. Тесты в отдельном модуле

### 4. Перед отправкой на проверку код должен быть прогнан через flake8 и pylint, по желанию еще black
