## YATUBE_API

**API** (от англ. **A**pplication **P**rogramming **I**nterface, «программный интерфейс
приложения») — это интерфейс для обмена данными.

>Предназначен для взаимодействия frontend и backend составляющей
> приложения **Yatube**. С его помощью можно:

- Получить список всех публикаций. При указании параметров limit и offset 
выдача будет работать с пагинацией
- Добавить новые публикации в коллекцию публикаций
- Получить/обновить(*полностью или частично*)/удалить публикации по id
- Добавить новый комментарий
- Получить все комментарии к публикации
- Получить/обновить(*полностью или частично*)/удалить комментарий к
публикации по id
- Получить список доступных сообществ/информацию о сообществе по id
- Подписаться на пользователя
- Получить все подписки пользователя, сделавшего запрос
- Получить/обновить/проверить JWT-токен

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

Открыть документацию:

```
http://127.0.0.1:8000/redoc/
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

### Авторы: Коновалов Сергей, команда ЯндексПрактикум
