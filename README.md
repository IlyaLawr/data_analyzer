# Data Analyzer

**Краткое описание:**  
Консольное приложение на Python для анализа данных с помощью LLM (Gemini API). Автоматически скачивает CSV-датасет с Kaggle, формирует «человеко-читаемую» схему столбцов через Pandas, отправляет задачу модели, выполняет сгенерированный код в безопасном окружении, получает результат и возвращает человеко-читаемый ответ.

**Установка и использование:**  
1. Клонируйте репозиторий и перейдите в папку проекта:
```bash
    git clone <URL>
    cd data_analyzer
```

2. Создайте и активируйте виртуальное окружение:
```bash
    python3 -m venv .venv
    source .venv/bin/activate    # Linux/macOS
    .venv\Scripts\activate       # Windows
```

3. Установите зависимости:
```bash
    pip install --upgrade pip
    pip install -r requirements.txt
```

4. Создайте файл .env в корне проекта и добавьте следующие строки (замените ВАШ_GEMINI_API_KEY на свой ключ):
```ini
URL='https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash-preview-05-20:generateContent?key='
KEY='ВАШ_GEMINI_API_KEY'
PROXY=''  # если делаете запрос на API из РФ то необходим прокси сервер
```

5. Запустите приложение из папки `src`, передав вопрос к модели в кавычках:
```bash
    python main.py Ваш вопрос
```
Примеры вопросов и ответов в папке `result`.


# Структура проекта

```bash
freelance_data_analyzer/
├── .env                            # Переменные окружения (URL Gemini, API-ключ, PROXY)
├── requirements.txt                # Список зависимостей
├── results/                        # Примеры вопросов и ответов
└── src/
    ├── application/
    │   ├── data_analyst.py                 # Формирует запросы к LLM, парсит и обрабатывает код
    │   ├── dataclasses.py                  # Класс Context (role/text)
    │   ├── services/
    │   │   ├── execute_code_service.py     # Безопасное исполнение кода (RestrictedPython)
    │   │   └── source_data_retrieval_service.py  # Скачивание датасета с Kaggle
    │   └── use_case/
    │       └── freelance_data_analysis.py  # Координация всего процесса (Use Case)
    │
    ├── infrastructure/
    │   ├── api/
    │   │   ├── gemini_builder.py           # Формирует JSON-запрос для Gemini
    │   │   ├── gemini_client.py            # Асинхронный клиент (httpx.AsyncClient)
    │   │   ├── gemini_parser.py            # Извлекает текст из ответа LLM
    │   │   └── utils.py                    # Глобальная `system_instruction`
    │   └── pandas_data_schema_generator.py # Чтение CSV и генерация схемы через pandas
    │
    ├── presentation/
    │   └── cli.py                          # Настройка `argparse` (приём аргумента question)
    │
    ├── settings.py                         # Настройки (pydantic: URL, KEY, PROXY из .env)
    └── main.py                             # Точка входа (CLI → Use Case → вывод результата)
```

# При запуске приложение выполнит следующие шаги:

- Скачает CSV-датасет с Kaggle.

- Сформирует схему столбцов (имена, типы, уникальные значения).

- Отправит схему и вопрос в LLM; модель вернёт блок с Python-кодом.

- Выполнит сгенерированный код в безопасном окружении (RestrictedPython) и запишет данные в `result`.

- Повторно отправит `result` в LLM для текстовой интерпретации без кода.

- Выведет итоговый человеко-читаемый ответ в консоль.
