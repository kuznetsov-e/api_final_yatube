# API Yatube

## Описание

Этот проект представляет собой API для социальной сети, где пользователи могут создавать посты, комментировать их, подписываться на других пользователей и группировать посты по категориям. Приложение построено на базе Django и Django REST Framework, что обеспечивает надёжную и масштабируемую серверную часть для управления контентом, созданным пользователями.

### Функциональность:
- **Посты**: Пользователи могут создавать, просматривать, редактировать и удалять свои посты.
- **Комментарии**: Пользователи могут оставлять комментарии к постам.
- **Подписки**: Пользователи могут подписываться на других пользователей, чтобы отслеживать их посты.
- **Группы**: Пользователи могут группировать посты по категориям.

Это API позволяет разработчикам интегрировать функции социальной сети в их приложения.

## Установка

Чтобы запустить этот проект локально, выполните следующие шаги:

### 1. Клонируйте репозиторий и перейдите в директорию проекта

```bash
git clone https://github.com/kuznetsov-e/api_final_yatube.git
cd api_final_yatube
```

### 2. Создайте и активируйте виртуальное окружение

```bash
python3 -m venv env
source env/bin/activate
```

### 3. Установите зависимости

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Примените миграции

```bash
python3 manage.py migrate
```

### 5. Запустите проект

```bash
python3 manage.py runserver
```

Теперь приложение должно быть доступно по адресу `http://127.0.0.1:8000/`.

## Примеры использования API

Ниже приведены примеры взаимодействия с API.

### 1. Получить все посты

**Эндпоинт:**

```
GET /api/v1/posts/
```

**Пример запроса:**

```bash
curl -X GET http://127.0.0.1:8000/api/v1/posts/
```

**Ответ:**

```json
[
    {
        "id": 1,
        "text": "Это пример поста",
        "author": "user_1",
        "image": null,
        "group": null,
        "pub_date": "2024-08-28T06:23:47.942759Z"
    },
    ...
]
```

### 2. Создать новый пост

**Эндпоинт:**

```
POST /api/v1/posts/
```

**Пример запроса:**

```bash
curl -X POST http://127.0.0.1:8000/api/v1/posts/ \
    -H "Authorization: Bearer <your-token>" \
    -H "Content-Type: application/json" \
    -d '{"text": "Содержимое нового поста"}'
```

**Ответ:**

```json
{
    "id": 2,
    "text": "Содержимое нового поста",
    "author": "user_1",
    "image": null,
    "group": null,
    "pub_date": "2024-08-28T06:23:47.942759Z"
}
```

### 3. Подписаться на пользователя

**Эндпоинт:**

```
POST /api/v1/follow/
```

**Пример запроса:**

```bash
curl -X POST http://127.0.0.1:8000/api/v1/follow/ \
    -H "Authorization: Bearer <your-token>" \
    -H "Content-Type: application/json" \
    -d '{"following": "another_user"}'
```

**Ответ:**

```json
{
    "user": "current_user",
    "following": "another_user"
}
```
