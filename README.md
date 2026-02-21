# HTTP Availability Benchmark Tool

Консольная программа на Python для тестирования доступности серверов по протоколу HTTP. Инструмент замеряет время выполнения запросов и выводит итоговую статистику по каждому хосту.

## Требования
- Python 3.7+
- Библиотека `requests`

## Установка и запуск

1. Склонируйте репозиторий или скачайте файлы.
2. Установите зависимости:
   ```bash
   pip install -r requirements.txt
3.запуск:
    python bench.py -H [https://ya.ru](https://ya.ru),[https://google.com](https://google.com) -C 5
4.Пример работы:
    --- Testing host: [https://ya.ru](https://ya.ru) (5 requests) ---
    Host:      [https://ya.ru](https://ya.ru)
    Success:   5
        Failed:    0
    Errors:    0
    Min:       42.15ms
    Max:       55.40ms
    Avg:       48.22ms
    ------------------------------