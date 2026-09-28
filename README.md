# Учебный проект: Python-функции и тестирование

Учебный проект для практики написания функций и модульных тестов на Python.  
В проекте реализованы функции для решения квадратного уравнения, поиска тёзок среди менторов и подсчёта голосов на выборах.

## Структура проекта
PythonEducationNetology/
├── quadratic_equation.py
├── same_name.py
├── votes.py
├── tests/
│ ├── init.py
│ ├── test_quadratic_equation.py
│ ├── test_same_name.py
│ └── test_votes.py
├── README.md
└── ... (venv, .idea, .coverage и др.)

```text

## Реализованные функции

### `quadratic_equation.py`
- `discriminant(a, b, c)` — вычисляет дискриминант квадратного уравнения.
- `solution(a, b, c)` — возвращает корни уравнения, строку `'корней нет'` или `'любое число'`.

### `same_name.py`
- `same_name(courses_list: list) -> list` — возвращает список списков полных имён менторов, которые являются тёзками в рамках каждого курса.

### `votes.py`
- `vote(votes)` — определяет номер победителя или возвращает строку `"Нужен второй тур выборов"`.
- `check_votes_count(votes_count)` — служебная функция для проверки корректности подсчёта голосов (не изменять).
```

## Запуск тестов

### Вариант 1. Только стандартная библиотека (`unittest`)
Дополнительные пакеты не нужны.
```bash
python -m unittest discover tests
````
### Вариант 2. С измерением покрытия (coverage, опционально)
```bash
pip install coverage
coverage run -m unittest discover tests
coverage report -m
```
### Вариант 3. С pytest (опционально)
```bash
pip install pytest coverage
coverage run -m pytest
coverage report -m
```