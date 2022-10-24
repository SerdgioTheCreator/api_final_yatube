## YATUBE_API

API (Application Programming Interface) - программный интерфейс
для взаимодействия одной компьютерной программы с другими.

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/SerdgioTheCreator/api_final_yatube
```

```
cd api_final_yatube/
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
source env/bin/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

### Пример запросов:

Создание публикации:

```
http://127.0.0.1:8000/api/v1/posts/
```

```json
{
"text": "string",
"image": "string",
"group": 0
}
```

Добавление комментария:

```
http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/
```

```json
{
  "text": "string"
}
```

Подписка:

```
http://127.0.0.1:8000/api/v1/follow/
```

```json
{
  "following": "string"
}
```

Получить JWT-токен:

```
http://127.0.0.1:8000/api/v1/jwt/create/
```

```json
{
  "username": "string",
  "password": "string"
}
```
