# web-vuln-scanner

Лёгкий сканер веб-уязвимостей (SQLi/XSS) на Python.

## Возможности (план)

- краулер сайта и поиск форм;
- SQL-инъекции: error-based и time-based payload'ы;
- XSS: проверка отражения в ответах;
- rate limiting и вежливые задержки;
- отчёты в текст и JSON;
- только для своих сайтов / с явного разрешения.

## Стек

- Язык: Python 3
- Планируемые библиотеки: `requests`, `beautifulsoup4`

## Сборка и запуск

```bash
pip install -r requirements.txt
python main.py https://example.com
```

## Лицензия

MIT
