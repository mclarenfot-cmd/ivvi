# Modular Auth Orders

Учебный Python-проект для практики модульной архитектуры и работы с Git.

Проект показывает:

- разделение кода на независимые модули;
- контракт авторизации через абстрактный интерфейс;
- передачу зависимости в модуль заказов через конструктор;
- unit-тесты для ключевой бизнес-логики;
- готовую структуру репозитория с `.gitignore`.

## Структура

```text
src/
  core/
    auth_service.py
  auth/
    password_auth_service.py
  orders/
    order_service.py
  main.py
tests/
  test_auth_service.py
  test_order_service.py
```

## Запуск приложения

```bash
python -m src.main
```

## Запуск тестов

```bash
python -m unittest discover -s tests
```

Если установлен `pytest`, можно запустить:

```bash
pytest tests/
```

## Проверка синтаксиса

```bash
python -m compileall src tests
```

