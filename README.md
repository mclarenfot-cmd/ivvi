# ivvi

Практическая работа по Git и модульной структуре Python-проекта.

## Файлы

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

## Запуск

```bash
python -m src.main
```

## Тесты

```bash
python -m unittest discover -s src/tests
```

## Проверка

```bash
python -m compileall src
```
