# Домашнее задание #08

### 1. Найти все анаграммы образца в строке
Написать функцию, которая оптимально находит все позиции анаграммы pattern в строке text.
Оптимально -- за время O(n).

```python
def find_anagrams(text: str, pattern: str) -> List[int]:
    pass


assert find_anagrams("abcba", "abc") == [0, 2]
assert find_anagrams("aaa", "a") == [0, 1, 2]
assert find_anagrams("abc cba xabcd", "abc") == [0, 4, 9]
```

### 2. Тесты

### 3. Проверить и поправить код с помощью pylint и flake8
