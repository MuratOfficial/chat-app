# Chat App

Простое веб-приложение чата, созданное как учебный проект. Разработано с использованием Python и SQLite3. Проект находится на ранней стадии разработки и может содержать ошибки.

## 🛠️ Технологии

- **Язык программирования:** Python
- **База данных:** SQLite3
- **Веб-фреймворк:** Django (предположительно, исходя из структуры проекта)

## 📁 Структура проекта

```text
chat-app/
├── chat/         # Приложение чата
├── chatApp/      # Конфигурация проекта Django
├── db.sqlite3    # Файл базы данных SQLite
└── manage.py     # Утилита управления Django
```


## 🚀 Установка и запуск

1. **Клонируйте репозиторий:**

   ```bash
   git clone https://github.com/MuratOfficial/chat-app.git
   cd chat-app
   ```
2. **Создайте и активируйте виртуальное окружение (опционально):**

  ```bash
  python -m venv venv
  source venv/bin/activate  # Для Windows: venv\Scripts\activate
  ```
3. **Установите зависимости:**

  ```bash
  pip install -r requirements.txt
  ```
  Примечание: Если файл requirements.txt отсутствует, убедитесь, что установлены необходимые зависимости, такие как Django
  
4. **Примените миграции базы данных:**
   
```bash
python manage.py migrate
```

5. **Запустите сервер разработки:**

```bash
python manage.py runserver
```

6. **Откройте браузер и перейдите по адресу:**

```cpp
http://127.0.0.1:8000/
```

## ⚠️ Известные проблемы
* Проект находится в стадии разработки и может содержать ошибки.
* Возможны проблемы с функциональностью чата и интерфейсом пользователя.
* Отсутствует документация и тесты.

## 📌 Планы на будущее
* Улучшение пользовательского интерфейса.
* Добавление аутентификации пользователей.
* Реализация чата в реальном времени с использованием WebSockets.
* Написание тестов для обеспечения стабильности.

## 🤝 Вклад
Вклад приветствуется! Если у вас есть предложения или улучшения, пожалуйста, создайте pull request или откройте issue.
